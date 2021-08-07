FROM python:3.8
RUN pip install pipenv
# copy contents of project into docker
COPY ./ /app/
RUN cd app && pipenv install

WORKDIR /app

ENTRYPOINT pipenv run celery -A worker worker --loglevel=INFO