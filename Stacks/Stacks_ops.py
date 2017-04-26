#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:54:25 2017

@author: dhingratul

You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints



Output Format

For each type  query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
"""

n = int(input())
stack = []
for i in range(n):
    cmd = list(input().split(" "))
    if len(cmd) == 2:
        val = int(cmd[1])
    cmd = int(cmd[0])
    if cmd == 1:
        stack.insert(0, val)
    elif cmd == 2:
        stack.pop(0)
    else:
        print(max(stack))
