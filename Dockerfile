FROM tiangolo/meinheld-gunicorn-flask:python3.8

RUN apt update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app