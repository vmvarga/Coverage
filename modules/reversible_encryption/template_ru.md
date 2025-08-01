# Reversible Encryption Vulnerability Report

## Summary
Found {{ total_found }} accounts with reversible encryption enabled{% if total_admins_enabled > 0 %}, including {{ total_admins_enabled }} privileged and enabled accounts.{% else %}.{% endif %}

When reversible encryption is enabled for an account in Active Directory, the password is stored in a format that can be easily decrypted to plain text by any process or user with the appropriate permissions. This significantly increases the risk of credential exposure through misconfigured access rights, backups, or compromised systems. If such an account has administrative privileges or is used in service integrations, an attacker gaining access to the decrypted password may escalate privileges or move laterally within the domain. Reversible encryption should only be used in rare, justified scenarios, as it weakens the overall security posture of the environment.

## Vulnerable Accounts Details
| Account | Type | Status | Admin Rights | Password |
|---------|------|---------|--------------|----------|
{% for item in reversible_encryption %}| {{ item.account }} | {{ item.type }} | {% if item.is_enabled %}Enabled{% else %}Disabled{% endif %} | {% if item.is_admin %}Yes{% else %}No{% endif %} | {{ item.password }} |
{% endfor %} 

## Recommended Actions

- Disable reversible password encryption for all user accounts, unless explicitly required for a specific application or authentication mechanism.

- Review domain and local password policies to ensure that reversible encryption is not enabled by default.

- Educate administrators on the risks of reversible encryption and establish guidelines for secure password storage practices.

- Monitor Group Policy Objects (GPO) and account creation processes to prevent unintended re-enablement of reversible encryption settings.