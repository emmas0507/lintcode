def longest_common_prefix(list_str):
    prefix = ""
    for i in range(len(list_str[0])):
        ichar = list_str[0][i]
        for str in list_str:
            if str[i] != ichar:
                return prefix
        prefix = prefix + ichar
    return prefix

list_str = ["flower", "flow", "flight"]
list_str = ["dog","racecar","car"]
print(longest_common_prefix(list_str))
