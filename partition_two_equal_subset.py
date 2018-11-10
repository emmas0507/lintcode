def parition_two_equal_subset(input, target, visited):

    # if input[-1] > target:
    #     print('last element is larger than target')
    #     return False
    # elif input[-1] == target:
    #     return True
    # else:
        for ind in range(len(input)):
            if not visited[ind]:
                visited[ind] = True
                print('target is {}, and input element is {}, visited list {}'.format(target, input[ind], visited))
                if target == input[ind]:
                    return True
                elif target - input[ind] > 0:
                    flag = parition_two_equal_subset(input, target - input[ind], visited)
                    return flag
                else:
                    continue
        return False


# input = [4, 3, 2, 3, 5, 2, 1]
input = [1,2,3,5]
target = sum(input)/2
visited = [False] * len(input)
print(parition_two_equal_subset(input, target, visited))

