# Enter your code here. Read input from STDIN. Print output to STDOUT
# axis = 0 column
# axis = 1 lines
from numpy import *

nums = input().split()
cols = int(nums[0])
rows = int(nums[1])
num_arr = [[0 for i in range(cols)] for j in range(rows)]

for i in range(0, cols):
    arr = input().split()
    for j in range(0, rows):
        num_arr[i][j] = int(arr[j])

print(mean(num_arr, axis = 1))
print(var(num_arr, axis = 0))
print(round(std(num_arr, axis = None), 11))
