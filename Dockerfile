FROM python:3.13-alpine

COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

# gettext for compilemessages
RUN apk add --no-cache gettext

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    PYTHONUNBUFFERED=1 \
    PATH="/code/.venv/bin:$PATH"

WORKDIR /code

# Install dependencies first for layer caching
COPY uv.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

COPY locale ./locale
RUN django-admin compilemessages --ignore .venv

COPY . .

EXPOSE 8000

CMD ["sh", "docker_init.sh"]
