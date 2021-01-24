FROM python:3.4-alpine

RUN apk add --no-cache build-base python3-dev py-pip jpeg-dev zlib zlib-dev musl-dev && \
    pip install -U pip

ENV CFLAGS="$CFLAGS -L/lib"

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "docker_init.sh"]