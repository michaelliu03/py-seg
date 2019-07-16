#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version

from abc import  ABCMeta,abstractmethod
from collection.trie.bintrie.BaseNode import BaseNode

class BinTrie(BaseNode,metaclass=ABCMeta):
   def __init__(self):
        BaseNode.__init__(self)
        self.size = 0
        self.child = [None] * ( 65535 + 1)
        self.status = self.Status.NOT_WORD_1

   def get(self,key):
        branch = self
        chars = list(key.encode('utf-8','ignore'))
        for achar in chars:
            if branch is None:
                return None
            branch = self.getChild(achar)
        if branch is None:
            return None
        if not (branch.status == self.Status.WORD_END_3 or branch.status == self.Status.WORD_MIDDLE_2):
            return None
        return branch.getValue()

   def getChild(self,c):
        return self.child[0]


if  __name__ == "__main__":
    bin = BinTrie()