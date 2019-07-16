# !/usr/bin/env python
# coding=utf-8
# by lsd 2017-05-18

"""
一个好用的人名词典
"""
from dictionary.common.CommonDictionary import CommonDictionary
from dictionary.item.EnumItem import EnumItem
from abc import ABCMeta, abstractmethod
from utility.Predefine import Predefine
from utility.ByteUtil import ByteUtil
from corpus.io.Convert import Convert
from corpus.io.IOUtil import IOUtil
from corpus.tag.NR import NR
import pickle


class NRDictionary(CommonDictionary):
    __metaclass__ = ABCMeta

    def __init__(self):
        CommonDictionary.__init__(self)
        self.logger = Predefine.logger

    def onLoadValue(self, path):
        valueArray = self.loadDat1(path + '.value.dat')
        if valueArray is not None:
            return valueArray

        valueList = []
        line = None

        try:
            br = open(path, 'r')
            while 1:
                line = br.readline().strip(' \n\t\r')
                if not line:
                    break
                args = EnumItem.create(line)
                nrEnumItem = EnumItem()
                for e in args.values()[0]:
                    nrEnumItem = nrEnumItem.init1(NR.valueOf(e.keys()[0]), int(e.values()[0]))
                valueList.append(nrEnumItem.labelMap.items())
            self.onSaveValue(valueList, path)
        except Exception as e:
            self.logger.error("读取%s失败[%s]\n该词典这一行格式不对：%s" % (path, str(e), line))
            return None

        return valueList

    def onSaveValue(self, valueArray, path):
        return self.saveDat(path + '.value.dat', valueArray)

    def saveDat(self, path, valueArray):
        try:
            out = open(path, 'w+')
            out.writelines(Convert.convert(len(valueArray)))
            for item in valueArray:
                out.writelines(Convert.convert(len(item)))
                for entry in item:
                    out.writelines(Convert.convert(NR.ordinal(NR.valueOf(entry[0]))))
                    out.writelines(Convert.convert(int(entry[1])))
            out.close()
        except Exception as e:
            self.logger.warning("保存失败%s" % str(e))
            return False

        return True

    def loadDat1(self, path):
        try:
            bytes = pickle.load(open(path + Predefine.PIC_EXT, 'rb'))
        except Exception as e:
            bytes = IOUtil().readBytes(path)
            out = open(path + Predefine.PIC_EXT, 'wb')
            pickle.dump(bytes, out)
        if bytes is None:
            return None
        nrArray = list(NR)
        index = 0
        size = ByteUtil.bytesHighFirstToInt(bytes, index)
        index += 4
        valueArray = [None] * size
        item = None
        for i in range(size):
            currentSize = ByteUtil.bytesHighFirstToInt(bytes, index)
            index += 4
            item = EnumItem()
            tm_dict = {}
            for j in range(currentSize):
                nr = nrArray[ByteUtil.bytesHighFirstToInt(bytes, index)]
                index += 4
                frequency = ByteUtil.bytesHighFirstToInt(bytes, index)
                index += 4
                item = item.init1(nr, frequency)
            valueArray[i] = item.labelMap.items()
        return valueArray


if __name__ == "__main__":
    nd = NRDictionary().loadDat1('D:/liepin_project/py-segmentation/data/dictionary/person/nr.txt.value.dat')
    print(nd)
