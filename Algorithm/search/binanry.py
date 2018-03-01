#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""

def binantySearch(value,target):
    """
    
    :param value: 
    :param target: 
    :return: 
    """
    if len(value) == 0:
        return -1

    if value[0] > target or value[len(value)-1] < target:
        return -1

    if len(value) == 1:
        if value[0] == target:
            return 0
        else:
            return -1

    half = len(value)/2
    if target > value[half]:
        temp = binantySearch(value[half:len(value)],target)
        if temp == -1:
            return -1
        else:
            half += temp
    elif target < value[half]:
        half = binantySearch(value[0:half], target)
    return half

def quicklysearch(value,target):
    pass

if __name__ =="__main__":

    data = [1,2,3,4,5,6,7,8,9,10,12,13,14,15]
    target = 11
    print binantySearch(data,target)