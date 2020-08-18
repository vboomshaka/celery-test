# -*- coding:utf-8 -*-

from __future__ import absolute_import


BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'


# 常用配置
# CELERY_IMPORTS = ("tasks", "graph_data_tasks")
# BROKER_URL = ''
# CELERY_RESULT_BACKEND = ''
# CELERY_TASK_SERIALIZER = 'msgpack'
# CELERY_RESULT_SERIALIZER = 'json'
# # A value of None or 0 means results will never expire
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务结果过期时间
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
# # celery worker的并发数
# CELERYD_CONCURRENCY = 2

# # 使用任务调度，使用Beat进程自动生成任务
# CELERYBEAT_SCHEDULE = {
#     'graph_data': {
#         'task': 'graph_data_tasks.sync_graph',
#         'schedule': timedelta(minutes=60),
#         'args': ()
#     },
#         'rank_for_guchong': {
#         'task': 'backend.celerytasks.rank_for_guchong.calc_ability_schedule',
#         'schedule': crontab(hour=11, minute=55),
#         'args': ()
#     }
# }

# CELERY_ACKS_LATE = True
# CELERYD_PREFETCH_MULTIPLIER = 1
