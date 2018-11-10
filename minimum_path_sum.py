def minimum_path_sum(input_array, i, j):
    if i == 0 and j == 0:
        return input_array[0][0]
    elif i == 0:
        left_value = minimum_path_sum(input_array, i, j-1)
        return left_value + input_array[i][j]
    elif j == 0:
        upper_value = minimum_path_sum(input_array, i-1, j)
        return upper_value + input_array[i][j]
    else:
        left_value = minimum_path_sum(input_array, i, j-1)
        upper_value = minimum_path_sum(input_array, i-1, j)
        return min(left_value, upper_value) + input_array[i][j]

input_array = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]

print(minimum_path_sum(input_array, 2, 2))
