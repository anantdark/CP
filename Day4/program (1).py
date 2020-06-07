k = list()
n = int(input('Enter the number of inputs'))
for i in range(n):
    k.append(input())
k = tuple(k)
find = input('enter the element you want to find')
found = k.count(find)
print(f'The element {find} is repeated {found} times.')

#CoDeD By AnAnT