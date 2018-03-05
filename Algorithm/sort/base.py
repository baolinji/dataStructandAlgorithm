#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""
import time


class baseSort(object):

    def __init__(self,data):
        self.data = data

    def CHeck(self):
        pass

    def bubble_sort(self):

        if len(self.data) == 0:
            return self.data

        if len(self.data) == 1:
            return self.data

        for j in range(len(self.data)):
            for i in range(len(self.data)-j-1):
                if self.data[i] < self.data[i+1]:
                    self.data[i],self.data[i+1] = self.data[i+1],self.data[i]

        return self.data

    def select_sort(self):

        if len(self.data) == 0:
            return self.data

        if len(self.data) == 1:
            return self.data

        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i] < self.data[j]:
                    self.data[i],self.data[j] = self.data[j],self.data[i]
        return self.data

    def inset_sort(self):
        #

        for i in range(len(self.data)):
            for j in range(i):
                if self.data[j] <self.data[i]:
                    self.data[i],self.data[j] = self.data[j],self.data[i]
        return self.data

    def binanry_sort(self):

        pass

    def quicklySort(self):

        if len(self.data) == 0 or  len(self.data) == 1:
            return self.data

        return self.data



if __name__ == "__main__":
    data = [12,43,4,67,1,334,5,6,87,9,1002,23,56]
    # data = [2,5]
    start = time.time()
    obj = baseSort(data)
    print obj.bubble_sort()
    end = time.time()
    print end-start
    print obj.select_sort()
    print time.time() - end
    print obj.inset_sort()