"""Composant Saints du Jour pour Home Assistant."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Configurer le composant saintdujour."""
    _LOGGER.info("Initialisation de %s", DOMAIN)
    # Pas de configuration automatique, l'intégration est ajoutée via l'UI
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer une entrée de configuration."""
    _LOGGER.info("Configuration de l'entrée %s pour %s", entry.entry_id, DOMAIN)
    try:
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
        _LOGGER.info("Plateforme sensor configurée avec succès pour %s", entry.entry_id)
        return True
    except Exception as e:
        _LOGGER.error("Erreur lors de la configuration du sensor : %s", e)
        raise ConfigEntryNotReady from e
