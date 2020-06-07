from itertools import combinations
lst = []
for i in range(1, int(input('Enter the number of inputs'))+1):
    lst.append(int(input(f'Enter value {i}\n')))
fin = lst.copy()
for i in range(len(lst), 1, -1):
    temp = list(combinations(lst, i))
    for j in range(len(temp)):
        temp[j] = sum(temp[j])
    fin.extend(temp)
counter = 0
while True:
    counter+=1
    if counter not in fin:
        print(f'The number that is not in list and cannot be represented as sum of items in list is {counter}')
        exit()

#CoDeD By AnAnT