#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    arr = s.split(':', 1)
    res = re.sub(r'[^0-9:]*', '', arr[1]);
    num = int(arr[0])
    if (arr[1][-2] == 'P'):
        if (num == 12):
            num = 0
        num += 12
    else:
        num %= 12
    return (f"{num:02}:{res}")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
