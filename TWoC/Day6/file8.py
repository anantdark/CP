#Spiral matrix traversal
matrix = [[1, 2, 3, 4],
          [14, 15, 16, 5],
          [13, 20, 17, 6],
          [12, 19, 18, 7],
          [11, 10, 9, 8]]
m = len(matrix[0])
n = len(matrix)
top = 0
down = n-1
left = 0
right = m-1
dir = 0
while(top<=down and left<=right):
    if dir == 0:
        for i in range(left, right+1):
            print(matrix[top][i], end = ' ')
        top+=1
    elif dir==1:
        for i in range(top, down+1):
           print(matrix[i][right], end = ' ')
        right = right-1
    elif dir==2:
        for i in range(right, left-1, -1):
            print(matrix[down][i], end = ' ')
        down -= 1
    elif dir == 3:
        for i in range(down, top-1, -1):
            print(matrix[i][left], end = ' ')
        left +=1
    dir = (dir+1)%4