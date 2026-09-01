# 🪿 Saints du Jour

<p align="center">
  <img src="custom_components/saintdujour/brand/icon.png" alt="Saints du Jour" width="128" height="128">
</p>

<p align="center"><b>Saints du Jour</b> — calendrier liturgique français pour Home Assistant</p>

Un composant personnalisé pour [Home Assistant](https://www.home-assistant.io), permettant d’afficher chaque jour le ou les saints célébrés selon le calendrier liturgique français.

<a href="https://www.buymeacoffee.com/xav59213"><img src="https://img.buymeacoffee.com/button-api/?text=xav59213&emoji=&slug=xav59213&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>

## 📦 Fonctionnalités

- Affiche automatiquement le saint du jour (par exemple : « les Pierre et Paul » pour le 29 juin).
- Mise à jour quotidienne du capteur.
- Intégration native via l’interface graphique Home Assistant.
- Compatible avec une carte Lovelace type `entity`.

## 🛠️ Installation

### Via HACS (recommandé)

1. Ouvrez **HACS > Intégrations**.
2. Cliquez sur les trois points en haut à droite > *Dépôt personnalisé*.
3. Ajoutez ce dépôt GitHub :

   `https://github.com/XAV59213/saintdujour`

   en tant que type **Intégration**.
4. Installez **Saints du Jour** depuis la liste HACS.
5. Redémarrez Home Assistant.

## ⚙️ Configuration

Aucune configuration manuelle n’est nécessaire. Une fois installée, ajoutez l’intégration via **Paramètres > Appareils & services > Ajouter une intégration** et recherchez **Saints du Jour**.

## 🧾 Exemple de carte Lovelace

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint du Jour
```

### Détails du capteur

| Attribut | Description |
| --- | --- |
| `state` | Nom du saint célébré |
| `saint_name` | Nom du saint (identique) |
| `feast_day` | Date du jour au format DD:MM |

## 🚀 Développement

- Domaine : `saintdujour`
- Fichier principal : `sensor.py`
- Flux de configuration intégré (`config_flow`)
- Aucune dépendance externe requise
- Images de marque locales (Home Assistant 2026.3+ / HACS) :
  - `custom_components/saintdujour/brand/icon.png` (256×256)
  - `custom_components/saintdujour/brand/icon@2x.png` (512×512)
  - `custom_components/saintdujour/brand/logo.png`
  - `custom_components/saintdujour/brand/logo@2x.png`

## ❗ Problèmes / suggestions

Signalez les bugs ou proposez des améliorations via l’onglet [Issues](https://github.com/XAV59213/saintdujour/issues) du dépôt.

## ✅ Compatibilité

- Home Assistant 2024.6.0 ou version ultérieure (icônes locales : 2026.3+)
- Testé sous installation supervisée et Docker
- Local (aucune API externe)
