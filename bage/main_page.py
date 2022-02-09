#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 18:36
# @Author  : A one
from bage.addmember_page import AddMember
from bage.base_page import BasePage


class Main(BasePage):

    #   进入消息页面
    def goto_message(self):
        pass

    #   进入日程界面
    def goto_schedule(self):
        pass

    #   进入文档界面
    def goto_document(self):
        self.find()

    #   进入团队界面
    def goto_team(self):

        # 进入添加成员界面
        return AddMember(self._driver)