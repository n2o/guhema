FROM python:3.11-alpine

RUN apk add --no-cache build-base python3-dev py-pip jpeg-dev zlib zlib-dev musl-dev libffi-dev freetype-dev gettext \
    lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev && \
    pip install -U pip && \
    pip install cffi && \
    pip install poetry==1.3.2

ENV CFLAGS="$CFLAGS -L/lib"

WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi --no-root

COPY . .

EXPOSE 8000

CMD ["sh", "docker_init.sh"]