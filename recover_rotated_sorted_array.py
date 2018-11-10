def recover_rotated(input_array):
    index = 0
    while index < (len(input_array)-1) and input_array[index] < input_array[index+1]:
        index = index + 1
    new_array = input_array[(index+1):] + input_array[0:(index+1)]
    return new_array

input_array = [1,2,3,4]
print(recover_rotated(input_array))
input_array = [1,2,3,0]
print(recover_rotated(input_array))
input_array = [3,4,1,2]
print(recover_rotated(input_array))

