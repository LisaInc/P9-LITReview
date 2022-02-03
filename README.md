# P9-LITReview

## Présentation

LITReview est un site permettant de partager autour d’œuvre grâce à un système de demande et de création de critique de livre, article, etc. 
Les différents utilisateurs peuvent communiquer via leur fil d'actualité, en s'abonnant à d'autres utilisateurs. 
Template bootstrap utilisé : https://github.com/startbootstrap/startbootstrap-bare

## Installer le site en local

Créer un environnement virtuel avec venv:

```
python3 -m venv .venv

. .venv/bin/activate
```

Installer Django et ses dépendance:

```pip install -r requirement.txt```

À partir du dossier LITReview, pour lancer le serveur:

```python3 manage.py runserver```

Le site sera à l'adresse http://127.0.0.1:8000/ à partir d'un navigateur.

Ce lien renvoie sur la page de connexion du site, faire un compte pour accéder au reste du site.
