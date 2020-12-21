# Problem code - CHEFEZQ (CoDeD By AnAnT)
def queries():
    answer = []
    for i in range(int(input())):
        n, limit = map(int, input().split())
        mails = list(map(int, input().split()))
        leftover = 0
        day = 0
        for mail in mails:
            mail+=leftover
            leftover = mail-limit
            day += 1
            if leftover<0:
                break
        answer.append(day+(leftover//limit)+1)
    print(*answer, sep='\n')
queries()