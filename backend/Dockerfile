FROM tiangolo/uwsgi-nginx-flask:flask
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000