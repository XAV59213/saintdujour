"""Capteurs pour afficher le saint du jour et le saint de demain."""
import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_FEAST_DAY,
    ATTR_OFFSET_DAYS,
    ATTR_SAINT_NAME,
    DOMAIN,
    SAINTS_OF_THE_DAY,
    SENSOR_NAME,
    SENSOR_UNIQUE_ID,
    TOMORROW_SENSOR_NAME,
    TOMORROW_SENSOR_UNIQUE_ID,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configurer les capteurs."""
    async_add_entities(
        [
            SaintDuJourSensor(
                name=SENSOR_NAME,
                unique_id=SENSOR_UNIQUE_ID,
                translation_key="saint_du_jour",
                offset_days=0,
            ),
            SaintDuJourSensor(
                name=TOMORROW_SENSOR_NAME,
                unique_id=TOMORROW_SENSOR_UNIQUE_ID,
                translation_key="saint_de_demain",
                offset_days=1,
            ),
        ],
        update_before_add=True,
    )


class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour ou de demain."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:church"
    _attr_should_poll = True

    def __init__(
        self,
        name: str,
        unique_id: str,
        translation_key: str,
        offset_days: int = 0,
    ) -> None:
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_translation_key = translation_key
        self._offset_days = offset_days
        self._attr_native_value = None
        self._attr_extra_state_attributes = {}
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, DOMAIN)},
            name="Saints du Jour",
            manufacturer="XAV59213",
            model="Calendrier liturgique",
        )

    async def async_update(self) -> None:
        """Met à jour le saint pour la date cible."""
        target_date = (dt_util.now() + timedelta(days=self._offset_days)).date()
        key = target_date.strftime("%d:%m")
        saint_name = SAINTS_OF_THE_DAY.get(key, "Inconnu")

        self._attr_native_value = saint_name
        self._attr_extra_state_attributes = {
            ATTR_SAINT_NAME: saint_name,
            ATTR_FEAST_DAY: key,
            ATTR_OFFSET_DAYS: self._offset_days,
        }
        _LOGGER.debug(
            "Mise à jour de %s (%s) : %s",
            self._attr_name,
            key,
            saint_name,
        )
