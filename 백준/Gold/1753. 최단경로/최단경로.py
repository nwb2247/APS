"""
다익스트라
한 정점(K)에서 다른 모든 정점으로의 최단 경로를 구하기 위한 Greedy 알고리즘

사용조건
음수 가중치 x (그리디의 특성에 의해 음수 가중치엔 적용 불가능)

설명 :
현재까지 방문한 정점(최단 거리가 확정된) 정점들과 연결된 정점들 중에서
아직 방문하지 않은(최단 거리가 확정되지 않은) 정점들 중 K로부터 최소 비용으로 도달가능한 정점 선택, 방문(최단 거리 확정)
매 순간 K로부터 최소 비용으로 도달가능한 정점을 찾고 업데이트하면, K로부터 모든 정점까지의 최단 경로를 구할 수 있다.

참고) 그래프 관련 알고리즘

● 최단 경로 알고리즘(Shortest Path Problem)

플로이드 워셜: 모든 정점 쌍 간 최단 거리 구하는 알고리즘 (음수인 가중치 OK, but 음수 사이클 X)

벨만 포드 	: 다익스트라와 비슷하나 음수 가중치 OK,  (코테엔 잘 나오지 않음)
			  아직 방문 안한 정점들에서 최단 경로를 찾는 다익스트라와 달리 벨만 포드는 매 단계 모든 간선을 전부 확인
			  다익스트라보다 느리고 플로이드 워셜보다 빠름

A*		: 정점의 개수가 너무 많아 다익스트라 적용 어려울 때, 근사적인 최소 거리를 찾는 알고리즘 (코테엔 잘 나오지 않음)


● 최소 신장 트리(MST) 알고리즘
신장 트리 : 모든 정점을 가장 적은 간선 수로 연결한 그래프
최소 신장 트리 : 신장 트리 중에서 사용된 가중치이 합이 최소인 트리

크루스칼 (그리디), 프림

● 위상 정렬
 => DFS

"""

import heapq, sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w,v)) # (가중치, 도착지)
# print(adj)

pq = []
heapq.heappush(pq, (0,K)) # (K와의 거리, 도착지점)

inf = 2**31-1
dist = [inf]*(V+1)
dist[K] = 0

while len(pq) != 0:
    cur_dist, cur_v = heapq.heappop(pq) # dist to K가 가장 작은 것을 꺼냄 (현재까지 방문한 정점들에 인접한...)
    if dist[cur_v] != cur_dist:         # 일종의 visited 역할, 이전에 갱신했던 최소값이 아니라면 이전에 이미 처리된 것이므로 pass
        continue
    for new_w, new_v in adj[cur_v]:     # 인접한 정점과 가중치를 꺼내서
        new_dist = dist[cur_v]+new_w
        if new_dist < dist[new_v]:      # K를 경유했을때 값이 더 작다면
            dist[new_v] = new_dist      # dist를 갱신하고
            heapq.heappush(pq, (new_dist, new_v))   # pq에 추가
print(*map(lambda x:"INF" if x == inf else x, dist[1:]), sep="\n")
