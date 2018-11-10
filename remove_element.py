def remove_element(input_array, target):
    current_position = 0
    for i in range(len(input_array)):
        if input_array[i] != target:
            tmp = input_array[i]
            input_array[current_position] = tmp
            current_position = current_position + 1
    return input_array[:current_position]

input_array = [0,4,4,0,0,2,4,4]
target = 4

print(remove_element(input_array, target))
