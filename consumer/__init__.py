#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""
from celery import Celery, platforms

celery_apps = Celery('chtnew_api_task')
celery_apps.config_from_object('consumer.celeryconfig_c')
platforms.C_FORCE_ROOT = True

