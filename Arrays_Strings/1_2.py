#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:31:13 2017

@author: dhingratul

P1.2
"""


def isPerm(s1, s2):
    d = {}
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s2)):
            if s2[i] in d:
                temp = d.get(s2[i])
                d[s2[i]] = temp+1
            else:
                d[s2[i]] = 1
        for i in range(len(s1)):
            if s1[i] in d:
                temp = d.get(s1[i])
                if temp == 1:

                    del(d[s1[i]])
            else:
                return False
        else:
            return True

# Main
print(isPerm("Abc","cbDA"))