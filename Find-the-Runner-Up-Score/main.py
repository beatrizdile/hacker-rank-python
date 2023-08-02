if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    high = max(arr)

    c = arr.count(high)
    
    for x in range(c):
        arr.remove(high)
    
    print(max(arr))
