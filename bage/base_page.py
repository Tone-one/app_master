#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 18:12
# @Author  : A one

from appium.webdriver.webdriver import WebDriver


class BasePage:

    # 定义一个私有变量
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
