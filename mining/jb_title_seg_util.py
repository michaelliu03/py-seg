#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version
import os
import codecs
from NlpAnalysis import NlpAnalysis
import  re
import random
import shutil

from sklearn.model_selection import train_test_split

segment = NlpAnalysis.newSegment().enableNameRecognize(False)
# 停用词表加载方法
def get_stopword_list():
    # 停用词表存储路径，每一行为一个词，按行读取进行加载
    # 进行编码转换确保匹配准确率
    stop_word_path = './stopword.txt'
    stopword_list = [sw.replace('\n', '') for sw in open(stop_word_path).readlines()]
    return stopword_list

'''
  构造二、三级目录并做成字典
'''
job_cls3_dict = {}
job_cls2_dict = {}
def get_label_list(path):
    with open(path, 'r', encoding='utf-8') as corpus_f:
        for line in corpus_f:
            line = line.strip('\r\n\t ')
            if line == '':
                continue
            else:
               line_cell = line.split(',')
               job_cls2_dict.setdefault(line_cell[2],line_cell[3])
               job_cls3_dict.setdefault(line_cell[4],line_cell[5])
    corpus_f.close()


def text_rem_bracket(text):
    r = re.sub("[（]", "(", text)
    ra = re.sub("[）]", ")", r)
    a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", ra)
    return a

def seg_words(text):
    termList = segment.seg(text)
    item = []
    for i in termList:
        item.append(i.word.lstrip().rstrip())
    #print(" ".join(item))
    return " ".join(item)


def load_data(inputfile,trainfilepath,testfilepath,ratio):
    ftrain = open(trainfilepath, "w",encoding='utf-8')
    ftest = open(testfilepath, "w",encoding='utf-8')
    count = 0
    with open(inputfile, 'r',encoding='utf-8') as fr:
        count += 1
        for line in fr:
            line = line.strip('\r\n\t ')
            if line == '':
                continue
            else:
                text_cell= line.split('\t')
                query_count = text_cell[4]
                if int(query_count) < 5:
                    continue
                else:

                    #print(query_count)
                    # 行号
                    line_num = text_cell[0]
                    # 去括号里面的内容
                    query_words = text_rem_bracket(text_cell[1].lower())
                    # 分词
                    sw = seg_words(query_words)
                    outline = sw
                    #label = "__label__"+ text_cell[2].lower() # 拼成可训练的样本
                    outline  = outline + "\t__label__"+ text_cell[2].lower() + "\n" # 拼成可训练的样本

                if count < int(line_num) * ratio:
                    ftrain.write(outline)
                    ftrain.flush()
                else:
                    ftest.write(outline)
                    ftest.flush()

    fr.close()
    ftrain.close()
    ftest.close()

    # text = text.decode("utf-8").encode("utf-8")
    # seg_text = jieba.cut(text.replace("\t", " ").replace("\n", " "))
    # outline = " ".join(seg_text)
    # outline = outline.encode("utf-8") + "\t__label__" + e + "\n"





# ftrain = codecs.open('some.txt','r',encoding='utf-8')
# segment = NlpAnalysis.newSegment().enableNameRecognize(False)
# for line in ftrain:
#     line = line.split("\t")


if __name__ == '__main__':
    get_label_list('dim_jobtitle.txt')
    load_data('some.txt','1.txt','1_test.txt',0.8)

