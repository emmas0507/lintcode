def remove_duplicates_sorted_array(input_array):
    current_value = input_array[0]
    current_index = 1
    for i in range(1, len(input_array)):
        if input_array[i] > current_value:
            current_value = input_array[i]
            input_array[current_index] = current_value
            current_index = current_index + 1
    return input_array[0:current_index]

a = [1, 1, 2, 2, 2, 3, 4]

print(remove_duplicates_sorted_array(a))
