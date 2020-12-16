# Insertion sort
#  Chose an element and insert it at it's correct place by moving the previous sorted elements forward by one step until the element's place comes, then place the element.

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    current = arr[i]
    for j in range(i-1, -1, -1):
        if current<arr[j]:
            arr[j+1] = arr[j]
    arr[j] = current
print(arr)
