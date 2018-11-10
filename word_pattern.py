def word_pattern(pattern, str_input):
    str = str_input.split(' ')
    pattern_dict = {}
    for i in range(len(pattern)):
        if pattern[i] in pattern_dict.keys():
            pattern_dict[pattern[i]] = pattern_dict[pattern[i]] + [i]
        else:
            pattern_dict[pattern[i]] = [i]

    for key, value in pattern_dict.items():
        str_ = str[value[0]]
        for v in value[1:]:
            if str[v] != str_:
                return False
    return True

pattern = 'abba'
str_input = "dog cat cat fish"

print(word_pattern(pattern, str_input))
