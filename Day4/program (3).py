fin = dict()
iter = int(input('Enter the number of elements you want to add.'))
for i in range(iter):
    tkey = (input('Enter the key for the dictionary'))
    tvalue = int(input('Enter the value corresponding to the key'))
    fin[tkey] = tvalue
    print('Item added')
k = sorted(fin.items(), key= lambda x: x[1], reverse= True)
print(f'The second largest dictionary value is {k[1][1]} for key {k[1][0]}')

#CoDeD By AnAnT