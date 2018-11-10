def product_exclude_itself(alist):
    sub_prod = [1] * len(alist)
    sub_prod[0] = alist[0]
    for i in range(1, len(alist)):
        sub_prod[i] = sub_prod[i-1] * alist[i]
    sub_prod_reverse = [1] * len(alist)
    sub_prod_reverse[-1] = alist[-1]
    for i in range(len(alist)-2, -1, -1):
        print(i)
        sub_prod_reverse[i] = sub_prod_reverse[i+1] * alist[i]
    print(sub_prod)
    print(sub_prod_reverse)
    product_list = [1] * len(alist)
    for i in range(len(alist)):
        if i < 1:
            pre_array = 1
        else:
            pre_array = sub_prod[i-1]
        if i >= len(alist)-1:
            post_array = 1
        else:
            post_array = sub_prod_reverse[i+1]
        print('i is {}'.format(i))
        print('pre_array is {}'.format(pre_array))
        print('post_array is {}'.format(post_array))
        product_list[i] = pre_array * post_array
    return product_list

alist = [1,2,3,4]
# print(product_exclude_itself(alist))

def product_exclude_itself(alist):
    sub_prod_reverse = [1] * (len(alist))
    for i in range(len(alist)-2, -1, -1):
        sub_prod_reverse[i] = sub_prod_reverse[i+1] * alist[i+1]
    print(sub_prod_reverse)
    product_list = [1] * len(alist)
    pre_array = 1
    for i in range(0, len(alist)):
        print(i)
        print(pre_array)
        print(sub_prod_reverse[i])
        product_list[i] = pre_array * sub_prod_reverse[i]
        pre_array = pre_array * alist[i]
    return product_list

print(product_exclude_itself(alist))
