#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 14:57
# @Author  : A one

# 黑名单列表

def black_wrapper(fun):

    def run(*args,**kwargs):
        basepage = args[0]
        try:
            return fun(*args,**kwargs)
        #   捕获元素未找到
        except Exception as e:

            #   遍历黑名单列表
            for black in basepage.black_list:
                eles = basepage.finds(*black)

                #   元素在黑名单中找到，后续操作可扩展
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
        raise e
        return run