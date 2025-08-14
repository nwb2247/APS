"""
BFS인데 육각변으로 맞닿아 있음

홀수행 짝수행 마다 위치가 다름

장애물 위치가 주어짐
0, 0에서 N-1, M-1로 이동
"""
from collections import deque

N, M, K = map(int, input().split())

ds = [[(-1,-1),(-1,0),(0,1),(1,0),(1,-1),(0,-1)],  # 짝수행
      [(-1,0),(-1,1),(0,1),(1,1),(1,0),(0,-1)]]  # 홀수행

arr = [[0]*M for _ in range(N)]
for _ in range(K):
    zr, zc = map(int, input().split())
    arr[zr][zc] = 1

# for lst in arr:
#     print(lst)

visited = [[-1]*M for _ in range(N)] # 미방문 -1
q = deque()

# 0으로만 다니고 가중치 1이므로 bfs
visited[0][0] = 0
q.append((0, 0))
while q:
    cr, cc = q.popleft()

    if (cr, cc) == (N-1, M-1):
        break

    for dr, dc in ds[cr%2]:
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and visited[nr][nc] == -1:
            visited[nr][nc] = visited[cr][cc] + 1
            q.append((nr, nc))

# for lst in visited:
#     print(lst)

print(visited[N-1][M-1])

