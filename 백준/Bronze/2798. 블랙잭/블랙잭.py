import sys

N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sol = 0
for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            s = arr[i] + arr[j] + arr[k]
            if s <= X and s > sol :
                sol = s
print(sol)