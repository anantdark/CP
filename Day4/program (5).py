cand = list(input('enter the names separated by space').split())
count = dict()
for i in cand:
    temp = (cand.count(i))
    count[i] = temp
count = sorted(count.items(), key = lambda x: x[1], reverse= True)
max = count[0][1]
count = sorted(count)
for i in count:
    if i[1] == max:
        print(f'{i[0]} won the election')
        exit(0)

#CoDeD By AnAnT