"""Flux de configuration pour Saints du Jour."""
import logging

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Ajouter l'intégration en un clic (aucune option)."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_only")

        # Pas de formulaire : HACS installe les fichiers, ce flux crée les capteurs.
        return self.async_create_entry(title="Saints du Jour", data={})
