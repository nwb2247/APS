"""
다익스트라
조건 : 음수 가중치 없음 (0이상)

일종의 그리디
방문하지 않은 정점 중, 시작점과의 거리가 최소거리인 정점을 선택한다.

직관적인 이해:
    음수 가중치가 없으니까 "먼저 확정한 정점"을 더 짧게 만들수 없다.
    항상 현재까지 가장 가까운 곳부터 확정하므로, 더 좋은 경로가 발견될 여지가 없다..
"""


N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)] # 인접행렬 (연결 되어 있지 않으면 무한으로 표시), 정점 번호 : 1~N
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

S, E = map(int, input().split())

visited = [0]*(N+1)             # 방문한 정점의 거리 (최단거리가 확정된...)
dist = [float('inf')]*(N+1)     # S에서 다른 모든 정점과의 거리

# 시작점 자기 자신과의 거리는 0
dist[S] = 0
# print(visited)
# print(dist)
# print()

# 다익스트라 시작
while visited[E] == 0:    # E의 최단거리가 확정될때까지 계속 수행

    # [1] 최단거리 확정 되지 않은 정점 중 가장 S와의 거리가 가장 짧은 정점 cur 선택  (dist[cur]은 최단거리 확정)
    mn = float('inf')
    cur = None
    for i in range(1, N+1):
        if visited[i] == 0 and dist[i] < mn:   # 아직 최단거리 확정되지 않은 정점 중 가장 짧은 정점
            cur = i
            mn = dist[i]

    # [2] dist[cur]은 최단거리 확정되었으므로 방문처리
    visited[cur] = 1

    # [3] 선택한 것과 인접한 정점들에 대해서 기존보다 S에 더 짧게 도달할 수 있는 것이 있다면 dist에 갱신해줌
    for w, adj_node in adj[cur]:
        dist[adj_node] = min(dist[adj_node], dist[cur] + w)

    # print(cur, visited)
    # print(dist)
    # print()

print(dist[E])

