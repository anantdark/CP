#Day 6 program 6
l = list(input('Enter the list separated by space').split())
l = list(map(int, l))
min = l[0]
for i in l:
    if i < min:
        min = i
min = l.index(min)
l1 = l[:min]
l2 = l[min:]

for i in range(len(l2)-1):
    if l2[i] + 1 != l2[i+1]:
        print('The array is not sorted')
        exit()
if len(l1) < 2 and l1[0] < l2[len(l2)-1]:
    print('The array is not sorted')
    exit()
for i in range(len(l1)-1):
    if l1[i] + 1 != l1[i+1]:
        print('The array is not sorted')
        exit()

if len(l2) == len(l):
    print('The array is sorted but not rotated')
else:
    print('The array is sorted and rotated at index', min+1)

#CoDeD By AnAnT