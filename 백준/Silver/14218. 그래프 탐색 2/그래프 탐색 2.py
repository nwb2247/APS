"""
[조건]
정점 N<=1000 간선 M<=100000
Q : 새로 지어질 하나의 도로를 Q번 차례로 출력
M개는 기존의 도로


[목표]
한 도로가 정비될 때마다 각 도시별로 수도를 방문하는데 최소 몇 도시를 방문해야하는지 출력

[접근]
origin 인접리스트에 Q의 각 도로를 하나씩 추가하면서
수도(1)부터 시작하는 BFS를 수행

O((V+E)*Q) => 5000 0000

[주의사항]
1번부터 시작
"""
from collections import deque

def bfs():
    visited = [-1]*(N+1) # 자기 자신과의 거리 0
    q = deque()

    # 수도 추가
    visited[1] = 0
    q.append(1)

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur]+1
                q.append(nxt)

    print(*visited[1:])


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)] # 1~N
for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

Q = int(input())
for _ in range(Q):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
    bfs()