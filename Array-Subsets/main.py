#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# s_arr = list(numpy.sort(arr)[::-1])

def subsetA(arr):
    arr.sort(reverse=True)
    n = len(arr)
    total = sum(arr)
    current = 0
    res = []
    for i in range(n):
        current += arr[i]
        res.append(arr[i])
        if current * 2 > total:
            break

    res.sort()
    return res

if __name__ == '__main__':
    arr = [5, 3, 2, 4, 1, 2]
    subsetA(arr)
