# Kerberoasting Vulnerability Report

## Summary
Found {{ total_found }} service accounts with cracked SPN passwords{% if total_admins_enabled > 0 %}, including {{ total_admins_enabled }} privileged and enabled accounts.{% else %}.{% endif %}
Kerberoasting attacks target service accounts with registered SPNs by requesting their Kerberos service tickets and attempting to crack them offline. If successful, the attacker obtains the clear-text password of the associated service account. These accounts often have elevated privileges or broad access within the domain. As a result, Kerberoasting can lead to privilege escalation, unauthorized access to critical systems, and facilitate further lateral movement across the network, potentially compromising the entire domain.

## Vulnerable Service Accounts
| Username | SPN | Password | Domain Admin |
|----------|-----|----------|--------------|
{% for user in all_users %}| {{ user.username }} | {% for spn in user.spn %}{{ spn }}  {% endfor %} | {{ user.password }} | {{ "Yes" if user.is_domain_admin else "No" }} |
{% endfor %} 

## Recommended Actions

- Use a tool for password analysis in Active Directory to identify weak or easily crackable passwords among accounts with registered SPNs (e.g., AD Sonar — [adsonar.ru](https://adsonar.ru/)).

- Use only non-privileged accounts to run services whenever possible. Service accounts should have the minimum necessary permissions required to function.

- Replace traditional service accounts with Group Managed Service Accounts (gMSA), which provide automatic password management and eliminate the need for manually set, potentially weak or reused passwords ([Learn more about gMSA](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview)).

- Regularly audit Active Directory for accounts with SPNs and identify those with elevated privileges. Eliminate unnecessary privileges or unused SPNs.

- Implement strict password policies for all accounts with SPNs, ensuring strong, complex, and regularly rotated passwords.

- Monitor for abnormal Kerberos ticket requests and service ticket activity to detect signs of Kerberoasting attempts.