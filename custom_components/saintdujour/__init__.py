"""Composant Saints du Jour pour Home Assistant."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Configurer le composant saintdujour."""
    # Créer une entrée de configuration automatiquement si aucune n'existe
    if not hass.config_entries.async_entries(DOMAIN):
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": config_entry_flow.SOURCE_IMPORT}, data={}
            )
        )
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer une entrée de configuration."""
    # Transférer la configuration au capteur
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True
