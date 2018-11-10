def paint_fence(n, k):
    # n is the number of post
    # k is the number of colors
    if n == 1:
        return k, 0
    if n == 2:
        return k*(k-1), k  # ways if two posts are different, ways if two posts are the same
    diff_n_1, same_n_1 = paint_fence(n-1, k)
    diff, same = same_n_1 * (k-1) + same_n_1 * (k-1), diff_n_1
    return diff, same

n = 3
k = 2
print(paint_fence(n, k))
