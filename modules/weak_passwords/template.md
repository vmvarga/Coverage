# Weak Passwords Vulnerability Report

## Summary
Found {{ total_found }} users with weak passwords{% if total_admins_enabled > 0 %}, including {{ total_admins_enabled }} privileged and enabled accounts.{% else %}.{% endif %}

Weak passwords significantly increase the risk of unauthorized access to critical systems and sensitive data. If an attacker successfully compromises an account — especially one with elevated privileges — this can lead to full domain compromise, lateral movement across the network, data breaches, and disruption of business operations. The presence of active domain accounts with weak or compromised passwords presents a critical vulnerability in the organization's security posture.

## Users with Weak Passwords
| Username | Password | Domain Admin | Status |
|----------|----------|--------------|--------|
{% for user in weak_password_users %}| {{ user.username }} | {{ user.password }} | {{ "Yes" if user.is_domain_admin else "No" }} | {{ "Active" if user.enabled else "Disabled" }} |
{% endfor %}

## Recommended Actions

- Use a tool for password analysis in Active Directory to identify weak, common, or compromised passwords among domain accounts (e.g., AD Sonar — [adsonar.ru](https://adsonar.ru/)).

- Define and enforce a password policy that requires a minimum password length of 12 characters, including numbers, uppercase and lowercase letters, and special characters. Domain accounts should be locked indefinitely after 5 failed login attempts, with manual unlocking required. This policy should be implemented through Group Policy Objects (GPO) or equivalent mechanisms.

- Avoid using common (dictionary-based) or easily guessable passwords. When developing a password policy, include examples of known weak password types.

- Use monitoring tools to detect online password brute-force attacks.