#Day6 problem 5
def fib(n):
    global fibs
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
fib(50)
sel = []
l = list(input('Enter the numbers separated by space').split())
l = map(int, l)
for i in l:
    if i in fibs:
        sel.append(i)
from itertools import combinations
temp = []
for i in range(2, len(sel)+1):
    temp.extend(list(combinations(sel, i)))
for i in range(len(temp)):
    fin = sum(temp[i])
    if fin in fibs:
        print(temp[i], fin)