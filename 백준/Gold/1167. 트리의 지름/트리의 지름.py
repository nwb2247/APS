"""
트리의 지름 :
트리 내 임의의 두 정점 사이의 거리 중 가장 긴 것

한 정점에서 다른 정점의 거리는 최소공통조상(LCA)을 지나는 경로의 거리 (유일)

[조건]
1~V번


[아이디어]

임의의 번호 (1 or V//2 등)을 루트로 삼고, visited 하면서 내려감 (이미 방문한 것은 부모라는 뜻)
나머지는 자식들 (이진 트리 아닐 수 있으므로 자식 2개 이상일 수 있음)

자식이 없을 때까지 내려 갔다가 올라오면서
첫번째로 큰값, 두번째로 큰값 의 합으로 ans 갱신해주고 (현재 정점이 LCA인 경로의 길이)
첫번째로 큰값를 return (조상 정점이 LCA가 되는 경로의 경우를 위해)
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
    for nxt, w in adj[cur]:     # 인접한 정점들에 대해서
        if visited[nxt] == 0:   # 방문하지 않은 정점, 즉 자식이라면
            visited[nxt] = 1    # 방문 처리,
            remain[nxt] -= 1    
            # 부모 cur에게서 자식 nxt로 갔으므로 nxt기준 남아있는 정점 -1 해줌
            # 이때 remain[nxt]가 1이었다면(부모만 있었다면) -1해주면 0이 되므로 종료조건이 됨
            length = dfs(nxt) + w   # nxt로 부터 올라온 경로의 최대값에 cur과 nxt의 거리도 더해줌
            if length >= mx1:       # 첫번째로 큰값, 두번째로 큰 값을 찾음
                mx2 = mx1           # "크거나 같다면" (> 아님에 주의)
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
