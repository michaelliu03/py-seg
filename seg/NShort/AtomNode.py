#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

class AtomNode(object):
    def __init__(self):
        self.sWord = ''
        self.nPOS = int()

    def init1(self, sWord, nPOS):
        self.sWord = sWord
        self.nPOS = nPOS
        return self