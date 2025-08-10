"""

[접근]

각 빈공간에 대해 bfs 진행하여 (범위의 크기, 범위 id)를 넣고

각 벽에 대해 하나씩 부숴보면서 네방향에 대해 서로 다른 번호라면 범위를 합해줌

"""
from collections import deque

ds = [(1,0),(-1,0),(0,1),(0,-1)]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]  # 범위의 크기, 범위 idx
walls = []

idx = 0
for sr in range(N):
    for sc in range(M):
        if arr[sr][sc] == 1:            # 벽이라면 walls에 넣고 다음 좌표
            walls.append((sr, sc))
            continue
        
        if visited[sr][sc][1] != -1:    # 방문했던 적 있다면 패스하고 다음 좌표
            continue
        
        # 0이고 방문한 적 없는 경우만
        block = []
        q = deque()
        q.append((sr, sc))
        visited[sr][sc][1] = idx
        while q:
            cr, cc = q.popleft()
            block.append((cr, cc))

            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and visited[nr][nc][1] == -1:
                    visited[nr][nc][1] = idx
                    q.append((nr, nc))

        size = len(block)       # 범위의 크기 확인
        while block:
            cr, cc = block.pop()
            visited[cr][cc][0] = size

        idx += 1

ans = [[0]*M for _ in range(N)]

for wr, wc in walls:
    ans[wr][wc] = 1
    sset = set()
    for dr, dc in ds:
        nr, nc = wr+dr, wc+dc
        if 0<=nr<N and 0<=nc<M and visited[nr][nc][1] != -1 and visited[nr][nc][1] not in sset:
            sset.add(visited[nr][nc][1])
            ans[wr][wc] += visited[nr][nc][0]

for lst in ans:     # (D) : 10으로 나눈 나머지를 출력;;;
    print(*map(lambda x: x%10, lst), sep="")




