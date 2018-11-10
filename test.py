def func(index_list):
    func_dict = {}
    for i in range(1, len(index_list)):
        tmp_func = lambda x: x[index_list[0]] - x[index_list[i]]
        func_dict[i] = tmp_func
    import pdb; pdb.set_trace()
    return func_dict

i = 1
x = [1, 2, 4]

func_dict = func(index_list=[0, 2])
print(func_dict[i](x))
