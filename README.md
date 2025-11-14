# GUHEMA

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
- **Multi-language Support**: German/English translations via django-modeltranslation

## Tech Stack

- **Python**: 3.11+
- **Framework**: Django 4.1.5
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Database**: SQLite (development)
- **PDF Generation**: ReportLab
- **Deployment**: Docker + Gunicorn

## Development Setup

### Prerequisites

- Python 3.11 or higher
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

4. Run migrations:
```bash
uv run python manage.py migrate
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
docker-compose up
```

## Testing

Run the test suite:

```bash
uv run python manage.py test
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
- **Testing**: Automated tests on pull requests
- **Docker**: Automatic Docker image builds and publishing to GitHub Container Registry

## License

See [LICENSE](LICENSE) file for details.

## Migration Notes

This project was recently migrated from Poetry to uv for improved performance and reliability. If you encounter any issues, please check the latest commit history or open an issue.
