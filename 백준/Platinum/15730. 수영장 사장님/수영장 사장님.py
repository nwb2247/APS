"""

"""
from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)


def edge(r, c):
    return r == 0 or r == N - 1 or c == 0 or c == M - 1


def bfs(sr, sc, h):
    pos = []

    v = [[0] * M for _ in range(N)]
    q = deque()

    v[sr][sc] = 1
    q.append((sr, sc))
    pos.append((sr, sc))

    while q:
        cr, cc = q.popleft()

        if edge(cr, cc):
            return []

        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if v[nr][nc] != 0:
                continue
            if arr[nr][nc] < h:
                v[nr][nc] = 1
                q.append((nr, nc))
                pos.append((nr, nc))

    return pos


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = max(map(max, arr))  # 주의 : 테두리 중 max가 아닌 전체중 max로 해야함 10000으로 해도 무관..

res = [lst[:] for lst in arr]
for tr in range(1, N - 1):  # 1, 2 도 OK
    for tc in range(1, M - 1):
        if not edge(tr, tc):
            res[tr][tc] = -1
# for l in res:
#     print(l)

for zr in range(1, N - 1):
    for zc in range(1, M - 1):
        if res[zr][zc] != -1:
            continue
        pos = bfs(zr, zc, arr[zr][zc])
        # print(zr, zc, pos)
        if not pos:
            res[zr][zc] = arr[zr][zc]  # 가능하지 않다면 자기 자신으로 채워줌
            continue

        # not 이 아니라면 일단 가능하다는 뜻
        left, right = res[zr][zc], INF
        good_h = left
        while left <= right:
            mid = (left + right) // 2
            tmp = bfs(zr, zc, mid)
            if tmp:
                left = mid + 1
                good_h = mid
                pos = tmp
            else:
                right = mid - 1

        for cr, cc in pos:
            res[cr][cc] = good_h

# for l in res:
#     print(l)

ans = 0
for r in range(N):
    for c in range(M):
        ans += res[r][c] - arr[r][c]
print(ans)
