FROM python:3.9.16-slim-buster

EXPOSE 9797

RUN pip install pipenv

WORKDIR /code

COPY . /code/

RUN pipenv install --dev --system --deploy

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]