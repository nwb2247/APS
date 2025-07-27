import heapq

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
    cur_dist, cur_v = heapq.heappop(pq)
    if dist[cur_v] != cur_dist: # 일종의 visited 역할, 갱신했던 최소값이 아니라면 이전에 이미 처리된 것이므로 pass
        continue
    for new_w, new_v in adj[cur_v]:
        new_dist = dist[cur_v]+new_w
        if new_dist < dist[new_v]:
            dist[new_v] = new_dist
            heapq.heappush(pq, (new_dist, new_v))
print(*map(lambda x:"INF" if x == inf else x, dist[1:]), sep="\n")

