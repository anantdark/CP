#CoDeD By AnAnt
import sys
def checker(seater):
    seater = '0' + seater + '0'
    count = 0
    tval = False
    for i in range(len(seater)):
        if seater[i] == '1':
            tval = True
        elif seater[i] == '0' and tval == True:
            count += 1
            tval = False
    return count
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        seater = sys.stdin.readline()
        sys.stdout.write(str(checker(seater))+'\n')