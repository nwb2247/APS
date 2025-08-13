"""
MST

cij = cji
cii = 0

행성 1부터 시작이지만 편의상 0으로 두자 (입력이 인접행렬로 주어지고, 최소비용만 출력하므로 ok)
"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

edges = []

for s in range(N):
    for e in range(s+1, N):
        edges.append((s, e, cost[s][e]))

edges.sort(key=lambda x:x[2]) # 가중치 기준 정렬

ans = 0
parent = [i for i in range(N)]
for s, e, w in edges:
    if find(s) == find(e): # 같은 그룹이면 넣지말기 (사이클생김)
        continue
    ans += w
    union(s, e)

print(ans)

