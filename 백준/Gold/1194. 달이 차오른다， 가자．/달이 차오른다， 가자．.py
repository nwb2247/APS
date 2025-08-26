"""
엣지
1 4
0fF1 nown으로 구별하지 말고 own에 바로 적용
"""
from collections import deque

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

doors = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}
keys = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5}

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
sr, sc = -1, -1

f = 0
for zr in range(N):
    for zc in range(M):
        if arr[zr][zc] == "0":
            sr, sc = zr, zc
            arr[zr][zc] = "."
            f = 1
            break
    if f:
        break

q = deque()
v = [[[0]*(1<<6) for _ in range(M)] for _ in range(N)]

v[sr][sc][0] = 1
q.append((sr, sc, 0, 0))
ans = -1
while q:
    cr, cc, cdist, own = q.popleft()
    # print(cr, cc, cdist, own)
    val = arr[cr][cc]

    if val == "1":
        ans = cdist
        break
    elif val in keys:
        key = keys[val]
        own = own | (1<<key)

    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            continue
        if arr[nr][nc] == "#" or v[nr][nc][own] == 1:
            continue
        if arr[nr][nc] in doors:
            key = doors[arr[nr][nc]]
            if own & (1 << key) == 0:
                continue
        v[nr][nc][own] = 1
        q.append((nr, nc, cdist+1, own))

print(ans)
