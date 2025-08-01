# Unconstrained Delegation Vulnerability Report

## Summary
Found {{ total_found }} accounts with unconstrained delegation enabled.

Unconstrained delegation allows a system or service to impersonate users and access other services on their behalf without restriction. When enabled, the credentials (including Kerberos Ticket Granting Tickets, or TGTs) of any user who authenticates to the delegated system can be cached and reused. If an attacker compromises such a system, they can extract TGTs from memory and impersonate privileged users — including domain admins — across the domain. This exposes the environment to high-risk attacks such as Golden Ticket forging and full domain compromise.

## Vulnerable Accounts Details
| Account | Type | Status |
|---------|------|---------|
{% for item in unconstrained_delegation %}| {{ item.account }} | {{ item.type }} | {% if item.is_enabled %}Enabled{% else %}Disabled{% endif %} |
{% endfor %} 

## Recommended Actions

- Identify and review all accounts and computers with unconstrained delegation enabled, especially those with elevated privileges or exposed to user authentication (e.g., domain-joined servers).

- Disable unconstrained delegation on all accounts and systems unless strictly required for legacy application compatibility.

- Where delegation is needed, use **constrained delegation** (`"Trust this user for delegation to specified services only"`) or **resource-based constrained delegation (RBCD)** as more secure alternatives.

- Isolate systems that require delegation into separate, hardened network segments and monitor them closely for unusual authentication behavior.

- Regularly audit delegation settings via scripts or tools to prevent reintroduction of insecure configurations.
