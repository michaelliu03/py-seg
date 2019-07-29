#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:NlpAnalysis.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

import sys
from Config import Config
from seg.viterbi.ViterbiSegment import ViterbiSegment



class NlpAnalysis(object):
    # 开启调试模式（会降低性能）
    def enableDebug(self, enable):
        Config.DEBUG = enable

    @staticmethod
    def newSegment():
        """
        创建一个分词器
        与创建一个分词对象相比，该方法便于版本升级后，保证使用最合适的分词器
        """
        return ViterbiSegment()

