FROM python:3.8

WORKDIR /usr/src/app

RUN pip install pipenv==v2021.5.29 --no-cache-dir
COPY Pipfile* ./
RUN pipenv install --dev --system --deploy

COPY . .
EXPOSE 80
