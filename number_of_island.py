def get_curr_island(i, j, input, visited):
    index_list = [(i, j)]
    visited[i][j] = True
    while len(index_list) > 0:
        print(index_list)
        curr_i = index_list[-1][0]
        curr_j = index_list[-1][1]
        index_list = index_list[:-1]
        if curr_j < len(input[0]) - 1 and input[curr_i][curr_j+1] == 1 and visited[curr_i][curr_j+1] is False:
            index_list = index_list + [(curr_i, curr_j + 1)]
            visited[curr_i][curr_j+1] = True
        if curr_i < len(input) - 1 and input[curr_i+1][curr_j] == 1 and visited[curr_i+1][curr_j] is False:
            index_list = index_list + [(curr_i + 1, curr_j)]
            visited[curr_i+1][curr_j] = True

    return visited


def number_of_island(input):
    nisland = 0
    n = len(input)
    m = len(input[0])
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            print('i is {} and j is {}'.format(i,j))
            print('visited at i,j is {}'.format(visited[i][j]))
            if input[i][j] == 1 and visited[i][j] is False:
                nisland = nisland + 1
                visited = get_curr_island(i, j, input, visited)
    return nisland

input = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
input = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
i = 0
j = 0
n = len(input)
m = len(input[0])
visited = [[False] * m for k in range(n)]
print(get_curr_island(i, j, input, visited))
print(number_of_island(input))


