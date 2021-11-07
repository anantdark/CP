#CoDeD By AnAnT
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        length = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split(' ')))
        values.sort()
        sequence = 1
        choice = 0
        for value in values:
            if value<=sequence:
                choice += sequence-value
                sequence+=1
            else:
                choice = 0
                break
        if choice%2!=0:
            sys.stdout.write('First\n')
        else:
            sys.stdout.write('Second\n')