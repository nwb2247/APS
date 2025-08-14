"""
BFS 응용 :
[1] 방문 여부가 아닌 최소값 갱신 가능 여부에 따라 인접 정점 append()
[2] 0-1 BFS : 최소값 갱신 횟수를 줄이기 위해 가장 최소에 가까이 갈 수 있는 거를 appendleft()
=>
단, 목표 정점에 도달하더라도, 최소값 갱신이 또 일어날 수 있으므로 완전 탐색이 필요함.
(따라서 정점이 너무 많다면 부적절)
최소값으로 갱신해야하므로, 초기화를 큰값으로 해야함

(다익스트라로 푼다면 목표 정점 도달시 종료 가능)

"""
from collections import deque

L = 200000  # 200000이상으로는 갈 일이 없음
S, E = map(int, input().split())

visited = [100001] * (L + 1)  # 최소값 갱신을 위해 최대치로 초기화해줌 (100000만번 보다 많이 움직일 일은 없음)
q = deque()
visited[S] = 0
q.append(S)

while q:
    cur = q.popleft()
    # 최소값이 더 갱신될 수 있으므로 E를 만났다고 종료해서는 안됨

    if 2 * cur <= L and visited[cur] < visited[2 * cur]: # 2*cur로 가는경우 0초가 걸리므로 가장 먼저 pop이 되게끔 앞쪽에 넣어줌
        visited[2 * cur] = visited[cur]
        q.appendleft(2 * cur)

    if cur + 1 <= L and visited[cur] + 1 < visited[cur + 1]:
        visited[cur + 1] = visited[cur] + 1
        q.append(cur + 1)

    if 0 <= cur - 1 and visited[cur] + 1 < visited[cur - 1]:
        visited[cur - 1] = visited[cur] + 1
        q.append(cur - 1)

print(visited[E])