def mergeSortedArray(a, b):
    a_index = 0
    b_index = 0
    new_array = []
    while (a_index < len(a)) and (b_index < len(b)):
        if a[a_index] <= b[b_index]:
            new_array = new_array + [a[a_index]]
            a_index = a_index + 1
        else:
            new_array = new_array + [b[b_index]]
            b_index = b_index + 1
    if a_index < len(a):
        new_array = new_array + a[a_index:]
    if b_index < len(b):
        new_array = new_array + b[b_index:]
    return new_array

a = [1,2,3,4]
b = [2,4,5,6]
print(mergeSortedArray(a, b))
