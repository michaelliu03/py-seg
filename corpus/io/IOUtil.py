#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version


from utility.Predefine import Predefine


class IOUtil(object):

    def __init__(self):
        self.logger = Predefine.logger

    def readBytes(self,path):
        try:
            return self.readBytesFromFile(path)
        except Exception as e:
            self.logger.warning("读取%s时发生异常%s" %(path,str(e)))

    def readBytesFromFile(self,path):
        bytes = []
        file1 = open(path, 'r',encoding='utf-8')
        n = 1
        while 1:
            line = file1.readline().strip(' \r\n')
            if not line:
                break

            for item in line.split(' '):
                i1 = item[:2]
                i2 = item[2:]

                for i in [i1, i2]:
                    if i != '':
                        v = int(i, 16)
                        if v >= 128:
                            v = v - 256
                        bytes.append(v)
            n += 1
        return bytes

if __name__ == "__main__":
    IOUtil().readBytesFromFile("D:/liepin_project/data/dictionary/person/nr.txt.value.dat")# file is latin1