"""Composant Saints du Jour pour Home Assistant."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "saintdujour"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer le composant saintdujour."""
    hass.states.async_set(f"{DOMAIN}.loaded", "true")
    return True
