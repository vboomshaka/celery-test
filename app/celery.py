# -*- coding=utf-8 -*-
from __future__ import absolute_import
from celery import Celery

# 创建一个celery的实例，名字叫做app
# 传递进去的第一个参数是Python包的名字，include加载任务文件，config_from_object指定celery的配置文件
app = Celery('app', include=['app.tasks'], timezone='Asia/Shanghai')
app.config_from_object('app.config')

# include : 每个worker应该导入的模块列表，以实例创建的模块的目录作为起始路径

# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )

# https://blog.csdn.net/PY0312/article/details/105906078
