"""Flux de configuration pour Saints du Jour."""
import logging
from homeassistant import config_entries
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gérer l'étape initiale."""
        _LOGGER.debug("Démarrage du flux de configuration pour %s", DOMAIN)
        if self._async_current_entries():
            _LOGGER.debug("Entrée existante trouvée, annulation")
            return self.async_abort(reason="single_instance_only")
        
        _LOGGER.debug("Création d'une nouvelle entrée de configuration")
        return self.async_create_entry(title="Saints du Jour", data={})

    async def async_step_import(self, import_data=None):
        """Gérer l'importation automatique."""
        _LOGGER.debug("Importation automatique pour %s", DOMAIN)
        return await self.async_step_user(None)
