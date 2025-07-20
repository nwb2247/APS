import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

sol = 0
for i in range(1, N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            ends = [0, i, j, k, N]
            sum = 0
            for x in range(4) :
                mul = 1
                for m in range(ends[x], ends[x+1]) :
                    mul *= arr[m]
                sum += mul
            sol = max(sol, sum)
print(sol)

