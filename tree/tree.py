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

class Tree():

    def __init__(self):
        self.root = None

    def create(self,t,data,i):
        """先序创建"""
        if data[i] =='#':
            return None
        else:
            t = node(data[i])
            t.lchild = self.create(t.lchild,data,i+1)
            t.rchild = self.create(t.rchild,data,i+1)
        return t

    def add_node(self,data):
        """层次"""
        self.leaf = []
        for i in data:
            if self.root == None:
                self.root = node(i)
                self.leaf.append(self.root)
            else:
                treenode = self.leaf[0]
                if treenode.lchild is None:
                    treenode.lchild = node(i)
                    self.leaf.append(treenode.lchild)
                else:
                    treenode.rchild = node(i)
                    self.leaf.append(treenode.rchild)
                    self.leaf.pop(0)


    def pre_visit(self,root):
        if root is None:
            return
        else:
            print root.value
            self.pre_visit(root.lchild)
            self.pre_visit(root.rchild)

    def mid_visit(self,root):
        if root is None:
            return None
        else:
            self.mid_visit(root.lchild)
            print root.value
            self.mid_visit(root.rchild)

    def aft_visit(self,root):
        if root is None:
            return
        else:
            self.aft_visit(root.rchild)
            self.aft_visit(root.lchild)
            print root.value


    def insert(self,root,data):
        if root.lchild is None:
            root.lchild = node(data)

        pass


    def sTree(self,root,target):

        if self.root is None:
            pass
        if self.root.value> target:
            self.sTree(self.root.lchild,target)
        if self.root.value< target:
            self.sTree(self.root.rchild,target)





if __name__ == "__main__":
    tree = Tree()
    # data = [1,2,3,4,5,6,12,3,4,5,12,4,3,4]
    # tree.add_node(data)

    temp =[1,2,3,4,5,6,7,8,9]
    for i in temp:
        tree.sTree(tree.root,i)
    print 1