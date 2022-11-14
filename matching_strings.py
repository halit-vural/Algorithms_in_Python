#!/bin/python3
'''
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#
s = ['ab', 'ab', 'abc', 'bc']
q = ['ab', 'bc', 'abc']

def matchingStrings(strings, queries):
    # Write your code here
    results = [0 for _ in queries]
    for i, q in enumerate(queries):
        for s in strings:
            if q == s:
                results[i] += 1
    return results

print(matchingStrings(s, q))

