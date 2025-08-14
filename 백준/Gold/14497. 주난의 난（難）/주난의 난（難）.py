"""
주난이 파동 4방으로 퍼짐

visited 최소 몇번만에 몇번만에 쓰러지는지

최소 갱신 시 append + 0-1 BFS

시작 끝 좌표 -1씩 해서 받기

"""
from collections import deque

ds = [(1, 0), (0, 1), (0, -1), (-1, 0)]

N, M = map(int, input().split())
sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
arr = [list(input()) for _ in range(N)]

arr[er][ec] = 1
arr[sr][sc] = 0

visited = [[N*M+1]*M for _ in range(N)]
visited[sr][sc] = 0
q = deque()
q.append((sr, sc))

while q:
    cr, cc = q.popleft()

    # 최소값 갱신될 수 있으므로 목표 만났다고 중단하면 안됨
    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<M:
            if visited[cr][cc] + int(arr[nr][nc]) < visited[nr][nc]:  # 최소값 갱신 이뤄질 때만 append
                visited[nr][nc] = visited[cr][cc] + int(arr[nr][nc])
                if arr[nr][nc] == 0:        # 0-1 BFS
                    q.appendleft((nr, nc))
                else:
                    q.append((nr, nc))


print(visited[er][ec])
