"""Composant Saints du Jour pour Home Assistant."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Configurer le composant saintdujour."""
    _LOGGER.debug("Démarrage de l'initialisation de %s", DOMAIN)
    
    # Créer une entrée de configuration automatiquement si aucune n'existe
    if not hass.config_entries.async_entries(DOMAIN):
        _LOGGER.debug("Aucune entrée de configuration trouvée, création automatique")
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": config_entry_flow.SOURCE_IMPORT}, data={}
            )
        )
    else:
        _LOGGER.debug("Entrée de configuration déjà existante")
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer une entrée de configuration."""
    _LOGGER.debug("Configuration de l'entrée de configuration pour %s", entry.entry_id)
    try:
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
        _LOGGER.debug("Plateforme sensor configurée avec succès")
        return True
    except Exception as e:
        _LOGGER.error("Erreur lors de la configuration de la plateforme sensor : %s", e)
        return False
