def zigzag_traversal(m):
    i = 0
    j = 0
    nrows = len(m)
    ncols = len(m[0])
    while i < nrows and j < ncols:
        print('i is {}, j is {}'.format(i, j))
        print('value is {}'.format(m[i][j]))
        if (i + j) % 2 == 0:
            if i == 0:
                j = j + 1
            elif j == ncols-1:
                i = i + 1
            else:
                i = i - 1
                j = j + 1
        else:
            if j == 0:
                i = i + 1
            elif i == nrows-1:
                j = j + 1
            else:
                i = i + 1
                j = j - 1

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
zigzag_traversal(m)
