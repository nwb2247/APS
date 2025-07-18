import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(range(0,N+1))
for _ in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    arr[i:j+1] = arr[j:i-1:-1]
print(*arr[1:])
