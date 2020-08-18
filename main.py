#coding :utf-8

from app.tasks import add, task_port_scan
import time


result = add.delay(1, 2)
print(result)

# result = task_port_scan.delay('39.96.212.188')
# print(result)