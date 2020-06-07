lst1 = input('Enter the items for list 1').split()
lst2 = input('Enter the items for list 2').split()
fin = []
for i in lst1:
    if i in lst2:
        fin.append(i)
print(fin)

#CoDeD By AnAnT