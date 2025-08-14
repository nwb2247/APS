"""
다익스트라
"""
from heapq import heappop, heappush

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    pq = []
    heappush(pq, (0, 0, 0)) # 거리, r, c

    dist = [[N*N*10]*N for _ in range(N)]
    dist[0][0] = 0

    while pq:
        curd, cr, cc = heappop(pq)

        if curd > dist[cr][cc]:
            continue

        if (cr, cc) == (N-1, N-1):
            break

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < N and curd + arr[nr][nc] < dist[nr][nc]:
                dist[nr][nc] = curd + arr[nr][nc]
                heappush(pq, (dist[nr][nc], nr, nc))

    print(f"#{tc} {dist[N-1][N-1]}")






# """
# DP -> 오답 (올라왔다가 내려오는 경우가 빠를수도 있음...)
# """
#

#
#     DP = [[0]*N for _ in range(N)]
#
#     for r in range(N):
#         for c in range(N):
#             if (r, c) == (0, 0):
#                 continue
#             mn = N*N*10
#             if r-1 >= 0:
#                 mn = min(mn, DP[r-1][c])
#             if c-1 >= 0:
#                 mn = min(mn, DP[r][c-1])
#             DP[r][c] = mn + arr[r][c]
#
#     print(f"#{tc} {DP[N-1][N-1]}")
#
