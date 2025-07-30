def dfs(cur, adj, visited):
    visited[cur] = True     # 방문 체크

    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs(nxt, adj, visited)

def solve():
    V = int(input())
    E = int(input())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):         # 무방향 그래프
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    visited = [False] * (V + 1)
    dfs(1, adj, visited)
    print(visited.count(True) - 1) # 시작 정점 제외


solve()
