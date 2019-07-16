#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Enum.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

class Enum(list):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

    def valueOf(self, name):
        if name in self:
            return name
        raise AttributeError

    def values(self):
        return self.values

    def ordinal(self, name):
        if name in self:
            return self.index(name)
        raise AttributeError

    def create(self, name):
        """
        创建自定义词性，如果已有该对应词性，则直接返回已有的词性
        :param name: 字符串词性
        :return: Enum词性
        """
        try:
            return self.valueOf(name)
        except Exception as e:
            return