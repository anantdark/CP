def anant():
    l = list(input('Enter the elements in the list separated by space').split())
    l = list(map(int, l))
    i = 1
    while True:
        if i not in l:
            print(i)
            break
        else:
            i+=1

if __name__ == '__main__':
    anant()