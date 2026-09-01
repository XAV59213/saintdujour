"""Capteurs pour afficher le saint du jour et le saint de demain."""
import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_FEAST_DAY,
    ATTR_OFFSET_DAYS,
    ATTR_SAINT_NAME,
    SAINTS_OF_THE_DAY,
    SENSOR_NAME,
    SENSOR_UNIQUE_ID,
    TOMORROW_SENSOR_NAME,
    TOMORROW_SENSOR_UNIQUE_ID,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
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
        ]
    )


class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour ou de demain."""

    def __init__(
        self,
        name: str,
        unique_id: str,
        translation_key: str,
        offset_days: int = 0,
    ):
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_translation_key = translation_key
        self._attr_icon = "mdi:church"
        self._offset_days = offset_days
        self._state = None
        self._attributes = {}

    async def async_update(self):
        """Met à jour le saint pour la date cible."""
        target_date = (dt_util.now() + timedelta(days=self._offset_days)).date()
        key = target_date.strftime("%d:%m")
        saint_name = SAINTS_OF_THE_DAY.get(key, "Inconnu")

        self._state = saint_name
        self._attributes = {
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

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
