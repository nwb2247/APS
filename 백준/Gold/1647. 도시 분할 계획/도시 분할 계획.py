"""
MST

단, 연결된 간선 중 가장 큰 가중치 빼주기


"""
import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x]) # 경로압축
    return parent[x]

def union(x, y):
    xr = find(x)
    yr = find(y)
    if xr == yr:
        return
    elif rank[xr] > rank[yr]:
        parent[yr] = xr
    elif rank[xr] < rank[yr]:
        parent[xr] = yr
    else:
        parent[yr] = xr
        rank[xr] += 1


N, M = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    edges.append((w, (s, e)))
edges.sort()

parent = [i for i in range(N+1)]
rank = [1]*(N+1)

sm = 0
mx = 0
for w, (s, e) in edges:
    if find(s) == find(e):
        continue
    union(s, e)
    sm += w
    mx = max(mx, w)

print(sm-mx)
