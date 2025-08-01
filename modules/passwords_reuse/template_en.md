# Password Reuse Vulnerability Report

## Summary
Found {{ total_found }} instances of password reuse with administrative accounts.

Password reuse across administrative accounts significantly increases the risk of lateral movement and privilege escalation in the event of a single account compromise. If an attacker gains access to one system or user, reused credentials can enable access to other critical systems without further exploitation. This undermines segmentation and containment strategies, and may lead to full domain compromise, data breaches, and disruption of business operations.

## Password Reuse Details
| Admin Account | Reuse Accounts | Password |
|---------------|----------------|----------|
{% for item in password_reuse %}| {{ item.admin_account }} | {% for acc in item.reuse_accounts %}{{ acc }}<br>{% endfor %} | {{ item.password }} |
{% endfor %} 

## Recommended Actions

- Use a tool for password analysis in Active Directory to identify reused passwords among domain accounts (e.g., AD Sonar — [adsonar.ru](https://adsonar.ru/)).

- Define and enforce a policy that requires the use of unique, strong passwords for all administrative accounts to prevent reuse across systems and services.

- Implement automatic generation and scheduled rotation of unique, strong local administrator passwords for each computer using Microsoft LAPS ([Local Administrator Password Solution](https://technet.microsoft.com/en-us/mt227395.aspx)).