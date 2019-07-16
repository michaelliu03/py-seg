#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from collection.treemap.TreeMap import TreeMap

class EnumBuster(object):
    """
    运行时动态增加词性工具
    """

    def __init__(self):
        self.extraValueMap = TreeMap({})