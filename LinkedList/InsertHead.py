#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:27:39 2017

@author: dhingratul

 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    if head is None:
        head = Node(data)
    else:
        newNode = Node(data)
        newNode.next = head
        head = newNode
    return head
