"""Flux de configuration pour Saints du Jour."""
import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gérer l'étape utilisateur."""
        _LOGGER.info("Démarrage du flux de configuration utilisateur pour %s", DOMAIN)

        if self._async_current_entries():
            _LOGGER.warning("Entrée existante trouvée, annulation du flux")
            return self.async_abort(reason="single_instance_only")

        if user_input is not None:
            _LOGGER.info("Utilisateur a confirmé l'ajout de l'intégration")
            return self.async_create_entry(title="Saints du Jour", data={})

        # Afficher un formulaire demandant si l'utilisateur veut ajouter l'intégration
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            description_placeholders={
                "description": "Voulez-vous ajouter l'intégration Saints du Jour pour afficher le saint du jour ?"
            }
        )

    async def async_step_import(self, import_data=None):
        """Gérer l'importation automatique."""
        _LOGGER.info("Exécution du flux d'importation automatique pour %s", DOMAIN)
        if self._async_current_entries():
            _LOGGER.warning("Entrée existante trouvée, annulation de l'importation")
            return self.async_abort(reason="single_instance_only")
        
        _LOGGER.info("Création automatique de l'entrée de configuration")
        return self.async_create_entry(title="Saints du Jour", data={})
