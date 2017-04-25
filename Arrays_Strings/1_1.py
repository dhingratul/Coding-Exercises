#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:24:38 2017

@author: dhingratul

P 1.1
"""

def isUnique(s):
    s2=s.upper()
    l=set(list(s2))
    if len(l) == len(s2):
        return True
    else:
        return False

# Main program
print(isUnique("ABCc"))    
    