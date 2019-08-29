#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Predefine.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

import  logging
import os
import sys

class Predefine:
    #ROOT  = os.getcwd() + "/data"
    ROOT = "/Users/michael/Desktop/nlpproject/py_seg" + "/data"

    # 人名nr
    TAG_PEOPLE = "未##人"
    # 地址 ns
    TAG_PLACE = "未##地"
    # 专有名词 nx
    TAG_PROPER = "未##专"
    # 团体名词 nt
    TAG_GROUP = "未##团"
    # 时间 t
    TAG_TIME = "未##时"
    # 字符串 x
    TAG_CLUSTER = "未##串"
    # 数词 m
    TAG_NUMBER = "未##数"
    # 句子的开始 begin
    TAG_BIGIN = "始##始"
    # 结束 end
    TAG_END = "末##末"
    # 其它
    TAG_OTHER = "未##它"

    MAX_FREQUENCY=25146057
    dTemp = float(1/MAX_FREQUENCY +0.00001)
    dSmoothingPara = 0.1

    logger = logging.getLogger('NlpSegment')
    logger.addHandler(logging.StreamHandler())

    BIN_EXT = '.bin'
    PIC_EXT = '.cPickle'
    TRIE_EXT = '.trie.dat'
    VALUE_EXT = '.value.dat'

    MAX_VALUE = 1.7976931348623157e+308

    CT_SINGLE = 5
    CT_DELIMITER = CT_SINGLE + 1
    CT_CHINESE = CT_SINGLE + 2
    CT_LETTER = CT_SINGLE + 3
    CT_NUM = CT_SINGLE + 4
    CT_INDEX = CT_SINGLE + 5
    CT_OTHER = CT_SINGLE + 12

    def __init__(self):
        pass
