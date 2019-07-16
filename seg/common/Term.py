#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from seg.config import Config
from utility.LexiconUtility import LexiconUtility

class Term(object):

    def __init__(self,word,nature):
        self.word = word
        self.nature = nature
        self.offset = int()

    def toString(self):
        if Config().ShowTermNature:
            return str(self.word) + '/' + str(self.nature)
        return self.word

    def length(self):
        """
        长度
        :@return
        """
        word = self.word.decode('utf-8')
        return len(word)

    def getFrequency(self):
        return LexiconUtility.getFrequency(self.word)