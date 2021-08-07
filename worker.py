import gc
import json
import time

import pandas as pd
import psycopg2
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(filepath: str):
    print(f'processing file: {filepath}')
    try:
        df = pd.read_csv(filepath)
        jsontest = df.to_json()
        print(f'jsonstring: {jsontest[:100]}')

        conn = psycopg2.connect(host='localhost',
                                user='postgres',
                                password='postgres',
                                database='postgres')  # To remove slash
        print(f'connect: {str(conn)}')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO public.event (eventdata) VALUES(%s)", (jsontest,))
        conn.commit()
        print(f'inserted record')
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        gc.collect()
    return
