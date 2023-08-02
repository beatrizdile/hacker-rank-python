if __name__ == '__main__':
    size = int(input())
    arr = [[input(), float(input())] for _ in range(size)]
    arr.sort(key=lambda item: (item[1], item[0]))
    lowest = arr[0][1]
    arr.pop(0)
    i = 0
    while i < len(arr):
        if lowest == arr[i][1]:
            arr.pop(i)
        i += 1
    if arr[0][1] == lowest:
        arr.pop(0)
    i = 0
    sec_low = arr[0][1]
    while i < len(arr):
        if sec_low == arr[i][1]:
            print(arr[i][0])
        i += 1
