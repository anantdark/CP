def checker():
    k = int(input())
    weights = list(map(int, input().split()))
    movement = list(map(int, input().split()))
    frogs = list(zip(weights, movement))
    print(frogs)
    for i in range(k-1):
        if frogs[i][0] > frogs[i+1][0]:
            frogs[i], frogs[i+1] = frogs[i+1], frogs[i]
            print(frogs)
        else:
            pass


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(checker())