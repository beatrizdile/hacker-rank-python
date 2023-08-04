#!/bin/python3

import math
import os
import random
import re
import sys
import numpy

#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# s_arr = list(numpy.sort(arr)[::-1])

def subsetA(arr):
    s_arr = sorted(arr, reverse=True)
    res = []
    while sum(res) <= sum(s_arr):
        res.append(s_arr[0])
        s_arr.remove(s_arr[0])

    res.sort()

    return res

if __name__ == '__main__':
    arr = [5, 3, 2, 4, 1, 2]
    subsetA(arr)
