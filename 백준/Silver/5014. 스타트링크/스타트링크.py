"""
bfs 최단거리
"""
from collections import deque

F, S, G, U, D = map(int, input().split())

# 인덷스 1부터 시작함 주의
visited = [-1] * (F + 1)
visited[S] = 0
q = deque()
q.append(S)

while q:
    cur = q.popleft()
    if cur == G:
        break

    for nxt in [cur + U, cur - D]:
        if 1 <= nxt <= F and visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
if visited[G] != -1:
    print(visited[G])
else:
    print("use the stairs")
