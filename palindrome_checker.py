# -*- coding: utf-8 -*-
"""
Palindrome checker
"""
from collections import deque
def palck(string):
    dq = deque(string.replace(' ','').lower())
    for i in range(len(dq)//2):
        if dq.popleft() != dq.pop():
            return False
    return True

A = palck('I haahi')
print(A)
