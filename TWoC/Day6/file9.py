#Day 6 file 9
l = list(input('Enter the elements separated by space').split())
l = list(map(int, l))
k = int(input('Enter the index of element'))-1
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
print(f'The {k+1}th smallest number in the list is {l[k]}')