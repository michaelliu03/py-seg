#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from dictionary.TransformMatrixDictionary import TransformMatrixDictionary

class CoreDictionaryTransformMatrixDictionary(object):
    def __init__(self):
        self.transformMatrixDictionary = TransformMatrixDictionary()