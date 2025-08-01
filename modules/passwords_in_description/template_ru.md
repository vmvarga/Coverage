# Passwords in Description Vulnerability Report

## Summary
Found {{ total_found }} accounts with passwords in their descriptions{% if total_admins_enabled > 0 %}, including {{ total_admins_enabled }} privileged and enabled accounts.{% else %}.{% endif %}

Storing passwords in the description field of Active Directory accounts exposes sensitive credentials in clear text to any user or process with read access to directory attributes. This significantly increases the risk of credential theft, especially if the affected accounts have administrative privileges or are active. An attacker with basic read access to the domain could easily harvest these passwords, potentially leading to unauthorized access, privilege escalation, and full domain compromise.

## Vulnerable Accounts Details
| Account | Status | Admin Rights | Password | Description |
|---------|---------|--------------|----------|----------|
{% for item in passwords_in_description %}| {{ item.account }} | {% if item.is_enabled %}Enabled{% else %}Disabled{% endif %} | {% if item.is_admin %}Yes{% else %}No{% endif %} | {{ item.password }} | {{ item.description }}
{% endfor %} 

## Recommended Actions

- Remove any plaintext passwords or other sensitive data from the description fields of all accounts.

- Review account descriptions across the domain to ensure they do not contain confidential or security-relevant information.

- Educate administrators and support staff on the risks of storing passwords or sensitive data in non-secure fields such as account descriptions.

- Implement role-based access controls (RBAC) to restrict read access to account attributes where possible.