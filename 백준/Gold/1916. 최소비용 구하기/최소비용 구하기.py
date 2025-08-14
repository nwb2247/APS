"""
다익스트라
조건 : 음수 가중치 없음 (0이상)

일종의 그리디
최소거리가 확정되지 않은 정점 중, 시작점과의 거리가 최소거리인 정점을 선택한다.

직관적인 이해:
    음수 가중치가 없으니까 "먼저 확정한 정점"을 더 짧게 만들수 없다.
    항상 현재까지 가장 가까운 곳부터 확정하므로, 더 좋은 경로가 발견될 여지가 없다..
"""


N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)] # 인접리스트, 정점 번호 : 1~N
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

S, E = map(int, input().split())

confirmed = [0]*(N+1)           # 최단거리 확정 여부 (방문 개념과는 차이 있으므로 visited대신 confirmed로 사용)
dist = [float('inf')]*(N+1)     # S에서 다른 모든 정점과의 거리

# 시작점 자기 자신과의 거리는 0
dist[S] = 0

# -------------------------------------------------------------------------------------------------------------
# 간소화한 다익스트라 (confirmed 배열 대신 dist로 확정과 거리 기록 기능을 모두 수행) (주석 제거 ver)
from heapq import heappop, heappush
pq = []
heappush(pq, (0, S))

while pq:

    curdist, cur = heappop(pq)
    if curdist != dist[cur] :
        continue

    if cur == E: # 도착정점을 찾았다면 break
        break

    for w, nxt in adj[cur]:
        if dist[cur] + w < dist[nxt]:
            dist[nxt] = dist[cur] + w
            heappush(pq, (dist[nxt], nxt))

print(dist[E])


# while pq: (주석 있는 ver)
#
#     # [1] 확정되지 않은 정점 중 가장 S와의 거리가 가장 짧은 정점 cur 선택  (이번에 확정될)
#     curdist, cur = heappop(pq)
#     if curdist != dist[cur] : # curdist가 dist[cur] 다르다는 것은(더 큼) 이전에 더 작은 거리 (dist[cur])이 나와서 이미 확정이 된 상태라는 뜻, 더이상 진행하지 않아도 됨
#         continue
#         # (pq를 사용하면 dist의 갱신이 이뤄질때마다 우선순위큐에 들어가므로 여러 개가 들어갈 수 있고, 확정 후에도 남아 있을 수 있음)
#     # [2] 지금 꺼낸 것이 S와의 거리가 가장 짧은 것이므로 dist[cur]이 S->cur의 최단거리임이 확정됨 (그리디)
#     #   => 이미 append할 때 dist[cur]에 최단 거리가 반영되어있으므로 별도 처리 불필요
#
#     if cur == E: # 도착정점을 찾았다면 break
#         break
#
#     # [3] 선택한 것과 인접한 정점들에 대해서 기존보다 S에 더 짧게 도달할 수 있는 것이 있다면 dist에 갱신해줌
#     for w, nxt in adj[cur]:
#         if dist[cur] + w < dist[nxt]: # 아직 확정되지 않았고, cur을 경유함으로써 더 짧은 거리가 가능해졌다면
#             # nxt가 확정되었다면 이미 dist[nxt]가 최단거리이므로 False,
#             # 확정되지 않았어도 확정을 위해선 dist[nxt]보다 더 짧아지는 경우만 넣으면 됨
#             dist[nxt] = dist[cur] + w       # 갱신하고 pq에 넣어줌
#             heappush(pq, (dist[nxt], nxt))
#
# print(dist[E])

# -------------------------------------------------------------------------------------------------------------

# # 우선순위를 이용한 다익스트라
# from heapq import heappop, heappush
# pq = []
# heappush(pq, (0, S))
#
# while pq:
#
#     # [1] 확정되지 않은 정점 중 가장 S와의 거리가 가장 짧은 정점 cur 선택  (이번에 확정될)
#     _, cur = heappop(pq)
#     if confirmed[cur] == 1:
#         continue
#         # 이미 확정되었다면 건너뜀
#         # (pq를 사용하면 dist의 갱신이 이뤄질때마다 우선순위큐에 들어가므로 여러 개가 들어갈 수 있고, 확정 후에도 남아 있을 수 있음)
#
#     # [2] 지금 꺼낸 것이 S와의 거리가 가장 짧은 것이므로 dist[cur]이 S->cur의 최단거리임이 확정됨 (그리디)
#     confirmed[cur] = 1
#
#     if cur == E: # 도착정점을 찾았다면 break
#         break
#
#     # [3] 선택한 것과 인접한 정점들에 대해서 기존보다 S에 더 짧게 도달할 수 있는 것이 있다면 dist에 갱신해줌
#     for w, nxt in adj[cur]:
#         if confirmed[nxt] == 0 and dist[cur] + w < dist[nxt]: # 아직 확정되지 않았고, cur을 경유함으로써 더 짧은 거리가 가능해졌다면
#             dist[nxt] = dist[cur] + w       # 갱신하고 pq에 넣어줌
#             heappush(pq, (dist[nxt], nxt))
#
# print(dist[E])

# -------------------------------------------------------------------------------------------------------------

# # 루프를 이용한 고전적 방식의 다익스트라
# while True:    # E의 최단거리가 확정될때까지 계속 수행
#
#     # [1] 확정되지 않은 정점 중 가장 S와의 거리가 가장 짧은 정점 cur 선택  (이번에 확정될)
#     mn = float('inf')
#     cur = None
#     for i in range(1, N+1):
#         if confirmed[i] == 0 and dist[i] < mn:   # 아직 최단거리 확정되지 않은 정점 중 가장 짧은 정점
#             cur = i
#             mn = dist[i]
#
#     if cur is None: # cur이 None이라는 것은 더 이상 방문하지 않은 노드가 없거나, S로부터 도달할 방법이 없다는 뜻(float('inf')) => while을 종료해야함
#         break
#
#     # [2] 지금 꺼낸 것이 S와의 거리가 가장 짧은 것이므로 dist[cur]이 S->cur의 최단거리임이 확정됨 (그리디)
#     confirmed[cur] = 1
#
#     if cur == E: # 도착정점을 찾았다면 break
#         break
#
#     # [3] 선택한 것과 인접한 정점들에 대해서 기존보다 S에 더 짧게 도달할 수 있는 것이 있다면 dist에 갱신해줌
#     for w, nxt in adj[cur]:              #아직 확정되지 않았고, cur을 경유함으로써 더 짧은 거리가 가능해졌다면
#         if confirmed[nxt] == 0 and dist[cur] + w < dist[nxt]: # 갱신
#             dist[nxt] = dist[cur] + w
#
# print(dist[E])
#
