def first_unique_character(input_array):
    # since character only has 26 characters
    number_array = [0] * 26
    for c in input_array:
        number_array[ord(c) - ord('a')] = number_array[ord(c) - ord('a')] + 1
    for i in range(len(input_array)):
        index = ord(input_array[i]) - ord('a')
        if number_array[index] == 1:
            return input_array[i]

input_array = 'abaccdeff'
# input_array = 'leetcode'
print(first_unique_character(input_array))

