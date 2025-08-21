"""
3개의 방화벽 설치가능
N, M이므로 완탐때리기
불위치에는 설치불가

0빈칸
1방화벽
2불

가지치기도 하지말자 일단은
8^3 * (8*8*4)?

정확히 3개 (더 적게도 안됨)
"""
from collections import deque

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

def bfs():
    global ans
    q = deque()
    visited = [[0]*M for _ in range(N)]
    for fr, fc in fireseed:
        visited[fr][fc] = 1
        q.append((fr, fc))

    while q:
        cr, cc = q.popleft()
        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if not oob(nr, nc) and ARR[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    cnt = 0
    for r in range(N):
        for c in range(M):
            if ARR[r][c] == 0 and visited[r][c] == 0:
                cnt += 1

    ans = max(ans, cnt)

    # print(cnt, BL)
    # for l in ARR:
    #     print(*l)
    # print()

def backtrack(depth, start):
    if depth == 3:
        for wr, wc in walls:
            ARR[wr][wc] = 1
        bfs()
        for wr, wc in walls:
            ARR[wr][wc] = 0
        return

    for i in range(start, BL):
        walls[depth] = blanks[i]
        backtrack(depth + 1, i + 1)

N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

fireseed = []
blanks = []
for zr in range(N):
    for zc in range(M):
        if ARR[zr][zc] == 2:
            fireseed.append((zr, zc))
        elif ARR[zr][zc] == 0:
            blanks.append((zr, zc))
BL = len(blanks)

walls = [()] * 3

ans = 0
backtrack(0, 0)
print(ans)

