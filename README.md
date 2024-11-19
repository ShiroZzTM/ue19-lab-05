# ⚽ **Football Data API App**

> Une application simple pour explorer les compétitions de football à l'aide de l'API Football-Data.

## 🎯 **Description**

Cette application Python interagit avec l'API **Football-Data** pour récupérer et afficher des informations sur les compétitions de football disponibles dans le monde entier. L'objectif est de simplifier l'accès aux données de football et de rendre ces informations accessibles même pour les débutants.

---

## 📂 **Structure du projet**

```plaintext
ue19-lab-05/
├── app.py             # Script Python principal
├── requirements.txt   # Liste des dépendances Python
├── Dockerfile         # Configuration pour conteneur Docker
└── README.md          # Documentation du projet
```

---

## 🛠️ **Fonctionnalités**

- 📋 **Liste des compétitions disponibles** : Affiche jusqu'à 10 compétitions de football.
- 🌍 **Détails régionaux** : Indique la zone géographique de chaque compétition.
- 🚀 **Prêt à l'emploi** : Aucun besoin de clé API ou d'authentification.
- 🐳 **Support Docker** : Déploiement simplifié via conteneurs.

---

## 🚀 **Prérequis**

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre machine :

1. **Python 3.13**
2. **Docker (facultatif, pour l'exécution dans un conteneur)**

---

## 📦 **Installation**

### 1. **Cloner le projet**
Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/ShiroZzTM/ue19-lab-05.git
cd ue19-lab-05
```

---

## 🖥️ **Exemple de sortie**

Lors de l'exécution, l'application retourne une liste des compétitions disponibles, par exemple :

```plaintext
Liste des compétitions disponibles :

Nom : Premier League
Code : PL
Zone : England

Nom : Bundesliga
Code : BL1
Zone : Germany

Nom : La Liga
Code : PD
Zone : Spain

...
```

