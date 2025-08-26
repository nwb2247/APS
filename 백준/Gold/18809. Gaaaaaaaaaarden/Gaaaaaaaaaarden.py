from itertools import combinations
from collections import deque

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

def bfs():
    v = [[0]*M for _ in range(N)]
    flower = [[0]*M for i in range(N)]

    cnt = 0
    rq = deque()
    gq = deque()
    for cr, cc in reds:
        rq.append((cr, cc))
        v[cr][cc] = 1
    for cr, cc in greens:
        gq.append((cr, cc))
        v[cr][cc] = 1

    while rq or gq:

        nrq = deque()
        tmp = deque() # red를 2로 표시했다가 다시 1로 바꿔주기 위해
        while rq:
            cr, cc = rq.popleft()

            if flower[cr][cc] == 1: # 이전에 꽃이 되었다면 패스
                continue

            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if oob(nr, nc):
                    continue
                if arr[nr][nc] != 0 and v[nr][nc] == 0:
                    v[nr][nc] = 2
                    nrq.append((nr, nc))
                    tmp.append((nr, nc))

        ngq = deque()
        while gq:
            cr, cc = gq.popleft()

            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc):
                    continue

                if arr[nr][nc] != 0:
                    if v[nr][nc] == 2: # 방금 red에서 넣어줬고 꽃이 안됐다면
                        flower[nr][nc] = 1
                        v[nr][nc] = 1 # 꽃이 됐으므로 1로 만들어줌
                        cnt += 1
                    elif v[nr][nc] == 0:
                        v[nr][nc] = 1
                        ngq.append((nr, nc))

        while tmp:
            nr, nc = tmp.popleft()
            v[nr][nc] = 1

        rq, gq = nrq, ngq

    return cnt

yellows = []
for zr in range(N):
    for zc in range(M):
        if arr[zr][zc] == 2:
            yellows.append((zr, zc))

vs = []
for sg in combinations(range(R+G), G):
    v = [0]*(R+G)
    for gi in sg:
        v[gi] = 1
    vs.append(v)

ans = 0
for s in combinations(yellows, R+G):
    for v in vs:
        greens = []
        reds = []
        for i in range(R+G):
            r, c = s[i]
            if v[i] == 1:
                greens.append((r, c))
            else:
                reds.append((r, c))
        ans = max(ans, bfs())
print(ans)

        