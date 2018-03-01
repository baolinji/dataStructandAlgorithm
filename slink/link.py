#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""

class lnode(object):
    def __init__(self,data):
        self.value = data
        self.lnext = None

class link(object):

    def __init__(self):
        self.root = lnode(None)

    def create(self,data):
        cursor = self.root
        for v in data:
            if cursor.value is None:
                cursor.value = v
            else:
                temp = lnode(v)
                cursor.lnext = temp
                cursor = cursor.lnext

    @property
    def lenght(self):

        cursor = self.root
        if cursor.value is None and cursor.lnext is None:
            return 0
        lenght = 1
        while(cursor.lnext is not None):
            cursor = cursor.lnext
            lenght +=1
        return lenght

    def covert(self):
        cursor = self.root
        pre = None
        while cursor.lnext is not None:
            temp = cursor.lnext
            cursor.lnext = pre
            pre = cursor
            cursor = temp
        cursor.lnext = pre

    def search(self,index):

        if index>self.lenght:
            print "This list is invalid"

        cur = self.root
        while index>0:
            cur = cur.lnext
            index = index - 1
        return cur

    def sort(self):

        return 0

    def delete(self,index):

        if index > self.lenght:
            raise ValueError("this list lenght is invaild.")

        cur = self.root
        pre = None
        while index >0:
            pre = cur
            cur = cur.lnext
            index -= 1
        pre.lnext = cur.lnext

    def add(self,index,value):

        if self.root is None:
            self.create([value])

        if index > self.lenght or index <0:
            raise ValueError("this index is more than self lenght.")

        cur = self.root
        pre = None
        while index>0:
            pre = cur
            cur =  cur.lnext
            index -= 1
        temp = node(value)
        pre.lnext = temp
        temp.lnext = cur



if __name__ == "__main__":

    data = [1,2,3,4,5]
    tLink = link()

    tLink.create(data)
    r = tLink.search(10)
    tLink.delete(2)
    tLink.add(2,10)
    #tLink.covert()
    print 1
