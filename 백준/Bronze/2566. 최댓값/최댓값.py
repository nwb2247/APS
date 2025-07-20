import sys

mat = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
maxVal = -1
r = -1
c = -1
for i in range(9) :
    for j in range(9) :
        if mat[i][j] > maxVal :
            maxVal = mat[i][j]
            r = i+1
            c = j+1
print(maxVal)
print(r, c)