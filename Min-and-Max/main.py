# Enter your code here. Read input from STDIN. Print output to STDOUT
# axis = 0 column
# axis = 1 lines

nums = input().split()
x = int(nums[0])
y = int(nums[1])
nums = [0 for j in range(x)]

for i in range(0, x):
    arr = input().split()
    for j in range(0, y):
        if j == 0:
            nums[i] = int(arr[j])
        elif nums[i] > int(arr[j]):
            nums[i] = int(arr[j])

for i in range(0, x):
    if i == 0:
        res = nums[0]
    elif res < nums[i]:
        res = nums[i]

print(f"{res}")
