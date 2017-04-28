#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:45:19 2017

@author: dhingratul
"""

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''
root.left=Node(2)
root.right=Node(3)

root.left.left  = Node(4);
'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''     