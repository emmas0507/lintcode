def valid_parentheses(str):
    # if left parenthese, push into stack, if right parenthese, pop from stack to see if type matches
    stack_list = []
    parenthese_pair = {'(': ')', '{': '}', '[': ']'}
    for s in str:
        if s in parenthese_pair.keys():
            stack_list = stack_list + [s]
        else:
            if len(stack_list) == 0:
                return False
            elif s == parenthese_pair[stack_list[-1]]:
                stack_list = stack_list[:-1]
            else:
                return False
    return True

str = "()[]{}"
str = "([)]"
print(valid_parentheses(str))
