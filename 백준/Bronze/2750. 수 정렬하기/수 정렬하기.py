import sys

N = int(sys.stdin.readline())
arr = [0]*N
for i in range(N) :
    arr[i] = int(sys.stdin.readline())
arr.sort()
for i in range(N) :
    print(arr[i])