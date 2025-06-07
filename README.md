# 🕊️ Saints du Jour

Un composant personnalisé pour [Home Assistant](https://www.home-assistant.io), permettant d’afficher chaque jour le ou les saints célébrés selon le calendrier liturgique français.

## 📦 Fonctionnalités

- Affiche automatiquement le saint du jour (par exemple : "les Pierre et Paul" pour le 29 juin).
- Mise à jour quotidienne du capteur.
- Intégration native via l’interface graphique Home Assistant.
- Compatible avec une carte Lovelace type `entity`.

## 🛠️ Installation

### Via HACS (recommandé)

1. Ouvrez **HACS > Intégrations**.
2. Cliquez sur les trois points en haut à droite > *Dépôt personnalisé*.
3. Ajoutez ce dépôt GitHub :  

https://github.com/xav59213/xav59213-saints-du-jour

en tant que type `Intégration`.
4. Installez **Saints du Jour** depuis la liste HACS.
5. Redémarrez Home Assistant.

## ⚙️ Configuration

Aucune configuration manuelle n’est nécessaire. Une fois installée, ajoutez l'intégration via **Paramètres > Appareils & Services > Ajouter une intégration** et recherchez **Saints du Jour**.

## 🧾 Exemple de carte Lovelace

Ajoutez ce code à votre tableau de bord pour afficher le capteur :

```yaml
type: entity
entity: sensor.saint_du_jour
name: Saint du Jour

🔍 Détails du capteur
Attribut	Description
state	Nom du saint célébré
saint_name	Nom du saint (identique)
feast_day	Date du jour au format DD:MM
🚀 Développement

    Domaine : saintdujour

    Fichier principal : sensor.py

    Flux de configuration intégré (config_flow)

    Aucune dépendance externe requise

    Code propriétaire : xav59213

❗ Problèmes / Suggestions

Signalez les bugs ou proposez des améliorations via l’onglet Issues du dépôt.
✅ Compatibilité

    Home Assistant 2023.6.0 ou version ultérieure

    Testé sous installation supervisée et Docker

    Local (aucune API externe)
