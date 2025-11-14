FROM python:3.11-alpine

# Install system dependencies and uv
RUN apk add --no-cache \
    build-base \
    python3-dev \
    py-pip \
    jpeg-dev \
    zlib \
    zlib-dev \
    musl-dev \
    libffi-dev \
    freetype-dev \
    gettext \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

ENV CFLAGS="$CFLAGS -L/lib"
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /code

# Copy dependency files for layer caching
COPY uv.lock pyproject.toml ./

# Install dependencies in a virtual environment
RUN uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY . .

# Install the project itself
RUN uv sync --frozen --no-dev

EXPOSE 8000

CMD ["sh", "docker_init.sh"]