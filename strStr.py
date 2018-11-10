# the first index of target string in source string

def strStr(source, target):
    flag = -1
    for i in range(len(source)):
        for j in range(len(target)):
            if source[i+j] != target[j]:
                break
        if j == len(target)-1:
            flag = 1
            break
    if flag == -1:
        return -1
    else:
        return i

source = 'abcdabcdefg'
target = 'bcd'
print(strStr(source, target))
