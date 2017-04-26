#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:22:34 2017

@author: dhingratul


 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    current = head
    while(current.next is not None):
        print(current.data)
        current = current.next
    print(current.data)
