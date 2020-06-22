#Day6 file 11

lis = list(input('Enter the elements in the list').split())
lis = list(map(int, lis))
for i in range(len(lis)-1):
    for j in range(len(lis)-1):
        if lis[j] > lis[j+1]:
            temp = lis[j]
            lis[j] = lis[j+1]
            lis[j+1] = temp
print(lis)
print('The max value is ', (lis[-1]*lis[-2])*lis[-3])