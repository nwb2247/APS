import sys

N = int(sys.stdin.readline())
arr = [False] + [bool(int(x)) for x in sys.stdin.readline().split()]

M = int(sys.stdin.readline())
for _ in range(M) :
    s, n = map(int, sys.stdin.readline().split())
    if s == 1 :
        for i in range(n, N+1, n) :
            arr[i] = not arr[i]
    else :
        i = 0
        while n-i >= 1 and n+i <= N and arr[n-i] == arr[n+i] :
            i += 1
        i -= 1
        for j in range(n-i, n+i+1) :
            arr[j] = not arr[j]
m = N//20
i = 0
for i in range(1, N+1) :
    print(int(arr[i]), end=" ")
    if i%20 == 0 :
        print()