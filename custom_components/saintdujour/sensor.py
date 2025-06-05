"""Capteur pour afficher le saint du jour."""
from datetime import date
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, SENSOR_NAME, SENSOR_UNIQUE_ID, SAINTS_OF_THE_DAY, ATTR_SAINT_NAME, ATTR_FEAST_DAY

async def async_setup_entry(hass, entry, async_add_entities):
    """Configurer le capteur."""
    async_add_entities([SaintDuJourSensor()])

class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour."""

    def __init__(self):
        self._attr_name = SENSOR_NAME
        self._attr_unique_id = SENSOR_UNIQUE_ID
        self._attr_icon = "mdi:church"
        self._state = None
        self._attributes = {}

    def update(self):
        """Mettre à jour le saint du jour."""
        today = date.today().strftime("%m:%d")
        self._state = SAINTS_OF_THE_DAY.get(today, "Inconnu")
        self._attributes = {
            ATTR_SAINT_NAME: self._state,
            ATTR_FEAST_DAY: today
        }

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
