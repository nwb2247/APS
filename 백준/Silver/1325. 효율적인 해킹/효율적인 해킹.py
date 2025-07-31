from collections import deque

# 입력받기
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    e, s = map(int, input().split()) # e가 s를 신뢰한다 : s가 감염되면 e도 감염된다.
    adj[s].append(e)

ans = []    # 정답 리스트
mx = 0      # 해킹 컴퓨터 수
for start in range(1,N+1):    # 주의 N, N+1
    cnt = 0
    q = deque()
    visited = [0]*(N+1)

    visited[start] = 1
    q.append(start)

    while q:
        cur = q.popleft()
        cnt += 1                # 감염되었으므로 += 1
        for nxt in adj[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)

    if cnt > mx:            # mx가 더 큰 값으로 갱신되는 경우 ans도 같이 초기화
        mx = cnt
        ans = [start]
    elif cnt == mx:         # 지금까지의 mx와 같은 경우 ans에 append
        ans.append(start)

ans.sort()
print(*ans)