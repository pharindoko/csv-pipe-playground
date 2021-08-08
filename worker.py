import gc
import json
import time
from pathlib import Path

import pandas as pd
import psycopg2
from celery import Celery
from sqlalchemy import create_engine

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(filepath: str):
    print(f'processing file: {filepath}')
    conn = None
    try:
        df = pd.read_csv(filepath)
        db_uri = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
        print(f'create engine for db')
        engine = create_engine(db_uri, echo=True)
        print(f'filepath: {filepath}')
        p = Path(filepath)
        print(f'filename: {p.stem}')

        df.to_sql(
            p.stem[:50],
            engine,
            if_exists='replace',
            index=False,
            chunksize=500
        )
       # jsontest = df.to_json()
       # print(f'jsonstring: {jsontest[:100]}')

       # conn = psycopg2.connect(host='localhost',
       #                         user='postgres',
       #                         password='postgres',
       #                         database='postgres')  # To remove slash
       # print(f'connect: {str(conn)}')
       # cursor = conn.cursor()
       # cursor.execute(
       #     f"INSERT INTO public.event (eventdata) VALUES(%s)", (jsontest,))
       # conn.commit()
       # print(f'inserted record')
       # cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # if conn:
        #     conn.close()
        #     print('db connection closed')
        gc.collect()
    return
