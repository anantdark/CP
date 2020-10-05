# DAY 6 PROBLEM 1

test = input('Enter the string').upper()
count = 0
from collections import Counter
temp = dict(Counter(test))
temp = list(temp.values())
for i in temp:
    if i == 1:
        count += 1
        temp.remove(i)
    elif i%2==0:
        temp.remove(i)
temp.sort()
temp.pop()
count = count + sum(temp)
print('The minimum number of strings to be removed to form a palindrome are\n',count)