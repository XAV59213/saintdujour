"""Capteur pour afficher le saint du jour."""
from datetime import date
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, SENSOR_NAME

async def async_setup_entry(hass, entry, async_add_entities):
    """Configurer le capteur."""
    async_add_entities([SaintDuJourSensor()])

class SaintDuJourSensor(SensorEntity):
    """Capteur pour le saint du jour."""

    def __init__(self):
        self._attr_name = SENSOR_NAME
        self._attr_unique_id = f"{DOMAIN}_sensor"
        self._state = None

    def update(self):
        """Mettre à jour le saint du jour."""
        # Exemple : associer une date à un saint (remplacer par une vraie source)
        saints = {
            "2025-06-05": "Saint Boniface",
            # Ajouter d'autres saints
        }
        today = date.today().strftime("%Y-%m-%d")
        self._state = saints.get(today, "Inconnu")

    @property
    def state(self):
        return self._state
