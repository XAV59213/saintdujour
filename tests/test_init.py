"""Tests setup/unload, config flow, capteurs, diagnostics."""

from unittest.mock import AsyncMock, patch

from freezegun.api import FrozenDateTimeFactory
from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import (
    MockConfigEntry,
    async_fire_time_changed,
)

from custom_components.saintdujour.const import DOMAIN
from custom_components.saintdujour.diagnostics import (
    async_get_config_entry_diagnostics,
)

TODAY = "sensor.saints_du_jour_saint_du_jour"
TOMORROW = "sensor.saints_du_jour_saint_de_demain"


async def _setup(hass: HomeAssistant) -> MockConfigEntry:
    entry = MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, title="Saints du Jour")
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


async def test_config_flow_cree_entree(hass: HomeAssistant, mock_card: AsyncMock) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "Saints du Jour"
    assert result["data"] == {}
    assert result["result"].unique_id == DOMAIN


async def test_config_flow_instance_unique(hass: HomeAssistant, mock_card: AsyncMock) -> None:
    MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN).add_to_hass(hass)
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"


async def test_setup_unload(hass: HomeAssistant, mock_card: AsyncMock) -> None:
    entry = await _setup(hass)
    assert entry.state is ConfigEntryState.LOADED
    mock_card.assert_awaited_once()
    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
    assert entry.state is ConfigEntryState.NOT_LOADED
    # Rechargement : la carte n'est enregistrée qu'une fois.
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    mock_card.assert_awaited_once()


async def test_echec_carte_ne_bloque_pas(hass: HomeAssistant) -> None:
    with patch(
        "custom_components.saintdujour.async_register_card",
        side_effect=RuntimeError("boom"),
    ):
        entry = await _setup(hass)
    assert entry.state is ConfigEntryState.LOADED
    assert hass.states.get(TODAY) is not None


async def test_capteurs_noel(
    hass: HomeAssistant,
    mock_card: AsyncMock,
    freezer: FrozenDateTimeFactory,
    entity_registry: er.EntityRegistry,
    device_registry: dr.DeviceRegistry,
) -> None:
    await hass.config.async_set_time_zone("Europe/Paris")
    freezer.move_to("2026-12-24 12:00:00+01:00")
    await _setup(hass)

    today = hass.states.get(TODAY)
    tomorrow = hass.states.get(TOMORROW)
    assert today.state == "les Adele"
    assert today.attributes["feast_day"] == "24:12"
    assert today.attributes["offset_days"] == 0
    assert tomorrow.state == "les Noël"
    assert tomorrow.attributes["feast_day"] == "25:12"
    assert tomorrow.attributes["offset_days"] == 1
    assert today.attributes["friendly_name"] == "Saints du Jour Saint du Jour"

    assert entity_registry.async_get(TODAY).unique_id == "saintdujour_sensor"
    assert entity_registry.async_get(TOMORROW).unique_id == "saintdujour_sensor_tomorrow"
    device = device_registry.async_get(entity_registry.async_get(TODAY).device_id)
    assert device is not None
    assert device.identifiers == {(DOMAIN, DOMAIN)}
    assert device.entry_type is dr.DeviceEntryType.SERVICE

    # Passage de minuit : mise à jour au plus tard à l'intervalle suivant.
    freezer.move_to("2026-12-25 00:00:30+01:00")
    async_fire_time_changed(hass)
    await hass.async_block_till_done()
    assert hass.states.get(TODAY).state == "les Noël"
    assert hass.states.get(TOMORROW).state == "les Etienne"


async def test_diagnostics(
    hass: HomeAssistant,
    mock_card: AsyncMock,
    freezer: FrozenDateTimeFactory,
) -> None:
    await hass.config.async_set_time_zone("Europe/Paris")
    freezer.move_to("2026-12-25 08:00:00+01:00")
    entry = await _setup(hass)
    diag = await async_get_config_entry_diagnostics(hass, entry)
    assert diag["calendar_size"] == 366
    assert diag["today"] == {"feast_day": "25:12", "saint": "les Noël"}
    assert diag["tomorrow"] == {"feast_day": "26:12", "saint": "les Etienne"}
    assert diag["entry"]["data"] == {}
