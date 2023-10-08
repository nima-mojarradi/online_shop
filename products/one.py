from celery import Celery
import time

app = Celery('first', broker='amqp://guest:guest@localhost:15672')

@app.task
def adding(a, b):
    time.sleep(20)
    return a + b