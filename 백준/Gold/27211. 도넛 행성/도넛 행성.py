from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ds = [[1,0],[0,1],[-1,0],[0,-1]]

# arr를 visited 겸용
# visited = [[0]*M for _ in range(N)]

cnt = 0
for sr in range(N):
    for sc in range(M):
        if arr[sr][sc] == 0:
            cnt += 1
            q = deque()
            q.append((sr, sc))
            arr[sr][sc] = 1
            while q:
                cr, cc = q.popleft()
                for dr, dc in ds:
                    nr, nc = cr + dr, cc + dc
                    if nr == -1:
                        nr = N-1
                    elif nr == N:
                        nr = 0
                    if nc == -1:
                        nc = M-1
                    elif nc == M:
                        nc = 0
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = 1
                        q.append((nr, nc))
print(cnt)


