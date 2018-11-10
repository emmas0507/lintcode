def partition_array_odd_even(input_array):
    j = 0
    for i in range(len(input_array)):
        if input_array[i] % 2 == 1:
            tmp = input_array[i]
            input_array[i] = input_array[j]
            input_array[j] = tmp
            j = j + 1
    return input_array

input_array = [1, 2, 3, 4]

array_ = partition_array_odd_even(input_array)

print(array_)
