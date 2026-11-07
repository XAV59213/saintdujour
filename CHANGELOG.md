# Changelog

## Non publié

### Ajouté
- Diagnostics téléchargeables (`diagnostics.py`) : fuseau, taille du calendrier, saints calculés.
- `icons.json` : icône des capteurs via les traductions d’icônes.
- Tests automatisés (pytest-homeassistant-custom-component) : config flow, setup/unload, capteurs (passage de minuit, Noël), diagnostics, carte Lovelace — couverture 100 %. Workflow GitHub Actions **Tests** (ruff, mypy strict, pytest avec seuil 95 %).
- README : entités et attributs, mise à jour des données, cas d’usage et automatisations, limitations, suppression, diagnostics et logs.
- `quality_scale.yaml` : auto-évaluation des 54 règles Quality Scale actuelles (done / todo / exempt justifiés). Aucun niveau officiel revendiqué (intégration custom HACS, manifest inchangé).

### Modifié
- Noms des capteurs pris dans les traductions (`translation_key`) au lieu d’un nom codé en dur ; noms anglais alignés sur `strings.json` pour garder les mêmes entity_id (« Saint du Jour » / « Saint de Demain »).
- Appareil déclaré comme service (`DeviceEntryType.SERVICE`), `PARALLEL_UPDATES = 0`, intervalle de mise à jour 1 min (au lieu de 30 s).
- Typage strict (mypy `--strict`), config flow simplifié (contrôle d’instance unique par `unique_id`), retrait du wrapper `ConfigEntryNotReady` inutile.
- `quality_scale.yaml` mis à jour : plus aucune règle en todo (done prouvés par tests/docs, exempt justifiés). Aucun niveau officiel revendiqué.

### Corrigé
- Calendrier : ajout du 25 décembre (« les Noël », calendrier PTT) qui manquait — les capteurs affichaient « Inconnu » ce jour-là (et la veille pour « Saint de demain »). Test de complétude du calendrier (366 jours) ajouté.

## 1.3.4 - 2026-10-31

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
