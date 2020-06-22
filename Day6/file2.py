#Problem 6 Day 2

k = [0, 1, 0, 1, 0, 1, 1, 1, 0]
fin = []
for i in k:
    if i == 0:
        fin.insert(0, i)
    elif i ==1:
        fin.append(i)
print(fin)