def longest_way(words_list):
    length_dict = {}

    for w in words_list:
        if len(w) in length_dict:
            length_dict[len(w)] = length_dict[len(w)] + [w]
        else:
            length_dict[len(w)] = [w]

    longest_l = max(length_dict.keys())
    return length_dict[longest_l]

words_list = ['dogs', 'google', 'facebook', 'internationalization', 'balbla']
words_list = ['like', 'love', 'hate', 'yes']
print(longest_way(words_list))
