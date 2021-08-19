import gc
from pathlib import Path

import pandas as pd
import psycopg2
from celery import Celery
from sqlalchemy import create_engine

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(filepath: str):
    print(f'processing file: {filepath}')
    try:
        df = pd.read_csv(filepath)
        db_uri = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
        print(f'create engine for db')
        engine = create_engine(db_uri, echo=True)
        print(f'filepath: {filepath}')
        p = Path(filepath)
        print(f'filename: {p.stem}')

        df.to_sql(p.stem[:50],
                  engine,
                  if_exists='replace',
                  index=False,
                  chunksize=500)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        gc.collect()
    return
