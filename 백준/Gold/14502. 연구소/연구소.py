"""
[2차 풀이]

[이해 및 구상]

새로운 벽은 반드시 3개를 세워야함

0빈칸 1벽 2바이러스

아무 벽도 세우지 않으면 빈칸으로 뻗어나감

안전 영역 -> 바이러스가 퍼지지 않은 빈칸의 수

출력 : 안전영역의 최대 크기
"""
from collections import deque


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C) # (I) 0 <= c 가 아닌 c <= 0 로 적음


def check():
    global ans

    q, v = deque(virus), [[0 for _ in range(C)] for _ in range(R)]
    while q:
        cr, cc = q.popleft()

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) or m[nr][nc] != 0 or v[nr][nc] == 1: # 범위밖이거나 빈칸이 아니거나, 방문한 곳이라면
                continue
            v[nr][nc] = 1
            q.append((nr, nc)) # (I) nr, nc를 넣어줘야하는데 cr, cc를 넣음

    cnt = 0
    for cr in range(R):
        for cc in range(C):
            if m[cr][cc] == 0 and v[cr][cc] == 0:
                cnt += 1 # 빈칸이면서 감염되지 않은 (방문하지 않은) 곳이라면 cnt += 1)

    ans = max(ans, cnt)


    return


def backtrack(depth, start):  # 지금까지 몇개 설치했는지, blanks에서 몇번부터 설치할건지

    if depth == 3:
        check()
        return

    for i in range(start, L):
        cr, cc = blanks[i]
        m[cr][cc] = 1  # 벽세우기
        backtrack(depth + 1, i + 1)
        m[cr][cc] = 0  # 원복

    return


def solve():
    backtrack(0, 0)
    return


def init():
    global L
    # [1] 빈칸 찾기, 바이러스 채우기
    for cr in range(R):
        for cc in range(C):
            if m[cr][cc] == 0:
                blanks.append((cr, cc))
            elif m[cr][cc] == 2:
                virus.append((cr, cc))
    # [2] 빈칸 개수
    L = len(blanks)


ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
R, C = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]
blanks = []
virus = []
L = -1       # 빈칸의 길이
init()

ans = 0
solve()
print(ans)

# -----------------------------------------------------------

# """ 
# [1차 풀이]
#
# 3개의 방화벽 설치가능 
# N, M이므로 완탐때리기
# 불위치에는 설치불가
# 
# 0빈칸
# 1방화벽
# 2불
# 
# 가지치기도 하지말자 일단은
# 8^3 * (8*8*4)?
# 
# 정확히 3개 (더 적게도 안됨)
# """
# from collections import deque
# 
# def oob(r, c):
#     return not (0<=r<N and 0<=c<M)
# 
# def bfs():
#     global ans
#     q = deque()
#     visited = [[0]*M for _ in range(N)]
#     for fr, fc in fireseed:
#         visited[fr][fc] = 1
#         q.append((fr, fc))
# 
#     while q:
#         cr, cc = q.popleft()
#         for dr, dc in DS:
#             nr, nc = cr+dr, cc+dc
#             if not oob(nr, nc) and ARR[nr][nc] == 0 and visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 q.append((nr, nc))
# 
#     cnt = 0
#     for r in range(N):
#         for c in range(M):
#             if ARR[r][c] == 0 and visited[r][c] == 0:
#                 cnt += 1
# 
#     ans = max(ans, cnt)
# 
#     # print(cnt, BL)
#     # for l in ARR:
#     #     print(*l)
#     # print()
# 
# def backtrack(depth, start):
#     if depth == 3:
#         for wr, wc in walls:
#             ARR[wr][wc] = 1
#         bfs()
#         for wr, wc in walls:
#             ARR[wr][wc] = 0
#         return
# 
#     for i in range(start, BL):
#         walls[depth] = blanks[i]
#         backtrack(depth + 1, i + 1)
# 
# N, M = map(int, input().split())
# ARR = [list(map(int, input().split())) for _ in range(N)]
# DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 
# fireseed = []
# blanks = []
# for zr in range(N):
#     for zc in range(M):
#         if ARR[zr][zc] == 2:
#             fireseed.append((zr, zc))
#         elif ARR[zr][zc] == 0:
#             blanks.append((zr, zc))
# BL = len(blanks)
# 
# walls = [()] * 3
# 
# ans = 0
# backtrack(0, 0)
# print(ans)
# 
# 
