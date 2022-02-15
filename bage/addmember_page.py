#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 18:37
# @Author  : A one
from selenium.webdriver.common.by import By

from bage.base_page import BasePage


class AddMember(BasePage):

    # 添加成员
    def add_member(self, name, alias, acctid, iphone):
        """
        1.点击手动输入添加
        2.输入姓名、别名、账号、手机号
        3.上划寻找“保存并继续添加”按钮

        :param name:
        :param alias:
        :param acctid:
        :param iphone:
        :return:
        """
        self.find_click(By.XPATH, '//*[@resource-id="com.tencent.wework:id/dp3"]')

        self.find_input(By.XPATH,)