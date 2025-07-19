import sys

N, M = map(int, sys.stdin.readline().split())

mat1 = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
mat2 = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for i in range(N) :
    for j in range(M) :
        mat1[i][j] += mat2[i][j]
for i in range(N) :
    print(*mat1[i])