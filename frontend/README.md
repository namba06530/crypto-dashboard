# Frontend build

- Vue 3 app built with Vite and TailwindCSS.
- `docker compose up --build` builds the JS with `npm run build` inside Docker.
- The compiled files in `dist/` are copied into an Nginx image.
- Nginx serves `index.html` and uses a SPA fallback (`try_files`).
- Run `docker compose up` and visit `http://localhost:3000`.
