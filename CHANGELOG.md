# Changelog

## Non publié

### Corrigé
- Carte Lovelace : plus d’entity_id préremplis (défauts vides, résolution auto). Si l’entité configurée est vide/absente, la carte écrit l’entity_id réel dans la config (`config-changed`, une seule fois) : fini « Entité inconnue sélectionnée » dans l’éditeur. Un choix valide de l’utilisateur est respecté.

## 1.3.3 - 2026-10-31

### Corrigé
- Carte Lovelace : résolution automatique des capteurs si l’entity_id configuré est absent (attributs `feast_day` + `offset_days`, puis `sensor.saint_du_jour` / `sensor.saints_du_jour_saint_du_jour` et équivalents demain). Fini « Entité introuvable » quand les IDs diffèrent.

## 1.3.1 - 2026-10-31

### Corrigé
- Carte Lovelace : entités par défaut alignées sur les vrais entity_id HA (`sensor.saints_du_jour_saint_du_jour`, `sensor.saints_du_jour_saint_de_demain`) au lieu de `sensor.saint_du_jour` / `sensor.saint_de_demain` (« Entité introuvable »). Doc mise à jour.

## 1.3.0 - 2026-10-31

### Ajouté
- Carte Lovelace native **Saint du jour** (`custom:saintdujour-card`) livrée avec l’intégration : saint du jour + saint de demain, style soigné avec 🙏.
- Éditeur visuel (`getConfigForm`) : sélecteurs d’entités, libellés FR, titre, icône, affichage de demain.
- Chargement automatique du JS depuis le paquet de l’intégration (`/saintdujour/saintdujour-card.js`), sans copie dans `www` ni ressource manuelle.
