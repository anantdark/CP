def solve(arr):
    a = int(arr[0])

    b = int(arr[1])

    c = int(arr[2])

    for i in range(3, arr.size):

        if (a + b + c) > 1 and (a + b + c) < 2:
            print(a, " ", b, " ", c)

        if (a + b + c) >= 2:

            if a > b and a > c:

                a = int(arr[i])

            else:

            if (b > a and b > c):

                b = int(arr[i])

            else:

                c = int(arr[i])

        else:

            if a < b & & a < c:

                a = int(arr[i])

            else

            if b < a and b < c:

                b = int(arr[i])

            else:

                c = int(arr[i])