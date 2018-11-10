def search_2D_matrix(matrix, target):
    # (num_rows, num_cols) = matrix.shape

    def search_rows(alist, target):
        index = 0
        if alist[0] > target:
            return 0
        for index in range(len(alist)-1):
            if alist[index] <= target and alist[index+1] > target:
                return index
        return index + 1

    column_1_list = [x[0] for x in matrix]
    row_index = search_rows(column_1_list, target)

    def search_cols(alist, target):
        for index in range(len(alist)):
            if alist[index] == target:
                return True
        return False

    column_exists = search_cols(matrix[row_index], target)
    return column_exists

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 0

print(search_2D_matrix(matrix, target))
