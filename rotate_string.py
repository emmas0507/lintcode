# rotate a string by number of offset

def rotate_string(input_str, n):
    n = n % len(input_str)
    new_str = input_str[n:] + input_str[0:n]
    return new_str

input_str = 'abcdfg'
n = 2

print(rotate_string(input_str, n))
