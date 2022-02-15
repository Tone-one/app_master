#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/15 11:19
# @Author  : A one
from selenium.webdriver.common.by import By

from bage.addmember_page import AddMember
from bage.base_page import BasePage


class CommunicationPage(BasePage):
    #   新增成员
    def goto_add_member_interface(self):
        #   点击添加成员
        self.find_click(By.XPATH, '//*[resource-id="com.tencent.wework:id/f0m"]')
        return AddMember(self)

    #   管理团队
    def goto_management_team_interface(self):
        pass

    #   个人中心
    def goto_personal_center(self):
        pass

