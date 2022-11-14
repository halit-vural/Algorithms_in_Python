#!/bin/python3

'''
Given an array of integers, where all elements but one occur twice, find the unique element.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    lonely = []
    for x in a:
        if x in lonely:
            lonely.remove(x)
        else:
            lonely.append(x)

    return lonely[0]


a = [1,2,3,4,2,1,4]
print(lonelyinteger(a))