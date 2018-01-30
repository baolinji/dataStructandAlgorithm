#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""
class node(object):

    def __init__(self,data):
        self.value = data
        self.lchild = None
        self.rchild = None

class Tree(node):

    def __init__(self,value):
        super(Tree,self).__init__(value)
        self.root = None

    def create(self,data):
        cursor = self.root
        if cursor is None:
            cursor = node(data[0])

        for i in data:
            #update tree
            if cursor.lchild is None:
                cursor.lchild = node(i)

            else:
                cursor.rchild = node(i)
                cursor = cursor.lchild

    def sTree(self,type=0):
        """
        0:;
        1:;
        2:;
        :param type: 
        :return: 
        """
        if self.root is None:
            return
        if type == 0:
            pass
        if type == 1:
            pass
        if type == 3:
            pass
