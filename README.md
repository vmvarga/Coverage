# Domain Coverage Analysis Tool

Tool for analyzing domain security based on various data sources:
- LDAP domain dump
- NTDS.dit dump
- Hashcat output

## Installation

### Using UV (Recommended)
```bash
uv venv
uv pip install -r requirements.txt
uv run main.py -h
```

### Old method
```bash
pip install -r requirements.txt
```

## Preparation

To run the script, you need to have the output of ldapdomaindump, secretsdump and the result of a brute-force attack on the obtained *.ntds file

```bash
mkdir ldapdomaindump && cd ldapdomaindump
ldapdomaindump -u vulnad.local\\Administrator -p "1qaz@WSX" 10.10.10.10

cd .. && mkdir DUMP
secretsdump.py vulnad.local/Administrator:1qaz@WSX@10.10.10.10 -outputfile DUMP/DUMP

hashcat -m 1000 DUMP/DUMP.ntds -o DUMP/DUMP.ntds.out /usr/share/wordlists/rockyou.txt
```

## Usage

```bash
usage: main.py [-h] [-l] [--ldd LDD] [--ntds NTDS] [--hashcat HASHCAT] [-o OUTPUT] [-m MODULES] [-v]

Domain Coverage Analysis Tool

options:
  -h, --help            show this help message and exit
  -l, --list-modules    List available modules
  --ldd LDD             Path to LDAP domain dump (JSON file, directory with JSON files, or ZIP archive)
  --ntds NTDS           Path to NTDS.dit dump
  --hashcat HASHCAT     Path to Hashcat output
  -o OUTPUT, --output OUTPUT
                        Path to output report file
  -m MODULES, --modules MODULES
                        Comma-separated list of modules to run (default: all)
  -v, --verbose         Enable verbose output
```

```bash
uv run main.py --ldd <path_to_ldap_dump> --ntds <path_to_ntds_dump> --hashcat <path_to_hashcat_output> --output <output_file>
```

### List modules
```bash
uv run main.py -l
Available modules:
- reversible_encryption
- passwords_reuse
- weak_passwords
- passwords_in_description
- kerberoasting
- pre2k
- asreproasting
- unconstrained_delegation
```

### Analysis using 3 modules:
```bash
uv run main.py --ldd ldapdomaindump --ntds DUMP --hashcat DUMP/DUMP.ntds.out -m passwords_reuse,weak_passwords,passwords_in_description
Parsing LDAP data...
Parsing NTDS data...
Parsing Hashcat output...
Loaded 3 modules
Running modules...
Building report to report.md...
Done!
```

## Module Development

To create a new module:

1. Create a new directory in `modules/`
2. Create `module.py` implementing `IModule` interface
3. Create `template.md` with Jinja2 template for report

Example module structure:
```bash
modules/my_module/
├── module.py
└── template.md
``` 