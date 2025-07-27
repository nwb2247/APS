from collections import deque

N, M = map(int, input().split())
lst = [0]*101

# 뱀, 사다리 입력
for _ in range(N+M):
    s, e = map(int, input().split())
    lst[s] = e

# visited 사용하여 방문했던 정점 다시 큐에 넣지 않아야 메모리 초과 나지 않음
visited = [False]*101

q = deque()
# 위치, 굴린 횟수
q.append((1, 0))
ans = 0

while len(q) > 0:
    cur, cnt = q.popleft()
    if visited[cur]:
        continue
    visited[cur] = True
    # 뱀, 사다리 적용
    dest = lst[cur] if lst[cur] != 0 else cur
    visited[dest] = True
    # print(cur, dest, cnt)
    if dest == 100:
        ans = cnt
        break
    for i in range(1, 6+1):
        nxt = dest+i
        if nxt <= 100 and not visited[nxt]:
            q.append((nxt, cnt+1))
print(ans)