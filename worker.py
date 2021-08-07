from celery import Celery
import pandas as pd
import time
import gc
app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(filepath: str):
    print(f'processing file: {filepath}')
    try:
        df = pd.read_csv(filepath)
        jsontest = df.to_json()
        print(f'jsonstring: {jsontest}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        gc.collect()
    return
