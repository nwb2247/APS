"""
1. 중첩 조합
조합을 중첩으로 사용
    a) 가능한 땅 중 R + G개 고르기
    b) 고른 땅 R + G 개 중 초록 배양액 G개의 인덱스고르기
그런데 b)는 a)와 독립적으로 수행할 수 있으므로
중첩으로 combinations를 사용하는대신에 ways에 b)의 결과를 담아두자

2. 동시에 배양액 퍼지는 것 구현
빨강으로 먼저 칠하는데, 대신 2로 칠하고 tmp에 이번에 추가된것을 담아두자
그리고 초록으로 칠할때, 2인것이 있으면 꽃으로 추가해주자
이때 꽃이 된것은 즉시 1로 만들어야 한다. (같은 꽃이 여러번 추가되지 않도록)
그리고 다음 빨강을 popleft할때는 꽃이 된것은 퍼지면 안되므로 꽃 된것 확인해주자

"""

from itertools import combinations
from collections import deque

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)


def bfs():
    v = [[0] * M for _ in range(N)]
    flower = [[0] * M for i in range(N)]

    cnt = 0 # 완성되고 flower를 세면 오래걸리므로 추가 될때 미리미리 세어주자
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
        tmp = deque()  # red를 2로 표시했다가 다시 1로 바꿔주기 위해
        while rq:
            cr, cc = rq.popleft()

            if flower[cr][cc] == 1:  # 이전에 꽃이 되었다면 패스
                continue

            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
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
                    if v[nr][nc] == 2:  # 방금 red에서 넣어줬고 꽃이 안됐다면
                        flower[nr][nc] = 1
                        v[nr][nc] = 1  # 꽃이 됐으므로 1로 만들어줌
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

ways = []       # ways로 미리 저장해두기 (전처리)
for sg in combinations(range(R + G), G):
    w = [0] * (R + G)
    for gi in sg:
        w[gi] = 1
    ways.append(w)

ans = 0
for s in combinations(yellows, R + G):
    for w in ways:
        greens = []
        reds = []
        for i in range(R + G):
            r, c = s[i]
            if w[i] == 1:
                greens.append((r, c))
            else:
                reds.append((r, c))
        ans = max(ans, bfs())
print(ans)
