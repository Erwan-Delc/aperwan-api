# Aper'wan API

API REST pour la gestion de l'application Aper'wan — un commerce de planches apéritives locales.

## 🧱 Stack technique

- **FastAPI** – Framework backend rapide et moderne  
- **SQLAlchemy** – ORM pour base MySQL  
- **Pydantic** – Validation de données  
- **Uvicorn** – Serveur ASGI léger  

## 📁 Structure du projet

```bash
aperwan-api/ 
├── app/ 
│   │ 
│   ├── api/ ← Routes (endpoints) 
│   │ 
│   ├── core/ ← Configs globales 
│   │ 
│   ├── crud/ ← Fonctions CRUD 
│   │ 
│   ├── db/ ← Connexion DB 
│   │ 
│   ├── models/ ← Modèles SQLAlchemy 
│   │ 
│   ├── schemas/ ← Schémas Pydantic 
│   │ 
│   └── main.py ← Point d'entrée FastAPI 
├── requirements.txt 
└── README.md
```

## 🚀 Lancement local

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Lancer le serveur
```bash
uvicorn app.main:app --reload
```
Accès à la documentation automatique :
- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

### 3. Exemple de route
GET /produits

© Aper'wan – Projet artisanal de planches apéro locales 🍷🧀