def valid_anagram(s, t):
    s_dict = {}
    for c in s:
        if c in s_dict.keys():
            s_dict[c] = s_dict[c] + 1
        else:
            s_dict[c] = 1
    for c in t:
        if c in s_dict.keys():
            s_dict[c] = s_dict[c] - 1
            if s_dict[c] < 0:
                return False
    return True

s = 'abcd'
t = 'dcab'

print(valid_anagram(s, t))
