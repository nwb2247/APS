from collections import deque

N, K = map(int, input().split())
L = 100001          # N, K의 최대 가능값
visited = [-1]*L    # 주의 max(N, K) 등으로 하면 1->2->8->7 등 불가

q = deque()
visited[N] = 0
q.append(N)

while q:
    cur = q.popleft()
    if cur == K:        # K 찾았으면 종료
        break
    for nxt in (cur-1, cur+1, 2*cur):
        if 0 <= nxt < L and visited[nxt] == -1:     # 주의 : nxt가 visited 범위 내에 있는지 확인
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
print(visited[K])
