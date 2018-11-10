def sum_of_all_subsets(n):
    # number of subsets of n is pow(2, n)
    # from n to n+1, it is sum_of_all_subsets(n) + pow(2, n) * (n+1)
    if n == 1:
        return 1
    else:
        return sum_of_all_subsets(n) * 2 + pow(2, n-1) * n
