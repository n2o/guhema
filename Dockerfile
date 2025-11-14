FROM python:3.11-alpine

RUN apk add --no-cache build-base python3-dev py-pip jpeg-dev zlib zlib-dev musl-dev libffi-dev freetype-dev gettext && \
    pip install -U pip poetry

ENV CFLAGS="$CFLAGS -L/lib"

WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi --no-root

COPY . .

EXPOSE 8000

CMD ["sh", "docker_init.sh"]