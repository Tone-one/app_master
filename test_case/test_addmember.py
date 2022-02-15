#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 10:16
# @Author  : A one
import logging

import allure
import pytest

from bage.communication_page import CommunicationPage


@allure.title("添加成功功能")
class TestAddMember:

    @allure.story("添加成员")
    def test_add_member(self):
        """
        1.跳转添加成员界面
        2.添加成员界面添加成员
        3.保存成员，返回通讯界面
        4.断言保存成功

        :return:
        """
        # 实例化
        add = CommunicationPage()
        # 跳转成员界面
        list_iphone = add.goto_add_member_interface().\
            add_member(name="可", alias="克", acctid="5555", iphone="13510582428").get_member()
        logging.info(list_iphone)
        assert '13510582428' in list_iphone


if __name__ == '__main__':

    pytest.main("-sq")

"""
pytest -s --alluredir=./result
allure generate ./result -o ./report
"""