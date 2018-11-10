def happy_number(x):
    number_list = []
    while x != 1:
        digit_list = []
        d = x
        while d > 0:
            digit_list = digit_list + [d % 10]
            d = d / 10
        x = sum([dd**2 for dd in digit_list])
        if x in number_list:
            return False
        else:
            number_list = number_list + [x]
        print(number_list)
    return True

x=17
print(happy_number(x))
