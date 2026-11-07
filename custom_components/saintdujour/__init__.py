"""Composant Saints du Jour pour Home Assistant."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN
from .frontend import async_register_card

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Configurer le composant saintdujour (chargement de la carte Lovelace)."""
    data: dict[str, bool] = hass.data.setdefault(DOMAIN, {})
    if not data.get("_card_registered"):
        try:
            await async_register_card(hass)
            data["_card_registered"] = True
        except Exception as err:  # noqa: BLE001 - la carte ne doit pas bloquer les capteurs
            _LOGGER.warning("Carte Lovelace non enregistrée : %s", err)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurer une entrée de configuration (crée les capteurs)."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Décharger l'entrée de configuration."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
