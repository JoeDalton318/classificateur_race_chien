# 🐕 Classificateur de Races de Chiens – Deep Learning & WebApp

## Présentation

Ce projet a été réalisé dans le cadre d'une mission bénévole pour une association de protection animale. L'objectif est de faciliter l'indexation des photos de chiens recueillis, en automatisant la détection de leur race à partir d'une simple image.

Nous avons développé une application web permettant d'uploader une photo de chien et d'obtenir instantanément le Top 3 des races les plus probables, grâce à un modèle de Deep Learning entraîné sur le **Stanford Dogs Dataset**.

---

## Fonctionnalités

- **Classification automatique** des races de chiens à partir d'une image.
- **Top 3** des races les plus probables avec pourcentages de confiance.
- **Historique** des dernières analyses réalisées.
- **Interface moderne**, responsive, avec drag & drop pour l'upload d'image.
- **Déploiement facile** (Flask, Keras, Tensorflow).

---

## Approche technique

Nous avons comparé deux méthodes :

1. **Réseau CNN personnalisé**  
   - Conception et entraînement d'un CNN "from scratch".
   - Optimisation des hyperparamètres (epochs, batch size, fonctions d'activation, etc.).

2. **Transfer Learning**  
   - Utilisation de modèles pré-entraînés (Xception, VGG16, MobileNet, etc.).
   - Fine-tuning sur le Stanford Dogs Dataset.
   - Data augmentation pour améliorer la robustesse.

Le modèle final sélectionné est basé sur le **Transfer Learning** (Xception), offrant un excellent compromis entre précision et rapidité.

---

## Prérequis

- Python 3.8+
- pip

---

## Installation

1. **Clonez le dépôt**  
   ```bash
   git clone https://github.com/votre-utilisateur/dog-breed-classifier.git
   cd dog-breed-classifier
   ```

2. **Installez les dépendances**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Placez le modèle et les labels**  
   - Le fichier du modèle (`mon_modele(2).h5`) et le fichier des labels (`labels.json`) doivent être à la racine du projet.
   - Un dossier `uploads` sera créé automatiquement pour stocker les images uploadées.

---

## Lancer l’application

```bash
python app.py
```

Ouvrez ensuite votre navigateur à l’adresse [http://localhost:5000](http://localhost:5000).

---

## Utilisation

1. **Uploadez une image de chien** (drag & drop ou clic).
2. Cliquez sur **Analyser la race**.
3. Consultez le Top 3 des races prédites et l’historique des analyses.

---

## Organisation du projet

- `app.py` : Backend Flask (serveur web, prédiction, gestion historique)
- `templates/index.html` : Frontend HTML/CSS/JS (interface utilisateur)
- `mon_modele(2).h5` : Modèle Keras/Tensorflow entraîné
- `labels.json` : Mapping des indices vers les noms de races
- `uploads/` : Images uploadées par les utilisateurs
- `requirements.txt` : Dépendances Python

---

## Ressources & Références

- [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)
- [Tutoriel Transfer Learning Tensorflow](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [COCO Dataset](https://cocodataset.org/#home)

---

## Pour aller plus loin

- Déploiement sur Azure ou GCP (voir support de présentation).
- Ajout d’une authentification pour les bénévoles.
- Extension à d’autres espèces animales.

---

## Remerciements

Merci à l’association, à tous les bénévoles et à Snooky 🐕 pour l’inspiration !

---

## Auteurs

- Gills Daryl KETCHA NZOUNDJI JIEPMOU pour la conception et le développement de la Web App.
- Frédéric FERNANDEZ DA COSTA et Narcisse Cabrel TSAFACK FOUEGAP pour le modèle de prédiction

---

## Licence

Projet open-source, usage libre pour toute association de protection animale.
