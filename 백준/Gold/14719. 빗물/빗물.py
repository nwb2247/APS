"""
1차원 BFS
"""
from collections import deque



K, N = map(int, input().split())
origin = list(map(int, input().split()))

def oob(r):
    return not (0<=r<N)

def bfs(sr, res, h):

    q = deque()
    v = [0 for _ in range(N)]
    v[sr] = 1
    q.append(sr)
    pos = []
    while q:
        cr = q.popleft()
        pos.append(cr)

        for dr in [-1, 1]:
            nr = cr+dr
            if oob(nr):
                return []
            if origin[nr] >= h:
                continue
            if v[nr] == 1:
                continue
            v[nr] = 1
            q.append(nr)

    return pos



def solve():
    res = [0 for _ in range(N)] # 확정 빗물 높이
    for sr in range(N):
        if res[sr] != 0:
            continue
        res[sr] = origin[sr]    # 처음엔 일단 원래 높이로 맞춰줌
        for h in range(origin[sr], K + 1):  # 높이 0~K
            lst = bfs(sr, res, h)
            if lst:
                for cr in lst:
                    res[cr] = h
            else:
                break
    return sum(map(lambda x:res[x]-origin[x], range(N)))

print(solve())
