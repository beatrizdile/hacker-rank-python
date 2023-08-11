def count_substring(string, sub_string):
    res = 0
    for i in range(len(string)):
        j = 0
        while(j < len(sub_string) and i+j < len(string)):
            if string[i+j] == sub_string[j]:
                j += 1
            else:
                break
            if j == len(sub_string):
                res += 1
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
