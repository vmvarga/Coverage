from typing import Dict, Any
from core.interfaces import IModule
from core.domain_state import DomainState
from core.utils import mask_password
from Crypto.Hash import MD4
import binascii

class Pre2kModule(IModule):
    def __init__(self, template_language):
        self._template_path = f"template_{template_language}.md"
    
    @property
    def template_path(self) -> str:
        return self._template_path
    
    def get_hash(self, password: str) -> str:
        """Calculate MD4 hash of password"""
        md4 = MD4.new()
        md4.update(password.encode("utf-16le"))
        return md4.hexdigest()

    def run(self, domain_state: DomainState) -> Dict[str, Any]:
        """Run Pre-2000 compatibility check"""
        # List of users with Pre-2000 compatibility
        all_users = []
        enabled = []
        disabled = []
        for comp_name, computer in domain_state.computers.items():
            pre2kpass = computer.sam_account_name.replace("$", "").lower()
            if self.get_hash(pre2kpass) == computer.nt_hash:
                userdata = {
                        "username": computer.sam_account_name,
                        "password": pre2kpass,
                        "status": computer.enabled
                    }
                if computer.enabled:
                    enabled.append(userdata)
                else:
                    disabled.append(userdata)

        all_users = enabled + disabled
        
        if not all_users:
            return {}
        return {
            "template": self.template_path,
            "all_users": all_users,
            "total_found": len(all_users)
        }