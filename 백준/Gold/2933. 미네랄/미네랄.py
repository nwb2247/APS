"""
공중에 떠 있는 미네랄 클러스터는 없으며,
두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다.
클러스터가 떨어질 때,
그 클러스터 각 열의 맨 아래 부분 중 하나가
바닥 또는 미네랄 위로 떨어지는 입력만 주어진다.
"""
from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]



def is_blank(r):
    if r == R:
        return False
    for c in range(C):
        if cave[r][c] == 'x':
            return False
    return True


def bfs(sr, sc):
    q = deque()
    visited = [[0] * C for _ in range(R)]
    q.append([sr, sc])
    visited[sr][sc] = 1

    cluster = []

    c_mx = 0
    c_mn = C

    r_mxs = [0]*C
    r_mns = [R]*C

    while q:
        cr, cc = q.popleft()
        c_mn = min(c_mn, cc)
        c_mx = max(c_mx, cc)
        r_mxs[cc] = max(r_mxs[cc], cr)
        r_mns[cc] = min(r_mns[cc], cr)
        cluster.append([cr, cc])
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                if cave[nr][nc] == 'x':
                    visited[nr][nc] = 1
                    q.append([nr, nc])
    # print(c_mn, c_mx)
    l_mn = R-1
    # print(r_mxs, r_mns)
    for cc in range(c_mn, c_mx+1):
        for cr in range(r_mxs[cc]+1, R):
            if cave[cr][cc] == 'x':
                l_mn = min(l_mn, cr - r_mxs[cc]-1)
                break
        else:
            l_mn = min(l_mn, R-1-r_mxs[cc])

    # print(l_mn, cluster)

    # for cc in range(c_mn, c_mx+1):
    #     for cr in range(r_mxs[cc], -1, -1):
    #         cave[cr+l_mn][cc] = cave[cr][cc]
    #     for cr in range(l_mn-1, -1, -1):
    #         cave[cr][cc] = "."
    for cr, cc in cluster:
        cave[cr][cc] = "."
    for cr, cc in cluster:
        cave[cr+l_mn][cc] = "x"


R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
hs = list(map(int, input().split()))

for i in range(N):
    r = -1
    if i % 2 == 0:
        for c in range(C):
            if cave[R - hs[i]][c] == 'x':
                cave[R - hs[i]][c] = '.'
                r = R - hs[i]
                break
    else:
        for c in range(C - 1, -1, -1):
            if cave[R - hs[i]][c] == 'x':
                cave[R - hs[i]][c] = '.'
                r = R - hs[i]
                break

    for dr, dc in ds:
        sr, sc = r + dr, c + dc
        if 0 <= sr < R and 0 <= sc < C:
            if cave[sr][sc] == 'x':
                bfs(sr, sc)
for lst in cave:
    print("".join(lst))
