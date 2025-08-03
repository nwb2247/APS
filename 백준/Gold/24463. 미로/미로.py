"""
[조건]
N, M <=2001 홀수
가장자리에 존재하는 .는 시작, 도착 (둘은 이웃하지 않음)
최단 경로에 없다면 @로 표시
성공 가능한 미로만 주어짐

[목표]
최단 경로에 없다면 @로 표시

[접근]
.를 두 구멍의 위치를 일단 찾음
BFS, 처음에 일단 .를 @로 초기화하고,
경로를 기록해두고, 경로의 좌표를 .로 돌려놓음
경로를 기록하기 위해 visited에는 직전 위치를 표시함
(이를 위해 (-2,-2)로 초기화, 시작점은 (-1,-1)로 기록)

[주의사항]
"""
from collections import deque

ds = [[1,0],[0,1],[-1,0],[0,-1]]

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
edgedots = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == ".":
            if r == 0 or c == 0 or r == N - 1 or c == M - 1:
                edgedots.append((r, c))
            arr[r][c] = "@"         # 일단 시작, 도착도 @로 바꿔둠

sr, sc = edgedots[0]
er, ec = edgedots[1]

visited = [[(-2,-2) for _ in range(M)] for _ in range(N)] # 직전 좌표
q = deque()
visited[sr][sc] = (-1,-1)   # 시작점의 전좌표를 -1,-1로 기록
q.append((sr, sc))

while q:
    cr, cc = q.popleft()
    if (cr, cc) == (er, ec):
        break
    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == "@" and visited[nr][nc] == (-2, -2):
            visited[nr][nc] = (cr, cc)
            q.append((nr, nc))

cr, cc = er, ec
while (cr, cc) != (-1, -1): # 아까 시작점의 전좌표를 -1,-1 로 기록해두었음
    arr[cr][cc] = "."
    cr, cc = visited[cr][cc]

for lst in arr:
    print(*lst, sep="")


