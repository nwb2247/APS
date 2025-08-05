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

    if visited[K] != -1 and visited[cur] > visited[K]:
        break

    if cur == K:
        cnt += 1

    for nxt in [cur-1, cur+1, cur*2]:
        if 0<=nxt<=L:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
            elif visited[nxt] == visited[cur] + 1:
                q.append(nxt)

print(visited[K])
print(cnt)