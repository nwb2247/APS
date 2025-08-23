"""
sr, sc로
처음높이 + 1에서 시작해서 여기에 얼마높이의 물을 댈수 있는지 확인

시간복잡도
N*M * N*M * 10 => 62500000

"""
from collections import deque


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)


def check():
    VISITED = [[0] * M for _ in range(N)]
    q = deque()

    pos = []

    VISITED[sr][sc] = 1
    q.append((sr, sc))
    while q:
        cr, cc = q.popleft()
        pos.append((cr, cc))

        for dr, dc in DS:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                return []

            if ARR[nr][nc] < h and VISITED[nr][nc] == 0:
                VISITED[nr][nc] = 1
                q.append((nr, nc))

    return pos



DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
ARR = [list(map(int, input())) for _ in range(N)]
RES = [[-1]*M for _ in range(N)]

for sr in range(N):
    for sc in range(M):
        if RES[sr][sc] != -1:
            continue
        RES[sr][sc] = ARR[sr][sc]
        for h in range(ARR[sr][sc] + 1, 10):
            pos = check()
            if pos:
                for zr, zc in pos:
                    RES[zr][zc] = h
            else:
                break

cnt = 0
for r in range(N):
    # print(RES[r])
    for c in range(M):
        cnt += RES[r][c] - ARR[r][c]
print(cnt)


