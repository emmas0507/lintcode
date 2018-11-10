def compare_dict(dict1, dict2):
    for k in dict1.keys():
        if (k not in dict2.keys()) or dict1[k] != dict2[k]:
            return False
    return True

def find_all_anagrams_in_string(s, p):
    index_list = []
    pdict = {}
    for i in p:
        if i in pdict.keys():
            pdict[i] = pdict[i] + 1
        else:
            pdict[i] = 1
    sdict = {}
    for i in range(len(p)):
        if s[i] in sdict.keys():
            sdict[s[i]] = sdict[s[i]] + 1
        else:
            sdict[s[i]] = 1

    for i in range(0, len(s)-len(p)):
        if compare_dict(pdict, sdict):
            index_list = index_list + [i]
        sdict[s[i]] = sdict[s[i]] - 1
        if s[i+len(p)] in sdict.keys():
            sdict[s[i+len(p)]] = sdict[s[i+len(p)]] + 1
        else:
            sdict[s[i+len(p)]] = 1
    return index_list

s = "cbaebabacd"
p = "abc"
print(find_all_anagrams_in_string(s, p))
