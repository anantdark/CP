Dictionary = list(input('enter words seperated by space').split())
arr = list(input('enter letters seperated by space').split())
for i in Dictionary:
    letters = list(i)
    temp = arr.copy()
    for i in letters:
        if i not in temp:
            break
        elif i in temp:
            temp.remove(i)
    else:
        print(''.join(letters))

#CoDeD By AnAnT