#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version
import  array
import math
from utility.Predefine import Predefine

class BitSet(object):
     # from low to high "00000001 00000010 00000011", the array is [1, 2, 3]

      def __init__(self,capacity=64):
          # "B"类型相当于 C 语言的 unsigned char， 即占用1byte（8位），所以size大小设置为8
          self.unit_size = 8
          self.unit_count = abs(math.floor((capacity + self.unit_size - 1) / self.unit_size))
          self.capacity = capacity
          self.arr = array.array("B",[0] * self.unit_count)
          self.logger = Predefine.logger

      def any(self):
        # 是否存在置为 1 的位
        for a in self.arr:
            if a != 0:
                return True
        return False


      def all(self):
          # 是否所有位都为 1， 即是否存在置为 0 的位
          t = (1 << self.unit_size) -1
          for a in self.arr:
              if (a & t) != t:
                  return False
          return True

      def none(self):
         # 是否所有位都为1，即是否存在位置为 0的位
         for  a in self.arr:
             if a !=0:
                 return False
         return True

     # 所有位为零为真
      def isEmpty(self):
          return self.none()


      def count(self):
        c = 0
        for a in self.arr:
            while a > 0:
                if a & 1:
                    c += 1
                a = a >> 1
        return c

      def size(self):
        return self.unit_count * self.unit_size

      def get(self, pos):
        index = int(pos / self.unit_size)
        offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
        return (self.arr[index] >> offset) & 1

      def get1(self, bitIndex):
         if bitIndex < 0:
            self.logger.error("bitIndex < 0" + str(bitIndex))

      def test(self, pos):
        if self.get(pos):
            return True
        return False

      def set(self, pos=-1):
        if pos >= 0:
            index = int(pos / self.unit_size)
            offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
            self.arr[index] = (self.arr[index]) | (1 << offset)
        else:
            t = (1 << self.unit_size) - 1
            for i in range(self.unit_count):
                self.arr[i] = self.arr[i] | t

      def reset(self, pos=-1):
        if pos >= 0:
            index = int(pos / self.unit_size)
            offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
            x = (1 << offset)
            self.arr[index] = (self.arr[index]) & (~x)
        else:
            for i in range(self.unit_count):
                self.arr[i] = 0

      def flip(self, pos=-1):
         if pos >= 0:
            if self.get(pos):
                self.reset(pos)
            else:
                self.set(pos)
         else:
            for i in range(self.unit_count):
                self.arr[i] = ~self.arr[i] + (1 << self.unit_size)

      def binstr(self):
          b = ""
          for a in self.arr:
             t = bin(a)
             b += "0" * (self.unit_size - len(t) + 2) + t + ","
          return "[" + b.replace("0b", "").strip(",") + "]"

      def show(self):
          return self.arr

if __name__ =="__main__":
    b = BitSet(16)
    for  i in range(16):
        if i % 5 ==0 :
            b.set(i)
    print(b)
    print(b.size())
    for i in range(16):
        print(b.get(i))
    #b.set(17)