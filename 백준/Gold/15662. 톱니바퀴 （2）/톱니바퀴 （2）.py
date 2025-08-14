from collections import deque

# q.rotate(1) # 시계방향
# q.rotate(-1) # 반시계방향

# N:0 S:1

N = int(input())
arr = [None] + [deque(list(map(int, input()))) for _ in range(N)]
# for lst in arr:
#     print(lst)
# 0번이 맨 위, 2오른쪽, 6왼쪽

K = int(input())
ops = [tuple(map(int, input().split())) for _ in range(K)]

for idx, d in ops:
    ds = [0]*(N+1)
    ds[idx] = d

    for i in range(idx, 1, -1):
        if arr[i][6] != arr[i-1][2]:
            ds[i-1] = (-1)*ds[i]
        else:
            break

    for i in range(idx, N):
        if arr[i][2] != arr[i+1][6]:
            ds[i+1] = (-1)*ds[i]
        else:
            break

    for i in range(1, N+1):
        arr[i].rotate(ds[i])


print(sum(map(lambda x:x[0], arr[1:])))
