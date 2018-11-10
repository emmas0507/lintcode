def unique_paths2(input_array, index_i, index_j):
    if index_i == 0 and index_j == 0:
        return 1
    elif index_i == 0:
        if input_array[index_i][index_j] == 1:
            return 0
        else:
            return unique_paths2(input_array, index_i, index_j-1)
    elif index_j == 0:
        if input_array[index_i][index_j] == 1:
            return 0
        else:
            return unique_paths2(input_array, index_i-1, index_j)
    else:
        if input_array[index_i][index_j] == 1:
            return 0
        left_value = unique_paths2(input_array, index_i, index_j-1)
        upper_value = unique_paths2(input_array, index_i-1, index_j)
        return left_value + upper_value

input_array = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
# print(unique_paths2(input_array, index_i=2, index_j=2))

print(unique_paths2(input_array, index_i=2, index_j=2))
