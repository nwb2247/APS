import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0]*(N+1)
for _ in range(M) :
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i, j+1) :
        arr[idx] = k
output = []
for n in range(1,N+1) :
    output.append(str(arr[n]))
print(" ".join(output))