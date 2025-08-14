"""
0 시작 N-1 끝

적 시야에 걸리는 곳은 지나갈 수 없음

N 정점 <= 100000
M 간선 <= 300000

양방향, 가중치

시야에 걸리는 곳은 지나갈 수 없음

넥서스 시야 0처리 해주자 (가야하므로)

"""
from heapq import heappop, heappush

N, M = map(int, input().split())

bad = list(map(int, input().split())) # 1이면 bad
bad[N-1] = 0 # 넥서스는 시야에서 보이지만 도달해야하므로 0처리

adj = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))

dist = [float('inf')]*N
dist[0] = 0
pq = []
heappush(pq, (0, 0))

# 시야 있으면 아예 append를 하지말자
while pq:
    curd, curnode = heappop(pq)

    if curnode == N-1:
        break

    if curd != dist[curnode]:
        continue

    for w, nxtnode in adj[curnode]:
        if bad[nxtnode] == 0 and curd + w < dist[nxtnode]:
            dist[nxtnode] = curd + w
            heappush(pq, (dist[nxtnode], nxtnode))

if dist[N-1] == float("inf"):
    print(-1)
else:
    print(dist[N-1])