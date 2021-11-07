#CoDeD By AnAnT
import sys
def checker(n):
    for i in range(10, 0, -1):
        if n%i==0:
            return i

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(checker(n))