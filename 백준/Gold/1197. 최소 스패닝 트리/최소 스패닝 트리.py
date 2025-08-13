"""
최소 신장 트리 (minimum spanning tree)
그래프에서 사이클을 제거하고 모든 정점을 연결하는 트리

prim : 정점 중심
kruskal : 간선 중심

prim : 지금까지 완성된 트리에서 최소 비용으로 연결 가능한 정점을 추가시킴
(시작점으로부터의 최소거리였던 dijkstra 와는 다르다)
"""
from heapq import heappop, heappush

V, E = map(int, input().split()) # 1~V
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))

tree = [0]*(V+1) # 트리에 포함이 된 것들

# 임의의 정점으로 시작
S = 1

pq = []
heappush(pq, (0, S)) # 임의의 시작정점 S, 완성된 트리로부터 올 수 있는 최소거리

sm = 0
while pq:

    cw, cnode = heappop(pq)
    if tree[cnode] == 1:    # 이미 트리에 들어가 있다면 건너뜀 (중복된 정점이 들어갈 수 있고, 트리 들어가고 나서도 남아있을 수 있기때문에)
        continue

    tree[cnode] = 1         # 꺼낸것이 트리에서 최소 가중치로 접근 가능한 정점이므로 트리에 추가

    sm += cw

    for nw, nnode in adj[cnode]:
        if tree[nnode] == 0:        # 인접한 정점 중 트리에 없는 것을 푸시
            heappush(pq, (nw, nnode))

print(sm)
