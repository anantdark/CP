# Bubble sort
# Swapping two number if first greater than second for n loops
# Time complexity O(n2)
n = int(input())
arr = list(map(int, input().split()))
for _ in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)