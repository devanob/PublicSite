from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend ='pyamqp://')

@app.task
def add(x, y):
    print(x)
    print(y)
    return x + y