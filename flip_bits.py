#!/bin/python3

'''
You will be given a list of 32 bit unsigned integers. Flip all the bits and return the result as an unsigned integer.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    return ~n & 0xffffffff

print(flippingBits(9))