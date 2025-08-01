# Pre-Windows 2000 Compatibility Vulnerability Report

## Summary
Found {{ total_found }} users with Pre-2000 compatibility enabled.

When a computer account is pre-created in Active Directory with the "Pre-Windows 2000" compatibility option enabled, it is assigned a predictable default password based on the computer name (typically the lowercase name without the trailing '$'). An attacker who knows or can guess the computer name may authenticate using this weak password. This can lead to unauthorized domain access, potential privilege escalation, and lateral movement within the network. Such accounts are often overlooked during password audits, increasing the long-term risk of compromise.

## Vulnerable Computers
| Computer | Password | Status |
|----------|----------|--------|
{% for computer in all_users %}| {{ computer.username }} | {{ computer.password }} | {{ "Enable" if computer.status else "Disable" }} |
{% endfor %} 

## Recommended Actions

- Regularly audit computer accounts in Active Directory and remove those that are unused or were created for legacy systems.

- Use tools such as [Pre2k](https://github.com/garrettfoster13/pre2k) or [NetExec (nxc)](https://github.com/NetExec-net/nxc) to identify computer accounts with the UserAccountControl value of 4128 (PASSWD_NOTREQD | WORKSTATION_TRUST_ACCOUNT), which indicates pre-created accounts with predictable default passwords.

- For identified accounts, set unique and strong passwords that are resistant to brute-force attacks.

- When creating new computer accounts, avoid using the "Assign this computer account as a pre-Windows 2000 computer" option to prevent assigning predictable passwords based on the computer name.
