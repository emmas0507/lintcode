# for n! get how many number of zeros

def training_zeros(n):
    numzeros = 0
    power5 = 5
    while power5 <= n:
        numzeros = numzeros + n // power5
        power5 = power5 * 5
    return numzeros

print(training_zeros(25))
