# Day 6 file15
lis = list(input('Enter 3 or more elements in the list').split())
lis = list(map(int, lis))
flag = 0
for i in range(len(lis)):
    temp = lis[i]
    t_index = lis.index(temp)
    back =  lis[:t_index]
    front = lis[t_index+1:]
    print(t_index, back, temp, front)
    for j in front:
        if temp > j:
            flag = 1
    for k in back:
        if temp < k:
            flag = 1
    if flag == 0:
        print('The element is',temp)
        exit()
    flag = 0