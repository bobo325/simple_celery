#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""

from celery import Celery, platforms

celery_app = Celery("chtnew_api_task")
celery_app.config_from_object("producer.celeryconfig")
platforms.C_FORCE_ROOT = True
celery_app.task()
# 启动celery：
# celery -A producer worker -l info
# or
# celery -A producer worker -loglevel=info
# 4版本的celery在windows上无法正常运行
# celery -A producer purge  # 清空所有相关模块的队列任务
