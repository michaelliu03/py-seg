#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from abc import ABCMeta,abstractmethod
from collection.enum.Enum import Enum

class BaseNode(object,metaclass=ABCMeta):


    Status = Enum([
        # 未指定，用于删除词条
        'UNDEFINED_0',
        # 不是词语的结尾
        'NOT_WORD_1',
        # 是个词语的结尾，并且还可以继续
        'WORD_MIDDLE_2',
        # 是个词语的结尾，并且没有继续
        'WORD_END_3'
    ])

    def __init__(self):
        self.child = []
        self.c =''
        self.value = None

    # 这个类是一个抽象的类
    @abstractmethod
    def getChild(self,c):
        pass


    def getValue(self):
        return self.value

    def transition(self,path,begin):
        cur = self
        for i in range(begin,len(path)):
            cur = cur.getChild(path[i])
            if cur  is None or cur.status == BaseNode.Status.UNDEFINED_0:
                return None
        return cur
