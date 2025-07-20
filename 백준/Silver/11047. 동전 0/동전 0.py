import sys, math

N, K = map(int, sys.stdin.readline().split())
arr = [0]*N

for i in range(N) :
    arr[i] = int(sys.stdin.readline())

cnt = 0
for i in range(N-1, -1, -1) :
    cnt += K//arr[i]
    K = K%arr[i]
print(cnt)
