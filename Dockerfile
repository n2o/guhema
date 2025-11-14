FROM python:3.11-alpine

RUN apk add --no-cache build-base python3-dev py-pip jpeg-dev zlib zlib-dev musl-dev libffi-dev freetype-dev gettext \
    lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev && \
    pip install -U pip

ENV CFLAGS="$CFLAGS -L/lib"

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "docker_init.sh"]