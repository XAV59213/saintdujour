"""Enregistre la carte Lovelace « Saint du jour » auprès de Home Assistant."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant

from ..const import CARD_FILENAME, CARD_URL, URL_BASE

_LOGGER = logging.getLogger(__name__)


def _version() -> str:
    try:
        manifest = Path(__file__).parent.parent / "manifest.json"
        return json.loads(manifest.read_text("utf-8")).get("version", "0")
    except Exception:  # noqa: BLE001
        return "0"


async def async_register_card(hass: HomeAssistant) -> None:
    """Sert le JS depuis le paquet de l'intégration et le charge dans le frontend.

    Aucune copie dans www, aucune ressource Lovelace à ajouter à la main.
    """
    folder = Path(__file__).parent
    if not (folder / CARD_FILENAME).is_file():
        _LOGGER.warning("Fichier de carte introuvable : %s", folder / CARD_FILENAME)
        return
    try:
        await hass.http.async_register_static_paths(
            [StaticPathConfig(URL_BASE, str(folder), False)]
        )
    except RuntimeError:
        _LOGGER.debug("Chemin statique déjà enregistré : %s", URL_BASE)

    version = await hass.async_add_executor_job(_version)
    add_extra_js_url(hass, f"{CARD_URL}?v={version}")
    _LOGGER.debug("Carte Lovelace Saint du jour chargée : %s", CARD_URL)
