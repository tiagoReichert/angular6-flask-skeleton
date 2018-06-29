FROM tiangolo/uwsgi-nginx-flask:python2.7-alpine3.7

LABEL maintainer "tiago@reichert.eti.br"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN apk update
RUN apk add postgresql-dev gcc musl-dev
RUN pip install -r requirements.txt

COPY . /app

RUN apk del gcc musl-dev && rm -rf /var/cache/apk/*

EXPOSE 5000