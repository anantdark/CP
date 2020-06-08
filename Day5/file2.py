k = list(input('Enter the numbers seperated by space').split())
k = list(map(int, k))
for i in range(len(k)-1):
    k[i] = max(k[i+1:])
print(k)

#CoDeD By AnAnT