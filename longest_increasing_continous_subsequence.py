def longest_increasing_continous_subseq(input_array):
    max_length = 0
    longest_length = 1
    for i in range(len(input_array)-1):
        if input_array[i+1] > input_array[i]:
            longest_length = longest_length + 1
        else:
            max_length = max(max_length, longest_length)
            longest_length = 1
        print('i is {}, max_length is {}, longest_length is {}'.format(i, max_length, longest_length))
    max_length = max(max_length, longest_length)
    return max_length

input_array = [5, 4, 2, 1, 3]
input_array = [5, 1, 2, 3, 4]
input_array = [1, 2, 3, 4, 5]
print(longest_increasing_continous_subseq(input_array))
