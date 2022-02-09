#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 16:01
# @Author  : A one

# 创建包类
from bage.base_page import BasePage
from appium import webdriver


class App(BasePage):

    _package = "com.tencent.wework"
    _activity = "com.github.moduth.blockcanary.ui.DisplayActivity"

    def start(self):
        if self._driver is None:
            engine = {
                'platformName': "android",
                'deviceName': "127.0.0.1:21503",
                'appPackage': self._package,
                'appActivity': self._activity,
                'noReset': True     # 不重置app
                      }
            self._driver = webdriver.Remote("http：//localhost:4723/wd/hub", engine)
            self._driver.wait_activity(15)  # 隐式等待
        else:
            self._driver.start_activity(self._package, self._activity)

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:

        return Main(self._driver)
