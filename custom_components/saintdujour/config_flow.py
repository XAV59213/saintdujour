"""Flux de configuration pour Saints du Jour."""
from homeassistant import config_entries
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gérer l'étape initiale."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_only")
        return self.async_create_entry(title="Saints du Jour", data={})
