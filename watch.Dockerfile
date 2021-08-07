FROM python:3.8
RUN pip install pipenv
COPY ./ /app/
RUN cd app && pipenv install

WORKDIR /app

ENTRYPOINT pipenv run python watch.py