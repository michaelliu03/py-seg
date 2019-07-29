#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version
from NlpAnalysis import NlpAnalysis

if __name__ == '__main__':
    testCase = [
        # "王总和小丽结婚了",
        # "柯文哲纠正司仪“恭请市长”说法：别用封建语言",
        # "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。",
        # "王国强、高峰先生和汪洋女士、张朝阳光着头、韩寒、小四",
        # "张浩和胡健康复员回家了",
        # "编剧邵钧林和稽道青说",
        # "这里有关天培的有关事迹",
        # "龚学平等领导,邓颖超生前",
        # "微软的比尔盖茨、Facebook的扎克伯格跟桑德博格"
        "节能灯采购"
    ]
    segment = NlpAnalysis.newSegment().enableNameRecognize(False)
    print ("===================")
    for sentence in testCase:
        termList = segment.seg(sentence)
        item = []
        for i in termList:
            item.append(i.word + "/" + i.nature)
        print (",".join(item))