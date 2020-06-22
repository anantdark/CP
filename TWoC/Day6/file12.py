def findMinLength(strList):
    return len(min(arr, key=len))


def allContainsPrefix(strList, str,

                      start, end):
    for i in range(0, len(strList)):

        word = strList[i]

        for j in range(start, end + 1):

            if word[j] != str[j]:
                return False

    return True


def CommonPrefix(strList):
    index = findMinLength(strList)

    prefix = ""  # Our resultant string

    low, high = 0, index - 1

    while low <= high:

        mid = int(low + (high - low) / 2)

        if allContainsPrefix(strList, strList[0], low, mid):

            prefix = prefix + strList[0][low:mid + 1]

            low = mid + 1

        else:

            # Go for the left part

            high = mid - 1

    return prefix


arr = ["geeksforgeeks", "geeks",

       "geek", "geezer"]

lcp = CommonPrefix(arr)

if len(lcp) > 0:

    print ("The longest common prefix is " + str(lcp))

else:

    print ("There is no common prefix")