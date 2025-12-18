from typing import Dict, List, Any
from core.domain_state import DomainState
from core.interfaces import IModule

class UnconstrainedDelegationModule(IModule):
    def __init__(self, template_language):
        self._template_path = f"template_{template_language}.md"
    
    @property
    def template_path(self) -> str:
        return self._template_path
    
    def run(self, domain_state: DomainState) -> Dict[str, Any]:
        """
        Check for accounts with unconstrained delegation enabled
        """
        findings = []
        
        # Process users
        for user in domain_state.users.values():
            if user.user_account_control & 0x80000:  # TRUSTED_FOR_DELEGATION flag
                findings.append({
                    "account": user.sam_account_name,
                    "type": "USER",
                    "is_enabled": user.enabled
                })
        
        # Process computers (excluding domain controllers)
        for computer in domain_state.computers.values():
            # Skip domain controllers (SERVER_TRUST_ACCOUNT flag = 0x2000)
            if computer.user_account_control & 0x2000:
                continue
            if computer.user_account_control & 0x80000:  # TRUSTED_FOR_DELEGATION flag
                findings.append({
                    "account": computer.sam_account_name,
                    "type": "COMPUTER",
                    "is_enabled": computer.enabled
                })
        
        # Sort findings: admins first, then enabled accounts, then disabled
        findings.sort(key=lambda x: (
            not x["is_enabled"],  # True sorts after False, so we negate
            x["account"]  # Secondary sort by account name
        ))
        
        if not findings:
            return {}
            
        return {
            "template": self.template_path,
            "unconstrained_delegation": findings,
            "total_found": len(findings)
        } 