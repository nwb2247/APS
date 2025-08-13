"""
최소 신장 트리 (minimum spanning tree)
그래프에서 사이클을 제거하고 모든 정점을 연결하는 트리

prim : 정점 중심
kruskal : 간선 중심

prim : 지금까지 완성된 트리에서 최소 비용으로 연결 가능한 정점을 추가시킴
(시작점으로부터의 최소거리였던 dijkstra 와는 다르다)

kruscal : 간선을 가중치 오름차순 정렬하고 하나씩 포함시킬지 확인 (다시 append 하지 않으므로 pq 사용필요 X)
단, 간선의 양끝 정점이 이미 같은 그룹에 있다면 넘어감
이를 확인하기 위해 union find 사용
"""
import sys

# 크루스칼을 이용한 최소신장트리 + 유니온파인드

sys.setrecursionlimit(10 ** 5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로압축
    return parent[x]


def union(x, y):  # y의 root를 x의 root의 부모로 만들어줌
    parent[find(x)] = find(y)


V, E = map(int, input().split())  # 1~V
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
edges.sort(key=lambda x: x[2]) # 가중치 기준 정렬

parent = [i for i in range(V + 1)]  # 초기화

ans = 0
for s, e, w in edges: # 가중치 작은거 부터 꺼내서
    if find(s) == find(e):  # 이미 같은 그룹이면 넘김 (넣으면 사이클 생김)
        continue
    ans += w                # 다른 그룹이면 union하고 가중치 더해줌
    union(s, e)

print(ans)

# # 프림을 이용한 최소신장트리
# from heapq import heappop, heappush
#
# V, E = map(int, input().split())  # 1~V
# adj = [[] for _ in range(V + 1)]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     adj[s].append((w, e))
#     adj[e].append((w, s))
#
# tree = [0]*(V+1) # 트리에 포함이 된 것들
#
# # 임의의 정점으로 시작
# S = 1
#
# pq = []
# heappush(pq, (0, S)) # 임의의 시작정점 S, 완성된 트리로부터 올 수 있는 최소거리
#
# ans = 0
# while pq:
#
#     cw, cnode = heappop(pq)
#     if tree[cnode] == 1:    # 이미 트리에 들어가 있다면 건너뜀 (중복된 정점이 들어갈 수 있고, 트리 들어가고 나서도 남아있을 수 있기때문에)
#         continue
#
#     tree[cnode] = 1         # 꺼낸것이 트리에서 최소 가중치로 접근 가능한 정점이므로 트리에 추가
#
#     ans += cw                # 가중치 더해줌
#
#     for nw, nnode in adj[cnode]:
#         if tree[nnode] == 0:        # 인접한 정점 중 트리에 없는 것을 푸시
#             heappush(pq, (nw, nnode))
#
# print(ans)
