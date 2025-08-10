"""
엣지 케이스
6 5 1
00000
11110
00000
11111
01111
00000

visited 관리를 위해 N*M*K 만들면 메모리 초과
대신 K가 10이하이므로 비트마스킹 사용하자

"""

from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

q = deque()
visited = [[0]*M for _ in range(N)]
# 비트마스킹을 이용해 각 벽 부순 횟수에 대해서 방문한 적 있는지 확인
# 최단 거리는 큐에 꺼내면서 확인 (닿을수만 있다면 가장 먼저 N-1, M-1에 도달하는 것이 최단 거리)

visited[0][0] = 1
q.append((0, 0, 1, 0))  # sr, sc, dist, 벽 부순 횟수 (k==K면 더이상 부술 수 없음)

ans = -1
while q:
    cr, cc, dist, k = q.popleft()

    if (cr, cc) == (N-1, M-1):  # 가장 먼저 도달하는 것이 가장 짧은 거리
        ans = dist
        break

    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if 0<=nr<N and 0<=nc<M:         # 범위 내에 있고,
            if arr[nr][nc] == 0 and visited[nr][nc] & 1<<k == 0:    # 빈칸이고, 현재 부순 횟수 k 에 대해 방문한 적 없다면
                visited[nr][nc] = visited[nr][nc] | 1<<k            # k번에 대해 방문처리해주고 큐에 넣어줌
                q.append((nr, nc, dist + 1, k))                     
            if arr[nr][nc] == 1 and k < K and visited[nr][nc] & 1<<(k+1) == 0:  # 벽이고, k+1에 대해 방문한 적 없다면
                visited[nr][nc] = visited[nr][nc] | 1<<(k+1)                    # k+1에 대해 방문처리해주고 k+1상태로 큐에 넣어줌
                q.append((nr, nc, dist + 1, k + 1))

print(ans)
