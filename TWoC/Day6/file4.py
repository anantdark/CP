def sol():
    n = input('Enter the number')
    temp = list(n)
    from itertools import permutations
    k = list(permutations(temp, len(temp)))
    temp = []
    for j in k:
        temp.append(int(''.join(j)))
    temp.sort()
    for i in range(len(temp)):
        try:
            if temp[i] == int(n) and temp[i+1] != int(n):
                print(temp[i+1])
        except:
         print('Sorry, this is the greatest possible number')

if __name__ == '__main__':
    sol()