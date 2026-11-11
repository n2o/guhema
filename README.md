# GUHEMA

Website of GUHEMA GmbH & Co. KG (metal-cutting saw blades, Remscheid). Static site built with [Astro](https://astro.build), hosted on Strato.

> **Migration in progress (branch `feat/astro`):** the Django site below is still live and is the reference for `tools/compare.py`. It is removed at the cutover to Strato.

## Astro site

```bash
npm ci
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
```

- **Languages:** German at `/…`, English at `/en/…`, Russian at `/ru/…` (one set of pages under `src/pages/[...lang]/`).
- **Product data:** `src/data/*.json` is the source of truth (exported once from Django with `tools/export_json.py`). Translated fields are `{ "de", "en", "ru" }`; missing languages fall back to German. Images live in `src/media/` (thumbnails are generated at build time), static files in `public/static/`.
- **Page texts:** UI strings are looked up by their German text with `t(lang, "…")`; translations in `src/i18n/{en,ru}.json`. Impressum/Datenschutz: `src/content/pages/*.md` (German only).
- **Product pages:** `src/components/groups/<slug>/{Overview,Details,Advices}.astro`, shared parts in `src/components/products/`.
- **Translations:** `python3 tools/translations.py export <lang> worklist.json` lists every text with its current translation; `… apply <lang> result.json` writes results back (and drops unused UI strings).
- **SEO:** canonical host `https://www.guhema.com` (keep `astro.config.mjs`, `public/.htaccess` and `public/robots.txt` in sync), hreflang, sitemap, structured data.
- **Deploy:** `.github/workflows/deploy.yml` builds and mirrors `dist/` via SFTP into `/guhema/` on Strato (secrets `SFTP_HOST`, `SFTP_USER`, `SFTP_PASSWORD`; the domain must point to that directory). Manual trigger until the cutover. Apache config: `public/.htaccess`.

---

## Django site (legacy, until cutover)

Django-based website for GUHEMA - a company specializing in industrial cutting tools and saw blades.

## Features

- **Product Catalog**: Browse various types of saw blades and cutting tools
  - Circular saw blades (Kreissägeblätter)
  - Band saw blades (Bandsägeblätter)
  - Jigsaw blades (Stichsägeblätter)
  - Hole saws (Lochsägen)
  - Hacksaw blades (Metallsägeblätter)
  - Sabre saw blades (Säbelsägeblätter)

- **News & Updates**: Latest company news and announcements
- **Fair Calendar**: Upcoming trade fairs and exhibitions
- **Downloads**: Product catalogs and documentation
- **Multi-language Support**: German/English/Russian translations via django-modeltranslation

## Tech Stack

- **Python**: 3.13+
- **Framework**: Django 5.2 LTS
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Database**: SQLite
- **Frontend**: Bootstrap 3.4.1, jQuery 3.7.1 (vendored in `templates/core/assets`)
- **Deployment**: Docker + Gunicorn behind nginx and Traefik

## Development Setup

### Prerequisites

- Python 3.13 or higher (uv installs it automatically)
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd guhema
```

2. Install dependencies with uv:
```bash
uv sync
```

3. Copy the CI secrets template (or create your own):
```bash
cp core/settings_secret_ci.py core/settings_secret.py
```

4. Run migrations and compile translations:
```bash
uv run python manage.py migrate
uv run python manage.py compilemessages --ignore .venv
```

5. Start the development server:
```bash
uv run python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Docker Deployment

### Build and run with Docker:

```bash
docker build -t guhema .
docker run -p 8000:8000 guhema
```

### Using Docker Compose:

```bash
docker compose up
```

The compose file expects `core/settings_secret.py`, `db.sqlite3`, `media/` and `static/` next to it.
The container runs `collectstatic` into `static/` and `migrate` on every start, so back up `db.sqlite3` before pulling a new image.

## Testing

Run the test suite:

```bash
uv run python manage.py test
uv run python manage.py makemigrations --check --dry-run
```

## Project Structure

```
guhema/
├── core/           # Core Django settings and middleware
├── products/       # Product catalog app
├── news/           # News and blog entries
├── fairs/          # Trade fair calendar
├── downloads/      # Downloadable resources
├── templates/      # HTML templates
├── static/         # Static files (CSS, JS, images)
├── media/          # User-uploaded files
└── locale/         # Translation files
```

## CI/CD

The project uses GitHub Actions for:
- **Testing**: System checks, missing-migration check and tests on pull requests and pushes to `main`
- **Docker**: Image builds on pull requests; pushes to `main` and `v*` tags are published to GitHub Container Registry

## License

See [LICENSE](LICENSE) file for details.
