# AS-REP Roasting Vulnerability Report

## Summary
Found {{ total_found }} accounts vulnerable to AS-REP Roasting{% if total_admins_enabled > 0 %}, including {{ total_admins_enabled }} privileged and enabled accounts.{% else %}.{% endif %}
AS-REP Roasting targets user accounts that do not require Kerberos pre-authentication. An attacker can request authentication data (AS-REP) for such accounts without knowing their password and then perform offline brute-force or dictionary attacks to recover the clear-text password. If successful, this may lead to unauthorized access, privilege escalation, and further lateral movement within the network. The risk is especially critical if affected accounts have elevated privileges or are used for service operations.

## Vulnerable Users
| Username | Password | Status |
|----------|----------|--------|
{% for user in all_users %}| {{ user.username }} | {{ user.password }} | {{ "Enable" if user.enable else "Disable" }} |
{% endfor %} 

## Recommended Actions

- Use a tool for password and account configuration analysis in Active Directory to identify accounts vulnerable to AS-REP Roasting — i.e., those with the "Do not require Kerberos preauthentication" flag enabled (e.g., AD Sonar — [adsonar.ru](https://adsonar.ru/)).

- Disable the "Do not require Kerberos preauthentication" option (`DONT_REQUIRE_PREAUTH` flag) for all domain accounts, unless explicitly required for operational purposes. Special attention should be paid to accounts with elevated privileges.

- Where the use of this flag is operationally justified, apply compensating controls such as strong, non-dictionary passwords and close monitoring for abnormal Kerberos authentication requests.