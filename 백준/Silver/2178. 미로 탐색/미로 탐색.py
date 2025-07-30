from collections import deque


def solve():
    dist = [[0] * M for _ in range(N)]  # 미방문을 0으로 표시 (시작칸을 1로 하기 때문에 가능)
    q = deque()                         # bfs

    q.append((0, 0))
    dist[0][0] = 1                      # 시작칸 dist 1로 표시

    while q:
        cr, cc = q.popleft()                    # q에서 다음 정점 꺼냄
        if cr == N - 1 and cc == M - 1:         # 도착지점에 도달했다면
            break
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:   # 4방향에 대해서
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:                 # 범위 안에 있고
                if arr[nr][nc] == 1 and dist[nr][nc] == 0:  # 값이 1이고 dist == 0 (아직 방문하지 않음)이라면
                    dist[nr][nc] = dist[cr][cc] + 1         # 이전에 왔던 점의 dist에 1추가
                    q.append((nr, nc))

    print(dist[N - 1][M - 1])


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

solve()
