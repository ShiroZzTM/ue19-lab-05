# Utiliser une image Python légère comme base
FROM python:3.13

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
COPY app.py ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script Python
CMD ["python", "./app.py"]
