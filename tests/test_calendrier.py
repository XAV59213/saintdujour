"""Non-régression : le calendrier des saints couvre chaque jour de l'année."""
from datetime import date, timedelta
import importlib.util
from pathlib import Path

_CONST = Path(__file__).parents[1] / "custom_components" / "saintdujour" / "const.py"
_spec = importlib.util.spec_from_file_location("saintdujour_const", _CONST)
const = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(const)


def test_25_decembre_present():
    assert const.SAINTS_OF_THE_DAY["25:12"] == "les Noël"


def test_calendrier_complet_annee_bissextile():
    attendus = {
        (date(2024, 1, 1) + timedelta(days=i)).strftime("%d:%m") for i in range(366)
    }
    assert set(const.SAINTS_OF_THE_DAY) == attendus
    assert all(v and v != "Inconnu" for v in const.SAINTS_OF_THE_DAY.values())
