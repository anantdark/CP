# CoDeD By AnAnT

import math
for _ in range(int(input())):
    days = int(input())
    attendance = input()
    present = attendance.count("1")
    total = (present+(120-days))/120
    if (total>=0.75):
        print('YES')
    else:
        print('NO')