#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from mining.jb_title_seg_util import *
import fasttext

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fasttext

#训练模型
#model = fasttext.supervised("1.txt", model='cbow', lr=0.05, dim=100, ws=5, epoch=5)
model = fasttext.train_supervised("1.txt", lr=0.1,dim=100,epoch=5,word_ngrams=2,loss= 'softmax')#fasttext.train_supervised("1.txt", lr=0.1, dim=100, epoch=5, , word_ngrams=2, loss='softmax')
model.save_model("model_file.bin")

