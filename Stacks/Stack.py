#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:06:55 2017

@author: dhingratul
"""

from sys import maxsize

def createStack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("Pushed item is", item)

def pop(stack):
    return stack.pop()

def peek(stack):
    # TO get the top elelment of stack
    return stack[len(stack)-1]

# Main program
stack=createStack();
push(stack,10)
push(stack, 20)
push(stack,30)    
print(pop(stack))             
print("Top element is",peek(stack))
