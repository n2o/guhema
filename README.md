# GUHEMA

Website of GUHEMA GmbH & Co. KG (metal-cutting saw blades, Remscheid): https://guhema.com. Static site built with [Astro](https://astro.build), hosted on Strato.

```bash
npm ci
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
```

- **Languages:** German at `/…`, English at `/en/…`, Russian at `/ru/…` (one set of pages under `src/pages/[...lang]/`).
- **Product data:** `src/data/*.json` is the source of truth. Translated fields are `{ "de", "en", "ru" }`; missing languages fall back to German. Images live in `src/media/` (thumbnails are generated at build time), static files in `public/static/`.
- **Page texts:** UI strings are looked up by their German text with `t(lang, "…")`; translations in `src/i18n/{en,ru}.json`. Impressum/Datenschutz: `src/content/pages/<page>.md` (German, legally binding) and `<page>.<lang>.md`.
- **Product pages:** `src/components/groups/<slug>/{Overview,Details,Advices}.astro`, shared parts in `src/components/products/`.
- **Translations:** `python3 tools/translations.py export <lang> worklist.json` lists every text with its current translation; `… apply <lang> result.json` writes results back (and drops unused UI strings).
- **SEO:** canonical host is `SITE` in `astro.config.mjs` (repeat it in the host redirect in `public/.htaccess`), hreflang, sitemap, robots.txt, structured data.
- **Deploy:** every push to `main` runs `.github/workflows/deploy.yml`: build, then mirror `dist/` via SFTP into `/guhema/` on Strato (secrets `SFTP_HOST`, `SFTP_USER`, `SFTP_PASSWORD`). HTTPS is forced in the Strato panel, other hosts redirect to `SITE` via `public/.htaccess`.

The former Django site is in the git history.
