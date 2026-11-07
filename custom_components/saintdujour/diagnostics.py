"""Diagnostics pour Saints du Jour."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import SAINTS_OF_THE_DAY
from .sensor import saint_for


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Retourner les diagnostics d'une entrée (aucune donnée sensible)."""
    today_key, today = saint_for(0)
    tomorrow_key, tomorrow = saint_for(1)
    return {
        "entry": {
            "title": entry.title,
            "version": entry.version,
            "data": dict(entry.data),
            "options": dict(entry.options),
        },
        "time_zone": hass.config.time_zone,
        "calendar_size": len(SAINTS_OF_THE_DAY),
        "today": {"feast_day": today_key, "saint": today},
        "tomorrow": {"feast_day": tomorrow_key, "saint": tomorrow},
    }
