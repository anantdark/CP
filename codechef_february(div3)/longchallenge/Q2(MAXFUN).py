# import itertools
def checker():
    # finvals = list()
    k = int(input())
    nums = list(map(int, input().split()))
    if len(nums)==3:
        return (abs(nums[0]-nums[1])+abs(nums[1]-nums[2])+abs(nums[2]-nums[0]))
    else:
        nums.sort()
        if (nums[1]-nums[0])>(nums[-1]-nums[-2]):
            return (abs(nums[0]-nums[1])+abs(nums[1]-nums[-1])+abs(nums[-1]-nums[0]))
        else:
            return (abs(nums[0]-nums[-2])+abs(nums[-2]-nums[-1])+abs(nums[-1]-nums[0]))
    # combs = set(itertools.combinations(nums, 3))
    # combs = list(combs)
    # for j in range(len(combs)):
    #     tempval = combs[j]
    #     x, y, z = tempval[0], tempval[1], tempval[2]
    #     finvals.append(abs(x-y)+abs(y-z)+abs(x-z))
    return max(finvals)
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(checker())
