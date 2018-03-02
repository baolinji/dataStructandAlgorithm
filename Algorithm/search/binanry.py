#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
  Author: Lynch
"""

def binantySearch1(value,target):
    """
    if target not in value return -1 ,else return index.
    :param value: 
    :param target: 
    :return: 
    """
    if len(value) == 0 or value[0] > target or value[-1] < target:
        return -1

    half = len(value)/2
    if target > value[half]:
        temp = binantySearch1(value[half:len(value)],target)
        if temp == -1:
            return -1
        else:
            half += temp
    elif target < value[half]:
        half = binantySearch1(value[0:half], target)
    elif target == value[half]:
        return half

    return half


def binanrySearch2(value,target,low,high):


    if len(value)== 0 or value[low]>target or value[high-1]<target:
        return -1

    if low == high and value[low] != target:
        return -1

    mid = low+(high-low)/2
    if value[mid]>target:
        return binanrySearch2(value,target,low,mid)
    elif value[mid]<target:
        # if mid+1 ,low may be more than high
        return binanrySearch2(value,target,mid,high)
    elif value[mid] == target:
        return mid


def binanrySearch3(value,target,low,high):

    #no recurrent
    pass


def insertValueSearch(value,target):



    pass


if __name__ =="__main__":

    data = [1,2,4,9,10,11,13]
    target = 6
    print binantySearch1(data,target)
    print binanrySearch2(data,target,0,len(data))