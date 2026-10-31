# 🪿 Saints du Jour

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz) [![Release](https://img.shields.io/github/v/release/XAV59213/saintdujour?label=release)](https://github.com/XAV59213/saintdujour/releases/latest) [![Hassfest](https://img.shields.io/github/actions/workflow/status/XAV59213/saintdujour/hassfest.yml?branch=main&label=Hassfest&logo=github)](https://github.com/XAV59213/saintdujour/actions/workflows/hassfest.yml) [![HACS validation](https://img.shields.io/github/actions/workflow/status/XAV59213/saintdujour/hacs.yml?branch=main&label=HACS%20validation&logo=github)](https://github.com/XAV59213/saintdujour/actions/workflows/hacs.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Downloads](https://img.shields.io/github/downloads/XAV59213/saintdujour/total.svg?label=Downloads)](https://github.com/XAV59213/saintdujour/releases) [![Version](https://img.shields.io/github/v/release/XAV59213/saintdujour?label=VERSION&color=blue)](https://github.com/XAV59213/saintdujour/releases/latest) [![Home Assistant](https://img.shields.io/badge/HOME%20ASSISTANT-%3E%3D2024.6.0-41BDF5.svg)](https://www.home-assistant.io)

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=xav59213&emoji=&slug=xav59213&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/xav59213)

## Via HACS (recommandé)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=saintdujour&category=integration)

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=saintdujour)


<p align="center">
  <img src="https://raw.githubusercontent.com/XAV59213/saintdujour/main/custom_components/saintdujour/brand/icon.svg" alt="Saints du Jour" width="128" height="128">
</p>

<p align="center"><b>Saints du Jour</b> — calendrier liturgique français pour Home Assistant</p>

