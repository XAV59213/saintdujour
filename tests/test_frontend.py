"""Tests de l'enregistrement de la carte Lovelace."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from homeassistant.core import HomeAssistant

from custom_components.saintdujour import frontend
from custom_components.saintdujour.const import CARD_URL, URL_BASE

MANIFEST_VERSION = __import__("json").loads(
    (Path(frontend.__file__).parent.parent / "manifest.json").read_text("utf-8")
)["version"]


async def test_enregistre_carte(hass: HomeAssistant) -> None:
    hass.http = MagicMock(async_register_static_paths=AsyncMock())
    with patch.object(frontend, "add_extra_js_url") as add_js:
        await frontend.async_register_card(hass)
    cfg = hass.http.async_register_static_paths.await_args.args[0][0]
    assert cfg.url_path == URL_BASE
    add_js.assert_called_once_with(hass, f"{CARD_URL}?v={MANIFEST_VERSION}")


async def test_chemin_deja_enregistre(hass: HomeAssistant) -> None:
    hass.http = MagicMock(
        async_register_static_paths=AsyncMock(side_effect=RuntimeError)
    )
    with patch.object(frontend, "add_extra_js_url") as add_js:
        await frontend.async_register_card(hass)
    add_js.assert_called_once()


async def test_fichier_absent(hass: HomeAssistant, tmp_path: Path) -> None:
    hass.http = MagicMock(async_register_static_paths=AsyncMock())
    fake = tmp_path / "__init__.py"
    with (
        patch.object(frontend, "__file__", str(fake)),
        patch.object(frontend, "add_extra_js_url") as add_js,
    ):
        await frontend.async_register_card(hass)
    add_js.assert_not_called()
    hass.http.async_register_static_paths.assert_not_called()


def test_version_illisible() -> None:
    with patch.object(frontend, "Path", side_effect=OSError):
        assert frontend._version() == "0"
