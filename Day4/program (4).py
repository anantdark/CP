iter = int(input('enter the number of items you want to enter.'))
fin = dict()
for i in range(iter):
    dkey = input('Enter the key for dictionary')
    dval = int(input('Enter the value corresponding to the key'))
    fin[dkey] = dval
    print('value added\n')
final = dict()
for key, value in fin.items():
    if value not in final.values():
        final[key] = value
print(final)

#CoDeD By AnAnT