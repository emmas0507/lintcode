def drop_egg(n, k):
    # n is number of eggs and k is number of floors
    eggfloor = [[0] * (k+1) for i in range(n)]

    for j in range(k+1):
        eggfloor[0][j] = j

    for i in range(n):
        eggfloor[i][0] = 0

    for i in range(n):
        eggfloor[i][1] = 1

    for i in range(1, n):
        for j in range(2, k+1):
            eggfloor[i][j] = 20000
            # print(eggfloor)
            for x in range(1, j):
                # print('x is {}'.format(x))
                res = 1 + max(eggfloor[i-1][x-1], eggfloor[i][j-x])
                # print('res is {}'.format(res))
                if res < eggfloor[i][j]:
                    eggfloor[i][j] = res
    return eggfloor[n-1][k]


n = 2
k = 100
ef = drop_egg(n, k)

print(ef)

# # A Dynamic Programming based Python Program for the Egg Dropping Puzzle
# INT_MAX = 32767
#
# # Function to get minimum number of trials needed in worst
# # case with n eggs and k floors
# def eggDrop(n, k):
#     # A 2D table where entery eggFloor[i][j] will represent minimum
#     # number of trials needed for i eggs and j floors.
#     eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
#
#     # We need one trial for one floor and0 trials for 0 floors
#     for i in range(1, n+1):
#         eggFloor[i][1] = 1
#         eggFloor[i][0] = 0
#
#     # We always need j trials for one egg and j floors.
#     for j in range(1, k+1):
#         eggFloor[1][j] = j
#
#     # Fill rest of the entries in table using optimal substructure
#     # property
#     for i in range(2, n+1):
#         for j in range(2, k+1):
#             eggFloor[i][j] = INT_MAX
#             for x in range(1, j+1):
#                 res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
#                 if res < eggFloor[i][j]:
#                     eggFloor[i][j] = res
#
#     # eggFloor[n][k] holds the result
#     return eggFloor[n][k]
#
# # Driver program to test to pront printDups
# n = 2
# k = 36
# print("Minimum number of trials in worst case with" + str(n) + "eggs and "
#        + str(k) + " floors is " + str(eggDrop(n, k)))
