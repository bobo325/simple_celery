# simple_celery
这是关于一个celery的一个demo，通过send_task的方式进行远端任务发送并执行。
#注意
-在编写测试过程中，发现任务只会Received task：，但是并没有执行任务体，经测试比较发现，是由于eta的时间虽然为now，但是并没有转化为utc时间点的当前时间，
导致时刻未到达，故任务尚未执行。
