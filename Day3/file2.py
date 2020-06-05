from itertools import permutations

str = input('Enter any string')
perm = permutations(str)
for i in perm:
    print(''.join(i), end = '\n')


#CoDeD By AnAnT