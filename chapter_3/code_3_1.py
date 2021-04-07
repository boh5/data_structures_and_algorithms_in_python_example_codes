#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/7
@Author  : dilless
@Site    : 
@File    : code_3_1
@Software: PyCharm
"""


def find_max(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val

    return biggest
