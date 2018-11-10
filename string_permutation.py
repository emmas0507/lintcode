def string_permutation(str1, str2):
    char_list1 = [None] * 26
    char_list2 = [None] * 26
    for s in str1:
        index = ord(s) - ord('a')
        char_list1[index] = char_list1[index] + 1
    for s in str2:
        index = ord(s) - ord('a')
        char_list2[index] = char_list2[index] + 1
    for i in range(26):
        if char_list1[i] != char_list2[i]:
            return False
    return True

str1 = ''
