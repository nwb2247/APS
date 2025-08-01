from collections import deque

ds = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
for sr in range(N):
    for sc in range(M):
        if arr[sr][sc] == 1 and visited[sr][sc] == 0:
            cnt += 1
            q = deque()
            q.append((sr, sc))
            visited[sr][sc] = 1

            while q:
                cr, cc = q.popleft()
                for dr, dc in ds:
                    nr, nc = cr + dr, cc + dc
                    # print(nr, nc, arr[nr][nc], visited[nr][nc])

                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q.append((nr, nc))

print(cnt)
