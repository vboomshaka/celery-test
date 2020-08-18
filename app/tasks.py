# -*- coding:utf-8 -*-
from __future__ import absolute_import
from app.celery import app

from plugins import port_scan


@app.task
def add(x, y):

    return x + y


@app.task(time_limit=200)
def task_port_scan(target):
    options = '-sV –host-timeout 200'
    ports = '22, 80'
    # 全端口扫描
    # return port_scan.run(target, options)
    return port_scan.port_scan(target, options, ports)
