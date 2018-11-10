def depth_sum_nested_list_weight_sum(input, depth):
    sum = 0
    for i in input:
        if type(i) == list:
            sum = sum + depth_sum_nested_list_weight_sum(i, depth+1)
        else:
            sum = sum + i * depth
    print('input is and sum is {}, {}'.format(input, sum))
    return sum

input = [[1,1],2,[1,1]]
input = [1,[4,[6]]]
print(depth_sum_nested_list_weight_sum(input, depth=1))
