"""
[조건]
N 노드수 M 알고싶은 쌍의 수 / 둘다 1000이하
노브 번호 1부터 N
=> 트리이므로 간선수 N-1

[목표]
두 노드 사이의 거리 출력

[접근]
트리 상 연결된 두 점의 거리는 음수가 아니므로, 두 노드의 (최소거리를 갖게하는) 경로는 유일하다
(불필요한 조상 노드가 까지 들리지 않고 "최소의 노드 수"만 지나가면 됨 => BFS)

플로이드 워셜은 O(N^3)이므로 불가능
BFS는 O((N+E)*M)) => O(V*M) (트리이기 때문에 E(간선의 수) 또한 N에 귀속, N-1) 이므로 가능

[주의사항]

[엣지케이스]
1 1
1 1
-----
0 => 1번 정점만 덩그러니 있는 경우
"""
from collections import deque

def bfs(s, e):
    q = deque()
    visited = [-1]*(N+1) # 같은 정점의 거리가 0, 따라서 초기화는 -1이하 값으로 해주자

    visited[s] = 0
    q.append(s)

    while q:
        cur = q.popleft()
        if cur == e:
            break
        for nxt, w in adj[cur]:
            if visited[nxt] == -1:  # 0아닌 -1 써야함에 주의
                visited[nxt] = visited[cur] + w
                q.append(nxt)
    print(visited[e])

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)] # 1~N
for _ in range(N-1): # 트리이므로 간선수 N-1
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
    adj[e].append((s, w))

for _ in range(M):
    s, e = map(int, input().split())
    bfs(s, e)