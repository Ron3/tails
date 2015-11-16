#coding:utf-8

__author__ = 'lamter'

import sys
import logging
import unittest
from glove import Glove

def suite():
    testSuite1 = unittest.makeSuite(GloveTest, "test")
    alltestCase = unittest.TestSuite([testSuite1, ])
    return alltestCase


class GloveTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        pass



    def test_int(self):
        """
        测量 int 的大小
        :return:
        """
        value = 1



    def test_pythonObj(self):
        """
        :return:
        """
        class A():
            def __init__(self):
                self.b1 = B()
                self.b2 = B()
                self.list = [1000, 23424.2, 'asdf0', u'unicode编码', self.b1]
                self.dic = {
                    132323423412312311: 'utf8编码',
                    '232': self.b2,
                    self.b2: set([1,2]),
                    u'unicode编码': None,
                }

            @property
            def propertyName(self):
                return 'propertyname'


        class B(): pass

        glove = Glove(A())
        glove.meaure()
        print glove.report


    def test_property(self):
        """

        :return:
        """
        class C():pass
        def foo():pass
        print
        print type(C()) == type


    def test_measure(self):
        """

        :return:
        """
        class A():
            pass

        a = A()

        for i in xrange(100):
            a1 = A()
            for j in xrange(100):
                a2 = A()
                setattr(a1, 'a%s' % j, a2)
            setattr(a, 'a%s' % i, a1)

        glove = Glove(a)
        glove.meaure()
        print glove.report



