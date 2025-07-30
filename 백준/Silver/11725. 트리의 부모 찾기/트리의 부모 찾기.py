from collections import deque

N = int(input())    # N : 정점의 수
adj = [[] for _ in range(N+1)] # tree이므로 자식마다 부모로 연결되는 간선 하나씩을 생각해보면 N개의 간선을 가짐

for i in range(N-1): # 어디가 부모고 자식인지 모르기 때문에 무방향 그래프로 받음
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

parent = [-1]*(N+1) # visited 역할 + 부모 기록 (1의 부모는 0으로 적어둠..)

q = deque()
q.append(1)
parent[1] = 0   # 1의 부모는 없지만 q에서 다시 들어가지 않도록 하기 위해 0으로 설정해둠
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if parent[nxt] == -1:   # 아직 부모를 못찾았으면 (즉 아직 방문하지 않았다면)
            parent[nxt] = cur   # cur이 nxt의 부모가 됨
            q.append(nxt)
print(*parent[2:], sep="\n")
