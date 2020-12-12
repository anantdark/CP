def binary(arr, n, key):
    s = 0;
    e = n;
    while (s<=e):
        mid = (s+e)//2
        if (arr[mid]==key):
            return mid
        elif (arr[mid]<key):
            s = mid+1
        else:
            e = mid-1
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    print(binary(arr, n, key))