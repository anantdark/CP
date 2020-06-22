#Day6 file10
k = int(input('Enter the number of lists'))
lists = []
for i in range(k):
    temp_list = list(input(f'Enter the elements in list {i+1}\n').split())
    temp_list = list(map(int, temp_list))
    lists.append(temp_list)
print('Your lists are', lists)
fin_list = []
for k in lists:
    fin_list.extend(k)
for j in range(len(fin_list)):
    for i in range(len(fin_list)-1):
        if fin_list[i] > fin_list[i+1]:
            temp = fin_list[i]
            fin_list[i] = fin_list[i+1]
            fin_list[i+1] = temp
print(fin_list)