#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from collection.treemap.TreeMap import TreeMap
from utility.Predefine import Predefine

class CustomNatureUtility(object):
    Predefine.logger.warning("已激活自定义词性功能,用户需对本地环境的兼容性和稳定性负责!\n")
    extraValueMap = TreeMap({})
    enumBuster = EnumBuster()

    def __init__(self):
        pass

    def addNature(self, name):
        """
        增加词性
        @param name 词性名称
        :return: 词性
        """
        customNature = self.extraValueMap.get(name)
        if customNature != None:
            return customNature
        return customNature