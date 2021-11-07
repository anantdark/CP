if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        length = int(input())
        values = list(map(int, input().split(' ')))
        maxindex = values.index(max(values))
        part1 = values[:maxindex]
        part2 = values[maxindex+1:]
        try:
            part1index = part1.index(max(part1))
        except:
            part1index = maxindex
        try:
            part2index = part2.index(max(part2))
        except:
            part2index = maxindex
        diff1 = maxindex-part1index
        diff2 = part2index-maxindex
        print(max(diff1, diff2))