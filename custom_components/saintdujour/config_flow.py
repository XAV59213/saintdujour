"""Flux de configuration pour Saints du Jour."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class SaintDuJourConfigFlow(ConfigFlow, domain=DOMAIN):
    """Gérer le flux de configuration."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ajouter l'intégration en un clic (aucune option)."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        # Pas de formulaire : HACS installe les fichiers, ce flux crée les capteurs.
        return self.async_create_entry(title="Saints du Jour", data={})
