def unique_paths(i, j):
    if i == 1:
        return 1
    elif j == 1:
        return 1
    else:
        left_value = unique_paths(i, j-1)
        upper_value = unique_paths(i-1, j)
        return left_value + upper_value

print(unique_paths(4, 5))
