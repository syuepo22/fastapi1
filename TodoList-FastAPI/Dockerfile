
FROM python:3.8.1-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        mariadb-dev mysql-client netcat-openbsd\
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /code/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /code
RUN chmod +x ./scripts/wait-for-db.sh
EXPOSE 8080

