def say(curr_list):
    say_list = []
    count = 0
    curr_number = curr_list[0]
    for i in range(len(curr_list)):
        if curr_list[i] == curr_number:
            count = count + 1
        else:
            say_list = say_list + [count, curr_number]
            count = 1
            curr_number = curr_list[i]

    say_list = say_list + [count, curr_number]
    return say_list

def count_and_say(n):
    nlist = [1]
    for i in range(n-1):
        nlist = say(nlist)
    return nlist

n = 5

print(count_and_say(n))
