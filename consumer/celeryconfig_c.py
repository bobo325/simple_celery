#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""
from config import rabbitmq_config

broker_url = rabbitmq_config['rabbit_mq_url']

enable_utc = True

timezone = 'UTC'

task_serializer = 'json'

result_serializer = 'json'

accept_content = ['json']
