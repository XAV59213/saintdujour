"""Fixtures communes."""

from collections.abc import Generator
from unittest.mock import AsyncMock, patch

import pytest


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations: None) -> None:
    """Activer custom_components/ dans les tests."""


@pytest.fixture
def mock_card() -> Generator[AsyncMock]:
    """Neutraliser l'enregistrement de la carte (frontend non chargé en test)."""
    with patch(
        "custom_components.saintdujour.async_register_card", new=AsyncMock()
    ) as mock:
        yield mock
