import numpy as np

def sum_of_square_numbers(n):
    if n < 0:
        return False
    else:
        k = int(np.floor(np.sqrt(n/2)))
    for i in range(k, 0, -1):
        if i * i == n:
            return True
        else:
            j = np.sqrt(n - i*i)
            if j * j + i * i == n:
                return True
    return False

n = 5

print(sum_of_square_numbers(n))

