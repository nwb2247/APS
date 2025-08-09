"""
트리의 지름 :
트리 내 임의의 두 정점 사이의 거리 중 가장 긴 것

한 정점에서 다른 정점의 거리는 최소공통조상(LCA)을 지나는 경로의 거리 (유일)

[조건]
1~V번


[아이디어]

임의의 번호 (1 or V//2 등)을 루트로 삼고, visited 하면서 내려감 (이미 방문한 것은 부모라는 뜻)
나머지는 자식들 (이진 트리 아닐 수 있으므로 자식 여럿일 수 있음)

자식이 없을 때까지 내려 갔다가 올라오면서 최대, 차대의 합으로 ans 갱신해주고
최대를 return
"""
import sys
sys.setrecursionlimit(110000)

def dfs(cur):
    global ans
    # 종료조건 : 자식이 없다면
    if remain[cur] == 0:
        return 0

    mx1 = 0     # 최대
    mx2 = 0     # 차대
    for nxt, w in adj[cur]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            length = dfs(nxt) + w
            if length >= mx1:
                mx2 = mx1
                mx1 = length
            elif length >= mx2:
                mx2 = length

    ans = max(ans, mx1+mx2)
    return mx1


V = int(input())
adj = [[] for _ in range(V+1)]
remain = [0]*(V+1)      # 아직 방문하지 않은 인접 정점 수 (0이면 자식이 없다는 뜻)
for _ in range(V):
    v, *info, dummy = map(int, input().split())
    # v : 현재 정점/ info : 마지막 제외 나머지는 인접 정점, 거리 / dummy는 -1
    for i in range(0, len(info), 2):
        adj[v].append((info[i], info[i+1])) # (정점, 거리)
        remain[v] += 1

visited = [0]*(V+1)

root = 1 # 임의로 root를 지정
visited[1] = 1 # (D) : 시작 노드를 방문처리 안함;;;
ans = 0

dfs(root)
print(ans)