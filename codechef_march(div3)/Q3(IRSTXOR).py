#CoDeD By AnAnT
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        c = int(sys.stdin.readline())
        cdec = bin(c).replace("0b", "")
        a = '1'
        b = '0' + '1'*(len(cdec)-1)
        for j in range(1, len(cdec)):
            if cdec[j] == '1':
                a += '0'
            else:
                a += '1'
        a = int(a, 2)
        b = int(b, 2)
        sys.stdout.write(str(a*b)+'\n')