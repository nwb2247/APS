"""
[조건]

[목표]

[접근]
위상 정렬?
지어야하는 건물을 시작으로 DFS
다음 노드로 넘어가면서 자기 자신을 더해줌

"""
from collections import deque

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = [-1] + list(map(int, input().split()))
    c_num = [0]*(N+1)
    adj = [[] for _ in range(N + 1)]
    for _ in range(K):
        s, e = map(int, input().split())
        adj[s].append(e)
        c_num[e] += 1
    W = int(input())
    q = deque()
    for i in range(1, N+1):
        if c_num[i] == 0:
            q.append(i)
    time = [0]*(N+1)

    while q:
        cur = q.popleft()
        time[cur] += lst[cur]
        for nxt in adj[cur]:
            time[nxt] = max(time[nxt], time[cur])
            c_num[nxt] -= 1
            if c_num[nxt] == 0:
                q.append(nxt)

    print(time[W])


