def kth_largest_in_n_arrays(arrays, K):
    sorted_arrays = []
    for i in range(len(arrays)):
        sorted_arrays = sorted_arrays + [sorted(arrays[i])]


    for k in range(K):
        lnumbers = []
        for i in range(len(sorted_arrays)):
            if len(sorted_arrays[i]) > 0:
                lnumbers = lnumbers + [sorted_arrays[i][-1]]
        max_number = max(lnumbers)
        max_index = lnumbers.index(max_number)
        sorted_arrays[max_index] = sorted_arrays[max_index][:-1]
        import pdb; pdb.set_trace()
    return max_number

arrays = [[9,3,2,4,7], [1,2,3,4,8]]
K = 3

print(kth_largest_in_n_arrays(arrays, K))

