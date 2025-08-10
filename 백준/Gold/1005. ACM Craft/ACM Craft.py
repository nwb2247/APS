"""
[조건]

[목표]

[접근]
위상 정렬
indegree (나에게 들어오는 정점) 배열 관리
[1] 처음에 q에 indegree가 0인 것들 넣고
[2] q에서 꺼내면서 인접한(나가는 방향) 정점 nxt에 대해 처리하고 indegree[nxt] -= 1
[3] 이 때 indegree[nxt] == 0이 되면 nxt도 큐에 넣어줌

[1] 처음에 q에 indegree가 0인 정점 넣어줌
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    [2] q에서 꺼내면서 인접한(나가는 방향) 정점 nxt에 대해 처리하고 indegree[nxt] -= 1
    cur = q.popleft()
    result.append(cur)
    for nxt in adj[cur]:
        indegree[nxt] -= 1
        [3] 이 때 indegree[nxt] == 0이 되면 nxt도 큐에 넣어줌
        if indegree[nxt] == 0:
            q.append(nxt)

=> 이때 result 길이가 정점의 수와 같지 않다면 사이클이 존재한다는 뜻

시간 복잡도 O(V+E) (정점들이 큐에 한번씩만 들어가고 간선 수 만큼 indegree를 감소하는 연산이 있음)


"""
from collections import deque

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = [-1] + list(map(int, input().split()))

    indegree = [0]*(N+1)
    adj = [[] for _ in range(N + 1)]

    for _ in range(K):
        s, e = map(int, input().split())
        adj[s].append(e)
        indegree[e] += 1

    W = int(input())

    # 큐에 indegree 0인 것들 넣어줌
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    time = [0]*(N+1)    # 하위 건물들의 최대 시간을 관리하기 위한 배열

    while q:
        cur = q.popleft()
        time[cur] += lst[cur]   # 꺼내면서 자기 자신의 시간을 더해줌 (큐에 있었다는 것은 indegree 0, 즉 하위 건물들이 다 지어졌다는 것)
        if cur == W:            # cur == W라면 중단해줘도 됨
            break

        for nxt in adj[cur]:    # 인접한 (나가는) 정점들에 대해서
            time[nxt] = max(time[nxt], time[cur])       # nxt 하위 건물 건설 시간 최대를 갱신
            indegree[nxt] -= 1                          # 하위 건물 하나 지었으므로 indegree[nxt] 감소 시켜줌
            if indegree[nxt] == 0:                      # 감소시켜서 지금 0이 된 상황이면 q에 추가
                q.append(nxt)

    print(time[W])