item = input('Enter the items separated by space.')
lst = item.split()
temp  = []
for i in lst:
    if i not in temp:
        temp.append(i)
print(temp)

#CoDeD By AnAnT