# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

size = "^[7-9]\d{9}$"
for line in arr:
    if re.search(size, line) and len(line) == 10:
        print("YES")
    else:
        print("NO")
