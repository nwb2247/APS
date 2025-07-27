import sys
input = sys.stdin.readline

N, M = map(int, input().split())
to_name = [""]*(N+1)
to_num = dict()
for i in range(1, N+1):
    to_name[i] = input().rstrip()
    to_num[to_name[i]] = i
for _ in range(M):
    st = input().rstrip()
    if ord("0") <= ord(st[0]) <= ord("9"):
        print(to_name[int(st)])
    else:
        print(to_num.get(st))