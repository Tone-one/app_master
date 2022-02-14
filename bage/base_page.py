#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 18:12
# @Author  : A one
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utils.black_handle import black_wrapper


class BasePage:

    # 定义一个私有变量
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

        #   黑名单列表
        self.black_list = [
            (By.ID, "com.android.permissioncontroller:id/permission_allow_button"),
        ]

    #   日志打印
    def log_info(self, message):
        logging.info(message)

    def iv_back(self):
        #   返回功能
        pass

    @black_wrapper
    def find(self, by, value):
        #   查找元素
        return self._driver.find_element(by, value)

    def finds(self, by, value):
        #   查找元素元祖
        return self._driver.find_elements(by, value)

    def find_click(self, by, value):
        self.log_info(f'find and click:{value}')
        return self.find(by, value).click()

    def find_input(self, by, value):
        self.log_info(f'find and input {value}')

    def swipe_find(self, text, num=5):
        self.log_info('swipe find :')
        self.log_info(text)
        self.log_info(num)
        for i in range(num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print("没有找到，滑一下")
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get('width')
                height = size.get('height')
                # 起点坐标
                start_x = width / 2
                start_y = height * 0.8

                # 终点坐标
                end_x = start_x
                end_y = height * 0.4
                # 滑动时长
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到")

    def tap_click(self,tap_time):
        """
        # 可模拟手指点击（最多五个手指），可设置按住时间长度（毫秒） :
        tap(self, positions, duration=None)

        参数Args:
        positions ： list（列表）类型，里面对象是元组，最多五个。
        如：[(100, 20), (100, 60)]，
        元组中一个元素表示一个坐标， 元组中最多可有5个坐标。
        duration ： 持续时间，单位毫秒，如：500

        # 调用方式
        driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        :return:
        """
        logging.info("点击空白区域收起弹窗")
        size = self.driver.get_window_size()
        # 获取高宽
        width = size.get('width')
        height = size.get('height')

        # 点击坐标
        start_x = width / 2
        start_y = height / 3
        self.driver.tap([(start_x,start_y)],tap_time)

    #   向上滑动
    def swipeUp(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5     # x坐标
        y1 = l['height'] * 0.75   # 起始y坐标
        y2 = l['height'] * 0.25   # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    #   向下滑动
    def swipeDown(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5          # x坐标
        y1 = l['height'] * 0.25        # 起始y坐标
        y2 = l['height'] * 0.75         # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2,t)

    #   向左滑动
    def swipLeft(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    #   向右滑动
    def swipRight(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    #   捕获对应元素，如果捕获到则触发点击
    def find_checkable(self, id, type):

        """
        获取元素状态：返回treu或false
        get_attribute('clickable')  是否可点击
        get_attribute('checked')   是否可选中
        get_attribute('displayed')  是否可见
        get_attribute('enabled')   是否可用

        :param
        id=元素id，type为元素状态
        """
        if self.driver.find_element_by_id(f"{id}").get_attribute(f"{type}"):
            self.find_click(By.ID,f"//*[resource-id='{id}'")
        else:
            print("元素捕获失败")

