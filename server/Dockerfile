FROM python:3.11-slim

RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client
WORKDIR /server

COPY ./poetry.lock /server/
COPY ./pyproject.toml /server/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /server/

RUN SECRET_KEY=build python ./manage.py collectstatic --noinput