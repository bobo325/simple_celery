#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""

rabbitmq_config = {
    "rabbit_mq_url": 'amqp://guest:guest@localhost:5672//',
    "celery_broker_url": "amqp://guest:guest@localhost:5672//"  # amqp
    # "celery_broker_url" = pgsql_pool_configs['url'].replace("postgresql+psycopg2", "db+postgresql")
}
# RabbitMQ服务所需的相关端口号
# 5672, 5671 (AMQP 0-9-1 without and with TLS)
# 15672 (if management plugin is enabled)
