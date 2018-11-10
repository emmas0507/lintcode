def length_of_last_word(str):
    last_word_length = 0
    for s in str:
        if s != ' ':
            last_word_length = last_word_length + 1
        else:
            last_word_length = 0
        print('char is {}, last word length is {}'.format(s, last_word_length))
    return last_word_length

str = "Hello World"
print(length_of_last_word(str))
