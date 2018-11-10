def valid_palindromen(str):
    flag = True
    i = 0
    j = len(str) - 1
    while i <= j:
        if not str[i].isdigit() and not str[i].isalpha():
            i = i + 1
        elif not str[j].isdigit() and not str[j].isalpha():
            j = j - 1
        else:
            print('position i is {} and position j is {}'.format(str[i], str[j]))
            if str[i].lower() != str[j].lower():
                flag = False
                break
            else:
                i = i + 1
                j = j - 1
    return flag

str = "A man, a plan, a canal: Panama"
str = "race a car"
print(valid_palindromen(str))
