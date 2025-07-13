# 🗺️ Roadmap de développement — Crypto Dashboard (Mise à jour)

Ce document trace l’ensemble des étapes prévues pour développer l’application selon une démarche modulaire, progressive et rigoureuse.

---

## 📌 **Statut actuel**

Phase 5 validée (Fetch engine réel) ✅

---

## 📆 **Étapes à suivre**

| Étape | Nom du module                         | Objectifs                                                                                   |
| ----- | ------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1️⃣   | **Initialisation projet**             | Setup GitHub, Docker, FastAPI, Vue                                                          |
| 2️⃣   | **Système d’authentification**        | Login sécurisé (JWT), middleware                                                            |
| 3️⃣   | **Modèle utilisateur & compte**       | DB, endpoints, UI ajout/suppression                                                         |
| 4️⃣   | **Dashboard & fetcher dummy**         | Route backend `/dashboard` (dummy), front minimaliste sans framework, affichage JSON simulé |
| 5️⃣   | **Fetch engine réel**                 | API Binance, Etherscan, CoinGecko                                                           |
| 6️⃣   | **Historique des refreshs**           | Table `refresh_logs`, affichage                                                             |
| 7️⃣   | **UI avancée (graphes, préférences)** | SPA Vue complète, composants graphiques, filtres                                            |
| 8️⃣   | **Tâches périodiques & scheduler**    | APScheduler, cron, test régularité                                                          |
| 9️⃣   | **CI/CD + tests**                     | GitHub Actions, tests Pytest                                                                |
| 🔟    | **Préparation à l’extension**         | Base multi-user, sécurité, doc API                                                          |

---

## ✅ **Suivi des phases**

* [x] **Phase 1 :** Initialisation dépôt, structure projet
* [x] **Phase 2 :** Backend FastAPI opérationnel + frontend statique
* [x] **Phase 3 :** Authentification mono-utilisateur (JWT)
* [x] **Phase 4 :** Dashboard dummy (backend route, front minimal, affichage JSON)
* [x] **Phase 5 :** Fetch engine réel
* [ ] **Phase 6 :** Historique des refreshs
* [ ] **Phase 7 :** UI avancée (SPA Vue, graphiques)
* [ ] **Phase 8 :** Tâches périodiques & scheduler
* [ ] **Phase 9 :** CI/CD + tests
* [ ] **Phase 10 :** Préparation à l’extension (multi-user, doc API)

---

**Remarque importante sur la phase 4 :**

> La partie frontend reste pour l’instant **minimaliste** (HTML+JS natif, sans framework).
> L’implémentation d’une vraie SPA Vue3 sera réalisée lors de la **phase 7** (UI avancée, graphiques…).