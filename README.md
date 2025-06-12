# Crypto Dashboard (MVP Mono-Utilisateur)

Application web personnelle de suivi des comptes crypto et wallet avec agrégation d'actifs et affichage via un dashboard moderne.

---

## 🚦 Statut du projet

> **Phase actuelle** : MVP, backend complet, frontend minimaliste (HTML+JS natif, sans SPA).
> La SPA Vue 3 sera ajoutée à l’étape 7 de la roadmap.

---

## 🔧 Stack technique

* **Backend** : FastAPI
* **DB** : PostgreSQL
* **ORM** : SQLAlchemy
* **Auth** : JWT
* **API externes à venir** : Binance, Etherscan, CoinGecko, etc
* **Frontend actuel** : HTML minimaliste (SPA Vue 3 à venir)

---

## ▶️ Lancer le projet

Copier `.env.example` vers `.env` et renseigner la variable `JWT_SECRET` pour
signer les tokens JWT.

```bash
docker compose up --build
```

* Le backend FastAPI écoute sur le port 8000
* Le frontend statique (Nginx) écoute sur le port 3000

---

## 💻 Tester l’application (MVP)

### 1. **Obtenir un token**

* Utiliser l’API `/auth/login` (POST) avec le couple user/pass initial (`admin`/`admin123` par défaut, ou selon `.env`)
* Récupérer le token JWT

### 2. **Accéder au dashboard**

* Aller sur [http://localhost:3000](http://localhost:3000)
* Entrer le token JWT dans la fenêtre de prompt
* Le dashboard affiche les données dummy de `/dashboard/` (backend)

---

## 🗺️ Roadmap (résumé)

Voir [ROADMAP.md](ROADMAP.md) pour le détail.

* 1. Initialisation projet ✅
* 2. Authentification JWT ✅
* 3. Modèles utilisateur & comptes ✅
* 4. Dashboard dummy & front minimaliste ✅
* 5. Fetch engine réel (API externes) 🔜
* 6. Historique des refreshs 🔜
* 7. **SPA Vue 3 + UI avancée** 🔜

---

## 📁 Structure

* **backend/** : API REST, gestion des comptes, dashboard dummy, etc.
* **frontend/** : (pour l’instant) HTML minimaliste avec JS natif

---

## 🤝 Organisation

* Avancement par branches dédiées, PR, validation par étape.
* Changement d’architecture ou de stack frontend uniquement à l’étape 7.