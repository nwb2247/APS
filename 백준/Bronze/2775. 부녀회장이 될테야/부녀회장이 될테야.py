import sys, math

T = int(sys.stdin.readline())

for _ in range(T) :
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    mat = [[0 for j in range(n+1)] for i in range(k+1)]

    for i in range(1, n+1) :
        mat[0][i] = i

    for i in range(1, k+1) :
        for j in range(1, n+1) :
            mat[i][j] = mat[i][j-1] + mat[i-1][j]

    print(mat[k][n])


