import sys, math

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sol = [1]*N
for i in range(N) :
    for j in range(N) :
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1] : sol[i] += 1

print(*sol)