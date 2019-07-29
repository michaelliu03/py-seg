#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext

def read_file(filename):
    """读取文件数据"""
    contents, labels = [], []
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            try:
                content,label = line.strip().split('\t')
                #print(content , label)
                if content:
                    contents.append(content)
                    labels.append(label)
            except:
                pass
    return contents, labels


classifier =fasttext.load_model('model_file.bin')
lines, test_cls = read_file("1_test.txt")
pred = classifier.predict(lines)
print(pred)
