#coding:utf-8

__author__ = 'lamter'

import sys
import logging
import unittest


def suite():
    testSuite1 = unittest.makeSuite(GloveTest, "test")
    alltestCase = unittest.TestSuite([testSuite1, ])
    return alltestCase


class GloveTest(unittest.TestCase):
    '''
    测试武将相关
    '''
    def setUp(self):
        pass



    def test_int(self):
        """
        测量 int 的大小
        :return:
        """
        value = 1
        init
