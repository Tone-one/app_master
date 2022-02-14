#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 11:19
# @Author  : A one

import pytest
import time


# 日志生成
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'mylog/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)






