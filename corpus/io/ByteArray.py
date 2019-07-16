#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from utility.ByteUtil import ByteUtil
from corpus.io.IOUtil import IOUtil

class ByteArray(object):
    """
    对字节数组进行封装，提供方便的读取操作
    """

    def __init__(self):
        self.bytes = []
        self.offset = 0

    def init(self, bytes):
        self.bytes = bytes
        self.offset = 0
        return self

    @staticmethod
    def createByteArray(path):
        bytes = IOUtil().readBytes(path)
        if bytes is None:
            return None
        return ByteArray().init(bytes)

    def nextInt(self):
        """
        读取一个int
        :return:
        """
        result = ByteUtil.bytesHighFirstToInt(self.bytes, self.offset)
        self.offset += 4
        return result

    def nextChar(self):
        """
        读取一个char，对应于writeChar
        :return:
        """
        result = ByteUtil.bytesHighFirstToChar(self.bytes, self.offset)
        self.offset += 2
        return result

    def nextByte(self):
        """
        读取一个字节
        :return:
        """
        res = self.bytes[self.offset]
        self.offset += 1
        return res

    def hasMore(self):
        return self.offset < len(self.bytes)


if __name__ == "__main__":
    s = "好123"
    s2 = s
    l2 = list(s2)
    b = ByteArray().init(l2)
    print (b.bytes)