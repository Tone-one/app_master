#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 18:36
# @Author  : A one
from bage.addmember_page import AddMember
from bage.base_page import BasePage


class Main(BasePage):

    #   切换消息页面
    def goto_message(self):
        pass

    #   切换日程界面
    def goto_schedule(self):
        pass

    #   切换文档界面
    def goto_document(self):
        pass

    #   切换通讯录界面
    def goto_contacts(self):

        #   点击通讯录
        

        # 进入添加成员界面
        return AddMember(self._driver)

