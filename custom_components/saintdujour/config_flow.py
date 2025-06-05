"""Flux de configuration pour Saints du Jour."""
import logging
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gérer l'étape utilisateur."""
        _LOGGER.info("Démarrage du flux de configuration pour %s", DOMAIN)

        if self._async_current_entries():
            _LOGGER.warning("Entrée existante trouvée, annulation du flux")
            return self.async_abort(reason="single_instance_only")

        if user_input is not None:
            _LOGGER.info("Utilisateur a confirmé l'ajout de l'intégration Saints du Jour")
            return self.async_create_entry(title="Saints du Jour", data={})

        # Afficher un formulaire pour confirmer l'ajout
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            description_placeholders={
                "description": "Voulez-vous ajouter l'intégration Saints du Jour pour afficher le saint du jour dans Home Assistant ?"
            },
            errors={}
        )
