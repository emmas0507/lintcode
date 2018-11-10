def reverse_words(w):
    w = w + ' '
    rword = ''
    curr_word_start = 0
    for i in range(len(w)):
        if w[i] == ' ':
            print(curr_word_start)
            rword = w[curr_word_start:i] + ' ' + rword
            curr_word_start = i + 1
    return rword[:-1]

w = 'the sky is blue'
w = 'a b c'
print(reverse_words(w))
