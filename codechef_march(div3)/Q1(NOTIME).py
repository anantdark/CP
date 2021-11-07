#CoDeD By AnAnT
import sys
n, h, x = map(int, sys.stdin.readline().split())
timezones = list(map(int, sys.stdin.readline().split()))
if x+max(timezones)>= h:
    sys.stdout.write('YES')
else:
    sys.stdout.write('NO')