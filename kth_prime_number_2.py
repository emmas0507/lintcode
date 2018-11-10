def kth_prime_number_2(k):
    # kth number that is multiplicative of 3, 5, 7
    number_list = [1]
    index3 = 0
    index5 = 0
    index7 = 0
    while True:
        num = min(min(number_list[index3] * 3, number_list[index5] * 5), number_list[index7] * 7)
        number_list = number_list + [num]
        if ( num / number_list[index3] == 3):
            index3 = index3 + 1
        if ( num / number_list[index5] == 5):
            index5 = index5 + 1
        if ( num / number_list[index7] == 7):
            index7 = index7 + 1
        if len(number_list) == k+1:
            break;
    print(number_list)
    return number_list[-1]

k = 5
print(kth_prime_number_2(k))
