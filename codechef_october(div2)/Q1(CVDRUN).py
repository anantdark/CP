# Problem code - CVDRUN (CoDeD By AnAnT)
from sys import stdin
def reader():
    return list(map(int, stdin.readline().strip().split()))

def check_path(no_of_city, jump_length, virus_pos, my_pos):
    for _ in range(no_of_city):
        next_city = (virus_pos+jump_length)%no_of_city
        virus_pos = next_city
        if (next_city==my_pos):
            return ('YES')
    else:
        return ('NO')

if __name__ == "__main__":
    k = []
    no_of_testcases = int(stdin.readline())
    for i in range(no_of_testcases):
        k.append(reader())
    for lst in k:
        print(check_path(*lst))