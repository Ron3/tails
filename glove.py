#coding:utf-8

__author__ = 'lamter'

import sys
import logging




class Glove(object):
    """
    calculate the size of a python obj.
    """
    def __init__(self, pyObj):
        """
        :param pyObj: a Python Obj
        :return:
        """
        self.orginObj = pyObj

        self.objs = {}          #

        self.size = 0           # byte

        # sort of constant and obj
        self.sort()


    def sort(self):
        """
        sort of constant and obj by type.
        :return:
        """

        if self.isConstant(self.orginObj):
            # const
            self.sortofconst()
        if isinstance(self.orginObj, list):
            # list
            self.sortoflist()
        elif isinstance(self.orginObj, dict):
            # dict
            self.sortofdict()
        else:
            # obj
            self.sortofobj()


    def sortofconst(self):
        """
        a const, int, float or basestring.

        >>> value= 1
        >>> glove = Glove(value)
        >>> glove.size
        24
        >>> value= 'a'
        >>> glove = Glove(value)
        >>> glove.size
        38

        :return:
        """
        self._addTotalSize(sys.getsizeof(self.orginObj))


    def sortoflist(self):
        """
        oringiObj is a list.

        :return:
        """
        size = self.getSizeOfList(self.orginObj)

        self._addTotalSize(size)



    def _addTotalSize(self, size):
        """
        :param size:
        :return:
        """
        self.size += size


    def meaure(self):
        """
        report
        :return:
        """
        text = 'total size: %s' % self.convert(self.size)

        logging.info(text)


    @staticmethod
    def convert(size):
        """
        all kinde of unit for size.

        >>> value = 16816513513761
        >>> Glove.convert(value) == "1TB	933GB	716MB	643KB	6433byte"
        False

        :param size:
        :return:
        """
        # kb = mb = gb = tb = 0

        TB = 1024 * 1024 * 1024 * 1024 * 8  # byte
        GB = 1024 * 1024 * 1024 * 8         # byte
        MB = 1024 * 1024 * 8                # byte
        KB = 1024 * 8                       # byte

        tb = size / TB
        rest = size % TB

        gb = rest / GB
        rest = rest % GB

        mb = rest / MB
        rest = rest % MB

        kb = rest / KB
        rest = rest % KB

        byte = rest

        return '%sTB\t%sGB\t%sMB\t%sKB\t%sbyte' % (tb, gb, mb, kb, byte)


    def isConstant(self, value):
        """

        :param value:
        :return:
        """
        return isinstance(value, (type(1), type(1.), basestring))


    def getSizeOfConstant(self, value):
        """
        get size of a list, recusively.
        :param value:
        :return:
        """
        return



    def _getSizeOfAny(self, value, obj=None):
        """
        :param value:
        :param obj: Not None meaning this value is belong to this obj not orginObj.
        :return:
        """
        size = 0
        if self.isConstant(value):
            # 常量
            size += self._addTotalSize(sys.getsizeof(value))
        elif isinstance(value, list):
            size += self.getSizeOfList(value, obj)
        elif isinstance(value, dict):
            size += self.getSizeOfDict(value, obj)
        else:
            size += 0
            self.getSizeOfObj(value)

        if obj:
            self.collectObj(obj, size)
            return 0
        else:
            return size




    def getSizeOfList(self, value, obj=None):
        """
        get size of a list, recusively.
        :param value:
        :param obj:
        :return:
        """
        # size of instance list itself, exclude data.

        size = 0
        for e in value:
            size += self._getSizeOfAny(e)

        if obj:
            self.collectObj(obj, sys.getsizeof(list) + s)
            return 0
        else:
            return size


    def getSizeOfDict(self, value, obj=None):
        """
        get size of a dict, recusively.
        :return:
        """
        size = 0
        for k, v in value.iteritems():
            size += self._getSizeOfAny(k)
            size += self._getSizeOfAny(v)

        if obj:
            self.collectObj(obj, sys.getsizeof(dict) + size)
            return 0
        else:
            return size


    def getSizeOfObj(self, obj):
        """
        get size of a obj, recusively.
        :param value:
        :return:
        """
        size = 0
        if self.isCountObj(obj):
            # This obj has been draw out.
            return size

        # size of obj itself.
        size = sys.getsizeof(obj)

        # add obj to collector to avoid count repeatedly.
        self.collectObj(obj, size)

        for k,v in obj.__dict__.iteritems():
            self._getSizeOfAny(k, obj)
            self._getSizeOfAny(v, obj)


    def sortofobj(self):
        """
        :return:
        """
        # count size of obj.
        self._addTotalSize(sys.getsizeof(self.orginObj))

        self.getSizeOfObj(self.orginObj)


    def isCountObj(self, obj):
        """
        the obj has been counted.
        :param obj:
        :return:
        """

        return obj in self.objs


    def collectObj(self, obj, size):
        """
        draw a obj from value.
        :param obj:
        :return:
        """
        if obj in self.objs:
            self.objs[obj] += size
        else:
            self.objs[obj] = size


    def sortofdict(self):
        """

        :return:
        """
        # TODO sortofdict


if __name__ == "__main__":
    import doctest
    doctest.testmod()