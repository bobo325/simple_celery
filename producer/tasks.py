#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""
import logging

from producer import celery_app as app


class Tasks(app.Task):
    # exc:失败的错误的类型
    # task_id: 任务的id
    # args: 任务函数的参数
    # kwargs:参数
    # einfo:任务失败后的详细异常信息
    # retval: 任务成功执行的返回值

    # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logging.error('task exec fail, task_id:%s,\n, args:%s, error:' % (task_id, args),
                      exc_info=1)  # error:后刚好接打印的报错
#    # 任务成功时执行
#     def on_retry(self, exc, task_id, args, kwargs, einfo):
#         pass

# 任务重试时执行
# def on_success(self, retval, task_id, args, kwargs):
#     print(retval)
#     print("Task successfully invoke!")


@app.task(base=Tasks, bind=True)
def simple():
    logging.info("simple_producer works")
    print("nice to meet you!")


@app.task(base=Tasks, bind=True)
def hello_world(self, order_no):

    print('nice to meet you!')
