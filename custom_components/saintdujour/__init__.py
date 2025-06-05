"""Composant Saints du Jour pour Home Assistant."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Configurer le composant saintdujour."""
    _LOGGER.info("Début de l'initialisation de %s", DOMAIN)
    
    # Vérifier si une entrée de configuration existe
    existing_entries = hass.config_entries.async_entries(DOMAIN)
    if not existing_entries:
        _LOGGER.info("Aucune entrée trouvée, lancement du flux de configuration automatique")
        try:
            await hass.config_entries.flow.async_init(
                DOMAIN,
                context={"source": config_entry_flow.SOURCE_IMPORT},
                data={}
            )
            _LOGGER.info("Flux de configuration automatique lancé avec succès")
        except Exception as e:
            _LOGGER.error("Erreur lors du lancement du flux automatique : %s", e)
            return False
    else:
        _LOGGER.debug("Entrée de configuration existante trouvée : %s", existing_entries)
    
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
