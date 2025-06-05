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
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer une entrée de configuration."""
    try:
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
        return True
    except Exception as e:
        _LOGGER.error("Erreur lors de la configuration du sensor : %s", e)
        raise ConfigEntryNotReady from e

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Décharger l'entrée de configuration."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
