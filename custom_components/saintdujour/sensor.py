"""Capteurs pour afficher le saint du jour et le saint de demain."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_FEAST_DAY,
    ATTR_OFFSET_DAYS,
    ATTR_SAINT_NAME,
    DOMAIN,
    SAINTS_OF_THE_DAY,
    SENSOR_UNIQUE_ID,
    TOMORROW_SENSOR_UNIQUE_ID,
)

_LOGGER = logging.getLogger(__name__)

# Calcul local sans I/O : aucune limite de parallélisme nécessaire.
PARALLEL_UPDATES = 0
# La valeur ne change qu'à minuit : une minute suffit (au plus 1 min de retard).
SCAN_INTERVAL = timedelta(minutes=1)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configurer les capteurs."""
    async_add_entities(
        [
            SaintDuJourSensor(SENSOR_UNIQUE_ID, "saint_du_jour", 0),
            SaintDuJourSensor(TOMORROW_SENSOR_UNIQUE_ID, "saint_de_demain", 1),
        ],
        update_before_add=True,
    )


def saint_for(offset_days: int) -> tuple[str, str]:
    """Retourne (clé JJ:MM, saint) pour aujourd'hui + offset_days."""
    target_date = (dt_util.now() + timedelta(days=offset_days)).date()
    key = target_date.strftime("%d:%m")
    return key, SAINTS_OF_THE_DAY.get(key, "Inconnu")


class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour ou de demain."""

    _attr_has_entity_name = True
    _attr_should_poll = True

    def __init__(self, unique_id: str, translation_key: str, offset_days: int) -> None:
        """Initialiser le capteur."""
        self._attr_unique_id = unique_id
        self._attr_translation_key = translation_key
        self._offset_days = offset_days
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, DOMAIN)},
            name="Saints du Jour",
            manufacturer="XAV59213",
            model="Calendrier liturgique",
            entry_type=DeviceEntryType.SERVICE,
        )

    async def async_update(self) -> None:
        """Met à jour le saint pour la date cible."""
        key, saint_name = saint_for(self._offset_days)
        self._attr_native_value = saint_name
        self._attr_extra_state_attributes = {
            ATTR_SAINT_NAME: saint_name,
            ATTR_FEAST_DAY: key,
            ATTR_OFFSET_DAYS: self._offset_days,
        }
        _LOGGER.debug("Mise à jour %s (%s) : %s", self.unique_id, key, saint_name)
