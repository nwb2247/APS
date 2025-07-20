import sys, math

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))

for c in sorted_arr :
    print(*c)