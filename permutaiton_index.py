import math

def permutation_index(input_array):
    array_length = len(input_array)
    if array_length == 1:
        return 1
    else:
        sorted_array = sorted(input_array)
        rank_of_first_value = sorted_array.index(input_array[0])
        return rank_of_first_value * math.factorial(array_length-1) + permutation_index(input_array[1:])


input_array = [2, 3, 1]

print(permutation_index(input_array))

