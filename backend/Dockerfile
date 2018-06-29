FROM tiangolo/uwsgi-nginx-flask:python2.7

LABEL maintainer "tiago@reichert.eti.br"

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000