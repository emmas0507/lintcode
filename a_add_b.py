# add two integer without using arithmetic oerpation

def aplusb(a, b):
    arev_bin = prepare_rev_bin(a)
    brev_bin = prepare_rev_bin(b)
    if len(arev_bin) < len(brev_bin):
        new_bin = [False] * len(brev_bin)
        for i in range(len(brev_bin)):
            new_bin[i] = arev_bin[i]
    elif len(brev_bin) < len(arev_bin):
        new_bin = [False] * len(arev_bin)
        for i in range(len(arev_bin)):
            new_bin[i] = brev_bin[i]
    else:
        pass
    print(arev_bin, brev_bin)
    add_list = []
    index = 0
    add_ = False
    while index < len(arev_bin):
        print(index)
        tmpa = arev_bin[index]
        tmpb = brev_bin[index]
        if tmpa and tmpb:
            import pdb; pdb.set_trace()
            if add_:
                add_list = add_list + [True]
                add_ = True
            else:
                add_list = add_list + [False]
                add_ = True
        elif tmpa or tmpb:
            if add_:
                add_list = add_list + [False]
                add_ = True
            else:
                add_list = add_list + [True]
                add_ = False
        else:
            if add_:
                add_list = add_list + [True]
                add_ = False
            else:
                add_list = add_list + [False]
                add_ = False
        print(add_list)
        print(add_)
        index = index + 1
    print(add_list)
    add_list2 = add_list + [add_]
    print(add_list2)
    new_int = 0
    for i in range(len(add_list2)):
        new_int = new_int + int(add_list2[i]) * pow(2, i)
    return new_int

def prepare_rev_bin(a_int):
    abin = convert_int_bin(a_int)
    arev_bin = reverse_list(abin)
    return arev_bin

def reverse_list(alist):
    rev_list = [0] * len(alist)
    for i in range(len(alist)):
        rev_list[len(alist)-1-i] = alist[i]
    return rev_list

def convert_int_bin(x):
    xlist = []
    while x > 0:
        xlist = [x % 2] + xlist
        x = x // 2
    xbin = [bool(x_) for x_ in xlist]
    return xbin

new_int = aplusb(5, 5)
print(new_int)



