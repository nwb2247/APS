"""

최단 경로 : bfs

1차 시도
    => 모든 벽을 하나씩 깬 상태에서 bfs (시간초과 가능성 있음)
    => 시간초과

2차 시도
    => 0와 붙어있는 1만을 부수길 고려한다면?
    => 시간초과

3차 시도
    => 시작점에서 출발해서 닿게 되는 벽(1)만 고려한다면? (bfs)
    => 시간초과

4차 시도
    => 시작점, 출발점 모두에서 닿게 되는 벽만을 고려
    => 시간초과

5차 시도
    => 시작점, 출발점에서 각각 돌리고, 벽 하나씩 부수면서 연결된 부분에서 합쳐줌 (어자치 벽은 하나만 부술 수 있으므로..)



"""
from collections import deque

ds = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(sr, sc, er, ec, visited):   # 시작, 도착, 거리 배열을 인자로 받음
    global ans
    q = deque()

    visited[sr][sc] = 1       # 시작칸도 셈
    q.append((sr, sc))

    while q:
        cr, cc = q.popleft()

        if (cr, cc) == (er, ec):
            break

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))

    return visited[er][ec]



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
INF = N*M + 1       # 가능한 최대 거리
ans = INF

visited_s = [[-1]*M for _ in range(N)]  # 시작점에서 먼저 출발
ret = bfs(0, 0, N-1, M-1, visited_s)
if ret != -1:
    ans = min(ans, ret)

walls = []                              # 시작점에서 부딪힐 수 있는 벽(1)의 좌표를 추가
for wr in range(N):
    for wc in range(M):
        if arr[wr][wc] == 1:
            for dr, dc in ds:
                nwr, nwc = wr+dr, wc+dc
                if 0<=nwr<N and 0<=nwc<M and visited_s[nwr][nwc] != -1: # 부딪힐 수 있다면
                    walls.append((wr, wc))
                    break

visited_e = [[-1]*M for _ in range(N)]  # 이번엔 도착점에서부터 출발
ret = bfs(N-1, M-1, 0, 0, visited_e)
if ret != -1:
    ans = min(ans, ret)

new_walls = []                          # 시작점에서 부딪혔던 벽들에 대해 도착점에서도 부딪힐 수 있늦지 확인
for wr, wc in walls:
    for dr, dc in ds:
        nwr, nwc = wr + dr, wc + dc
        if 0 <= nwr < N and 0 <= nwc < M and visited_e[nwr][nwc] != -1: # 부딪힐 수 있다면
            new_walls.append((wr, wc))
            break
walls = new_walls                       # 시작점과 도착점에서 모두 부딪힐 수 있는 벽들만 남음

# print(walls)              # walls, visited_s (출발 -> 도착 의 거리들), visited_e (도착 -> 출발 의 거리들) 확인
# for lst in visited_s:
#     print(lst)
# print()
# for lst in visited_e:
#     print(lst)

for wr, wc in walls:                    # 시작점과 도착점에서 모두 부딪힐 수 있는 벽들에 대해서
    mn_s = INF
    mn_e = INF
    for dr, dc in ds:                   # 각각에서 가장 짧은 거리를 확인
        nr, nc = wr+dr, wc+dc
        if 0<=nr<N and 0<=nc<M:
            if visited_s[nr][nc] != -1:
                mn_s = min(mn_s, visited_s[nr][nc])
            if visited_e[nr][nc] != -1:
                mn_e = min(mn_e, visited_e[nr][nc])
    # print(mn_s, mn_e)
    ans = min(ans, mn_s + 1 + mn_e)     # 시작점에서 벽까지 + 1(벽 자체) + 도착점에서 벽까지

if ans != INF:
    print(ans)
else:
    print(-1)