#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version
import os
import sys
from dictionary.CoreBiGramTableDictionary import CoreBiGramTableDictionary
from utility.Predefine import Predefine
import math

class MathTools(object):
    """
    从一个词到另一个词的词的花费
    """

    @staticmethod
    def calculateWeight(fromnode, tonode):
        frequency = fromnode.getAttribute().totalFrequency
        if frequency == 0:
            frequency = 1

        nTwoWordsFreq = CoreBiGramTableDictionary.getBiFrequency(fromnode.wordID, tonode.wordID)
        value = -math.log((Predefine.dSmoothingPara * frequency / Predefine.MAX_FREQUENCY) + (1 - Predefine.dSmoothingPara) * ((1 - Predefine.dTemp) * nTwoWordsFreq / frequency + Predefine.dTemp))
        if value < 0:
            value = -value
        return value


if __name__ == "__main__":
    MathTools()