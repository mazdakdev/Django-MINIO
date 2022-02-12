FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN apk update

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

