from typing import Dict, Any
from core.interfaces import IModule
from core.domain_state import DomainState
from core.utils import mask_password

class ASREPRoastingModule(IModule):
    def __init__(self, template_language):
        self._template_path = f"template_{template_language}.md"
    
    @property
    def template_path(self) -> str:
        return self._template_path
    
    def run(self, domain_state: DomainState) -> Dict[str, Any]:
        """Run AS-REP Roasting check"""
        # Список пользователей, уязвимых к AS-REP Roasting
        all_users = []
        enabled = []
        disabled = []
        for user in domain_state.users.values():
            # Проверяем флаг DONT_REQUIRE_PREAUTH (0x400000)
            if user.user_account_control & 0x400000 and user.enabled:
                enabled.append({
                    "username": user.sam_account_name,
                    "password": mask_password(user.cracked_password) if user.cracked_password else "Not cracked",
                    "enable": user.enabled
                }   )
            elif user.user_account_control & 0x400000 and not user.enabled:
                disabled.append({
                    "username": user.sam_account_name,
                    "password": mask_password(user.cracked_password) if user.cracked_password else "Not cracked",
                    "enable": user.enabled
                })

        all_users = enabled + disabled
        total_admins_enabled = sum(1 for user in all_users if user["enable"])

        if not all_users:
            return {}
        return {
            "template": self.template_path,
            "all_users": all_users,
            "total_found": len(all_users),
            "total_admins_enabled": total_admins_enabled
        } 