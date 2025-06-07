# 🗺️ Roadmap de développement — Crypto Dashboard

Ce document trace l’ensemble des étapes prévues pour développer l’application selon une démarche modulaire, progressive et rigoureuse.

---

## 📌 Statut : Phase 2 validée ✅

---

## 📆 Étapes à suivre

| Étape | Nom du module                         | Objectifs |
|-------|---------------------------------------|-----------|
| 1️⃣   | **Initialisation projet**             | Setup GitHub, Docker, FastAPI, Vue |
| 2️⃣   | **Système d’authentification**        | Login sécurisé (JWT), middleware |
| 3️⃣   | **Modèle utilisateur & compte**       | DB, endpoints, UI ajout/suppression |
| 4️⃣   | **Dashboard & fetcher dummy**         | UI + récupération manuelle simulée |
| 5️⃣   | **Fetch engine réel**                 | API Binance, Etherscan, CoinGecko |
| 6️⃣   | **Historique des refreshs**           | Table `refresh_logs`, affichage |
| 7️⃣   | **UI avancée (graphes, préférences)** | Composants graphiques, filtres |
| 8️⃣   | **Tâches périodiques & scheduler**    | APScheduler, cron, test régularité |
| 9️⃣   | **CI/CD + tests**                     | GitHub Actions, tests Pytest |
| 🔟    | **Préparation à l’extension**         | Base multi-user, sécurité, doc API |

---

## ✅ Suivi des phases

- [x] Phase 1 : initialisation dépôt, structure projet
- [x] Phase 2 : backend FastAPI opérationnel + frontend statique
- [ ] Phase 3 : Authentification mono-utilisateur (à venir)
- [ ] Phase 4 : ...
