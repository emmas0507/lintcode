def kth_prime_number(k):
    prime_number_list = []
    i = 2
    while True:
        curr_prime = True
        for p in prime_number_list:
            if i % p == 0:
                curr_prime = False
                break
        if curr_prime:
            prime_number_list = prime_number_list + [i]
        if len(prime_number_list) == k:
            return prime_number_list[-1]
        print('i is {}, prime_number_list is {}'.format(i, prime_number_list))
        i = i + 1

k = 5

print(kth_prime_number(5))
