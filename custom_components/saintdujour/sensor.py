"""Capteur pour afficher le saint du jour."""
import logging
from datetime import date
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, SENSOR_NAME, SENSOR_UNIQUE_ID, SAINTS_OF_THE_DAY, ATTR_SAINT_NAME, ATTR_FEAST_DAY

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Configurer le capteur."""
    _LOGGER.debug("Configuration du capteur pour %s", DOMAIN)
    async_add_entities([SaintDuJourSensor()])
    _LOGGER.debug("Capteur SaintDuJourSensor ajouté")

class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour."""

    def __init__(self):
        self._attr_name = SENSOR_NAME
        self._attr_unique_id = SENSOR_UNIQUE_ID
        self._attr_icon = "mdi:church"
        self._state = None
        self._attributes = {}
        _LOGGER.debug("Initialisation du capteur %s", SENSOR_UNIQUE_ID)

    def update(self):
        """Mettre à jour le saint du jour."""
        _LOGGER.debug("Mise à jour du capteur")
        today = date.today().strftime("%m:%d")
        self._state = SAINTS_OF_THE_DAY.get(today, "Inconnu")
        self._attributes = {
            ATTR_SAINT_NAME: self._state,
            ATTR_FEAST_DAY: today
        }
        _LOGGER.debug("Saint du jour mis à jour : %s (%s)", self._state, today)

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
