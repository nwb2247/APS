from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs():
    visited = [[0] * N for _ in range(N)]

    cnt = 0         # 영역의 개수
    for sr in range(N):     # 시작지점 설정
        for sc in range(N):
            if arr[sr][sc] > h and visited[sr][sc] == 0:   # h보다 크고(즉, h일때 안잠기고) 방문하지 않았다면
                q = deque()     # 각 시작지점마다 q를 초기화
                
                visited[sr][sc] = 1     # 시작지점 방문처리, 큐 삽입
                q.append([sr, sc])
                cnt += 1                # 영역 개수 추가
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ds:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < N:     # 범위 내에 있고
                            if arr[nr][nc] > h and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                q.append([nr, nc])

    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(100):  # 높이가 100인 좌표가 있다면, h:100까지도 고려해야함
    ans = max(ans, bfs())    # 높이가 h일때의 최대영역개수
print(ans)
