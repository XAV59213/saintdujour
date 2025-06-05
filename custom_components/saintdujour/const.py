"""Constantes pour le composant Saints du Jour."""
DOMAIN = "saintdujour"
SENSOR_NAME = "Saint du Jour"
SENSOR_UNIQUE_ID = f"{DOMAIN}_sensor"

# Attributs du capteur
ATTR_SAINT_NAME = "saint_name"
ATTR_FEAST_DAY = "feast_day"

# Exemple de liste statique des saints (à remplacer par une source réelle)
SAINTS_OF_THE_DAY = {
    "01-01": "Marie, Mère de Dieu",
    "06-05": "Saint Boniface",
    "12-25": "Noël",
    # Ajouter d'autres saints ici
}

# Configuration par défaut
DEFAULT_SCAN_INTERVAL = 86400  # Mise à jour quotidienne (en secondes)
