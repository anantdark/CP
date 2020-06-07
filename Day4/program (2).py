lst = int(input('Enter the number of tuples in the list'))
tp = int(input('Enter the size of tuples'))
finlist = []
for i in range(1, lst+1):
    temp = []
    print(f'Enter the elements for the tuple {i} in the list')
    for j in range(tp):
        a = int(input('Enter the elements in tuple'))
        temp.append(a)
    finlist.append(tuple(temp))
index = int(input('Enter the index for which the tuples will be sorted.'))
finlist.sort(key= lambda x : x[index-1])
print('sorted list according to tuple index is ', finlist)

#CoDeD By AnAnT