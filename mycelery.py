import time
from celery import Celery
from celery import task
my_task =  Celery("tasks", broker="redis://127.0.0.1:6379", backend="redis://127.0.0.1:6379")

@task
def fun(a):
    time.sleep(2)
    print("fun")

