def baseball_game(input_list):
    scores = [0] * 10
    index = -1
    for i in input_list:
        if i == 'C':
            index = index - 1
        elif i == 'D':
            scores[index + 1] = scores[index] * 2
            index = index + 1
        elif i == '+':
            if index > 0:
                scores[index+1] = scores[index] + scores[index-1]
            else:
                scores[index+1] = scores[index]
            index = index + 1
        else:
            scores[index+1] = int(i)
            index = index + 1
        print(scores)
    return sum(scores)

input_list = ["5","2","C","D","+"]
input_list = ["5","-2","4","C","D","9","+","+"]
print(baseball_game(input_list))
