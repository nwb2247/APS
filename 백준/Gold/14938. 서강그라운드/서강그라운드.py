"""
[조건]
길로 다른 지역과 연결, 양방향 통행
시작지점 중심으로 수색범위내 모든 아이템 습득 가능
지역 번호 1부터 시작

[목표]
최대 개수

[아이디어]
(XXX)
bfs로 각 지점을 시작점으로 해서 수색범위내의 모든 아이템 먹기
(범위 벗어나면 더이상 append()X
=> 다른쪽에서 더 빠르게 도달 가능한 경우 있으므로 BFS 부적절 => 다익스트라 사용해야함




"""

from heapq import *

# (D) bfs아닌 다익스트라 사용해야함 (다른쪽에서 더 빠르게 도달 가능한 경우 있으므로)
def dijkstra(start):
    global ans
    pq = []         # bfs위한 q, visited 생성
    visited = [rng+1]*(N+1)

    visited[start] = 0          # 시작점 방문처리, 큐에 추가
    heappush(pq, (0, start))    # 지금까지의 거리, 정점번호

    cnt = 0         # 아이템 합
    while pq:
        dist, cur = heappop(pq)       # 정점, 현재까지의 거리

        if visited[cur] != dist:
            continue

        if dist > rng:                # (D) rng을 써야 하는데 M을 써버림...
            continue
        else:
            # print(cur, " ", end = "")
            cnt += items[cur]       # 거리 내에 있으면 아이템 추가

        for w, nxt in adj[cur]:            # 인근정점, 거리
            ndist = dist + w
            if ndist < visited[nxt] :   # cur을 거치는 nxt와의 거리가, 현재까지의 최단 거리와 일치한다면
                visited[nxt] = ndist
                heappush(pq, (ndist, nxt))     # 방문하고 큐에 추가 (dist+nl : 현재까지 거리 + 추가 길이)
    # print()
    # print(cnt)
    ans = max(ans, cnt)

N, rng, M = map(int, input().split())
# N: 지역개수, rng: 수색범위 M:길 갯수
items = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, l = map(int, input().split())
    adj[a].append((l, b))
    adj[b].append((l, a))

ans = 0
# 시작점 정하면서 bfs
for i in range(1, N+1):
    dijkstra(i)
print(ans)


