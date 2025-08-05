"""
K의 최단 거리의 방법 수도 출력해야하므로

cur == K가 아닌
visited[K] != -1 and visited[cur] == visited[K]+1 를 종료 조건으로 한다
(K를 방문했고, K을 방문하는데 걸리는 최소 시간 + 1에 해당하는 정점을 큐에서 꺼냈다면 break

-----

if visited[nxt] == -1:                  # 방문하지 않았다면(아직 최단거리를 찾지 못했다면) 최단 거리를 기록
    visited[nxt] = visited[cur] + 1
    q.append(nxt)
elif visited[nxt] == visited[cur] + 1:  # 최단 거리를 이미 찾았다면, 새로운 nxt도 최단거리일 때 다시 append (꺼내면서 카운트)
    q.append(nxt)

# ex) 5->10->9->18->17 / 5->4->8->16->17
# 18에서 최단거리 찾았더라도, 16에서도 같은 거리로 17 도달 가능하므로 append
# 1 -> 2 시 1*2 => 2 1+1 => 2 등도 마찬가지


"""

from collections import deque

N, K = map(int, input().split())

L = 200000

visited = [-1]*(L+1)
q = deque()

visited[N] = 0
q.append(N)

cnt = 0
while q:
    cur = q.popleft()

    # K를 방문했고, K을 방문하는데 걸린 시간 + 1에 해당하는 정점을 큐에서 꺼냈다면 break
    if visited[K] != -1 and visited[cur] == visited[K]+1: # K를 방문해
        break

    # 꺼냈는데 K라면 count (위에서 visited[cur] == visited[K]+1 break했으므로 반드시 최단 거리임이 보장됨)
    if cur == K:
        cnt += 1

    for nxt in [cur-1, cur+1, cur*2]:
        if 0<=nxt<=L:
            if visited[nxt] == -1:                  # 방문하지 않았다면(아직 최단거리를 찾지 못했다면) 최단 거리를 기록
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
            elif visited[nxt] == visited[cur] + 1:  # 최단 거리를 이미 찾았다면, 새로운 nxt도 최단거리일 때 다시 append (꺼내면서 카운트)
                q.append(nxt)

            # ex) 5->10->9->18->17 / 5->4->8->16->17
            # 18에서 최단거리 찾았더라도, 16에서도 같은 거리로 17 도달 가능하므로 append
            # 1 -> 2 시 1*2 => 2 1+1 => 2 등도 마찬가지

print(visited[K])
print(cnt)