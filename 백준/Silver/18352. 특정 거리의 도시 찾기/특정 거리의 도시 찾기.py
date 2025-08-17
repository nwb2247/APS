"""
모든 도로 거리 1 -> BFS, 단방향
X부터 출발
최단거리 K에 도달했을때 하나씩 세기
K 넘어가면 세는 거 중단하고 멈춤
"""
from collections import deque

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)

ans = []
visited = [-1]*(N+1)
q = deque()

visited[X] = 0
q.append(X)

while q:
    cur = q.popleft()

    if visited[cur] == K:
        ans.append(cur)
    elif visited[cur] > K:
        break

    for nxt in adj[cur]:
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)
