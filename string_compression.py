def string_compression(s):

    compressed_str = ''
    count = 0
    curr_char = s[0]
    for i in range(len(s)):
        if s[i] == curr_char:
            count = count + 1
        else:
            if count <= 2:
                compressed_str = compressed_str + curr_char * count
            else:
                compressed_str = compressed_str + curr_char + str(count)
            curr_char = s[i]
            count = 1
        print('i is {}, curr_char is {}, count is {}'.format(i, curr_char, count))
    if count <= 2:
                compressed_str = compressed_str + curr_char * count
    else:
        compressed_str = compressed_str + curr_char + str(count)
    return compressed_str

s = 'aaabbcccaaa'
print(string_compression(s))
