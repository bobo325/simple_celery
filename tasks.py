# coding:utf-8

from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost:5672//')


@app.task
def add(x, y):
    return x + y

# celery -A tasks worker --loglevel=info
# 现在我们已经开启了一个Worker了，这样我们可以在应用程序中使用 delay()或者 apply_async()方法来调用任务。
# # 在tasks.py文件所在的目录打开终端。
# >>> from tasks import add
# >>> add.delay(2, 8)
# <AsyncResult: 1b50f449-8fa2-478a-9eea-561a3c29fd43>
