#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: bobo
@contact: 1126531273@qq.com
@time: 2018-09-30 8:50
"""
from datetime import datetime

from consumer import celery_apps
# from producer import celery_app

if __name__ == "__main__":
    # celery_app1.send_task('producer.tasks.simple', args=(), eta=datetime.now())
    celery_apps.send_task('producer.tasks.hello_world', args=(1,), eta=datetime.now())
    # eta:定义任务的开始时间,以utc时间为准  所以这里不执行的原因是因为当前时间和utc的当前时间不一致（datetime.datetime.utcfromtimestamp(time_struct)）

# 还有一种情况，是我们希望将一个datetime对象转成时间戳，很遗憾的是python并没直接提供这个方法，但是提供了一个timetuple()方法，它返回一个time.struct_time对象，通过它我们可以构造出时间戳了
# >>> dd = datetime.today()
# >>> tt = time.mktime(dd.timetuple())
# >>> print int(tt)
# 1472816083