k = list(input('Enter the numbers seperated by space').split())
k = list(map(int, k))
even, odd = list(), list()
for i in k:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even = sorted(even)
odd = sorted(odd, reverse=True)
odd.extend(even)
print(odd)

#CoDeD By AnAnT