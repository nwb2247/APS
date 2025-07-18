import sys

N = int(sys.stdin.readline())
# cnt = [0]*201
arr = list(map(int, sys.stdin.readline().split()))
# for i in range(N) :
#     cnt[arr[i]+100] += 1
V = int(sys.stdin.readline())
# print(cnt[V]+100])

print(arr.count(V))
