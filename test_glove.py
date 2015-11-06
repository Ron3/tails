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
                    self.b2: self.b2,
                    u'unicode编码': None,
                }


        class B(): pass

        glove = Glove(A())
        print glove.size

