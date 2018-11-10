def compare_string(strA, strB):
    dictA = {}
    flag = True
    for s in strA:
        if s in dictA.keys():
            dictA[s] = dictA[s] + 1
        else:
            dictA[s] = 1
    for s in strB:
        if s in dictA.keys() and dictA[s] >= 1:
            dictA[s] = dictA[s] - 1
        else:
            flag = False
            return flag
    return flag

strA = 'ABCD'
strB = 'AABC'

print(compare_string(strA, strB))