Un composant personnalisé pour [Home Assistant](https://www.home-assistant.io), permettant d’afficher chaque jour le ou les saints célébrés selon le calendrier liturgique français.


## 📦 Fonctionnalités

- Affiche automatiquement le saint du jour (par exemple : « les Pierre et Paul » pour le 29 juin).
- Affiche aussi le saint de demain (`sensor.saints_du_jour_saint_de_demain`), utile si l’on célèbre la veille.
- Mise à jour quotidienne des capteurs.
- Intégration native via l’interface graphique Home Assistant.
- Carte Lovelace native **Saint du jour** (`custom:saintdujour-card`) livrée avec l’intégration, avec éditeur visuel.

## 🛠️ Installation

### Via HACS (recommandé)


1. Ouvrez **HACS**.
2. Menu ⋮ → **Dépôts personnalisés**.
3. Ajoutez `https://github.com/XAV59213/saintdujour` en type **Intégration**.
4. Cherchez **Saints du Jour** dans HACS et cliquez **Télécharger**.
5. **Ensuite seulement**, redémarrez Home Assistant.
6. Allez dans **Paramètres → Appareils & services → Ajouter une intégration** et ajoutez **Saints du Jour**.

⚠️ HACS installe seulement les fichiers. Les capteurs `sensor.saints_du_jour_saint_du_jour` et `sensor.saints_du_jour_saint_de_demain` n’apparaissent **qu’après** l’étape 6. L’entité `update.saints_du_jour` vient de HACS (mise à jour du composant), ce n’est pas le capteur du saint.

> **Le dépôt disparaît après un redémarrage ?**  
> HACS retire les dépôts personnalisés qui n’ont pas encore été téléchargés. Ajoutez le dépôt, téléchargez l’intégration, *puis* redémarrez.

### Installation manuelle

Copiez `custom_components/saintdujour/` dans `/config/custom_components/`, redémarrez, puis ajoutez l’intégration depuis l’interface.

## ⚙️ Configuration

Aucune configuration manuelle n’est nécessaire une fois l’intégration ajoutée.

## 🙏 Carte Lovelace native

L’intégration embarque sa propre carte : rien à copier dans `www`, aucune ressource à ajouter. Le fichier est servi depuis `custom_components/saintdujour/frontend/saintdujour-card.js` (URL `/saintdujour/saintdujour-card.js`) et chargé automatiquement au démarrage de Home Assistant.

1. Installer / mettre à jour l’intégration puis **redémarrer** Home Assistant (vider le cache du navigateur si besoin).
2. Tableau de bord → **Modifier** → **Ajouter une carte** → chercher **« Saint du jour »**.
3. Régler dans l’éditeur : entités du jour / de demain, libellés, titre, icône, affichage de demain.

En YAML :

```yaml
type: custom:saintdujour-card
title: 🙏 Saints du jour
entity_today: sensor.saints_du_jour_saint_du_jour
entity_tomorrow: sensor.saints_du_jour_saint_de_demain
label_today: Saint du jour
label_tomorrow: Saint de demain
icon: 🙏
show_tomorrow: true
```

| Option | Défaut | Description |
| --- | --- | --- |
| `title` | `🙏 Saints du jour` | Titre (vide = pas de titre) |
| `entity_today` | *(vide = auto)* | Capteur du jour |
| `entity_tomorrow` | *(vide = auto)* | Capteur de demain |
| `label_today` / `label_tomorrow` | `Saint du jour` / `Saint de demain` | Libellés |
| `icon` | `🙏` | Emoji affiché devant chaque ligne |

La carte retrouve automatiquement les capteurs (attributs `feast_day` / `offset_days`) même si les entity_id ont été renommés ou diffèrent ; une entité valide choisie dans l’éditeur reste prioritaire. Si l’entité est vide ou absente, l’éditeur est rempli automatiquement avec l’entity_id réel trouvé.
| `show_tomorrow` | `true` | Affiche la ligne de demain |

## 🧾 Exemple de carte Lovelace (standard)

```yaml
type: entities
entities:
  - entity: sensor.saints_du_jour_saint_du_jour
    name: Saint du Jour
  - entity: sensor.saints_du_jour_saint_de_demain
    name: Saint de Demain
```

### Détails des capteurs

| Entité | Description |
| --- | --- |
| `sensor.saints_du_jour_saint_du_jour` | Saint célébré aujourd’hui |
| `sensor.saints_du_jour_saint_de_demain` | Saint célébré demain |

| Attribut | Description |
| --- | --- |
| `state` | Nom du saint célébré |
| `saint_name` | Nom du saint (identique) |
| `feast_day` | Date au format DD:MM |
| `offset_days` | `0` aujourd’hui, `1` demain |

## 🐞 Dépannage

### Je ne vois que `update.saints_du_jour`

C’est normal après HACS. Cette entité sert à mettre à jour le module. Pour créer les capteurs :

1. Redémarrer Home Assistant si ce n’est pas déjà fait.
2. **Paramètres → Appareils & services → Ajouter une intégration**.
3. Chercher **Saints du Jour** (ou **Saint du Jour**) et valider.

Les capteurs apparaissent alors sous l’appareil **Saints du Jour**.

## 🚀 Développement

- Domaine : `saintdujour`
- Fichier principal : `sensor.py`
- Flux de configuration intégré (`config_flow`)
- Aucune dépendance externe requise
- Images de marque locales (Home Assistant 2026.3+ / HACS) dans `custom_components/saintdujour/brand/` :
  - `icon.png` — 256×256
  - `icon@2x.png` — 512×512
  - `logo.png` / `logo@2x.png`
  - `icon.svg` — source vectorielle

## ❗ Problèmes / suggestions

Signalez les bugs ou proposez des améliorations via l’onglet [Issues](https://github.com/XAV59213/saintdujour/issues) du dépôt.

## ✅ Compatibilité

- Home Assistant 2024.6.0 ou version ultérieure (icônes locales : 2026.3+)
- Testé sous installation supervisée et Docker
- Local (aucune API externe)
