"""

쿼리마다 트리 내려가면 비효율

트리 만들어가면서, 하부의 정점 수 더해서 올라가고 배열만들어서 저장

"""
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(cur):
    cnts[cur] = 1       # 방문했으면 일단 1추가 (자기자신도 서브트리에 포함)

    if degree[cur] == 0:    # 디그리가 0 즉, 리프라면 리턴
        return

    for nxt in adj[cur]:
        if visited[nxt] == 0:   # 방문하지 않은 인접정점에 대해서
            visited[nxt] = 1    # 재귀 호출 전에 방문 처리
            degree[nxt] -= 1    # 재귀 호출 전에 디그리 1 줄여줌
            dfs(nxt)            # 재귀 호출
            cnts[cur] += cnts[nxt]  # 재귀 호출 완료되어있으면, cnts[nxt] 확정되었으므로 cnts[cur]에 추가


N, R, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]  # 인접리스트
degree = [0]*(N+1)      # 연결된 간선의 수
cnts = [0]*(N+1)        # 아래 정점들의 수
for _ in range(N-1):
    s, e = map(int, input().split())
    adj[s].append(e)    # 인접리스트에 넣고, degree도 추가
    degree[s] += 1
    adj[e].append(s)
    degree[e] += 1
qs = [int(input()) for _ in range(Q)]   # 쿼리

# 재귀 호출하면서 방문처리
visited = [0]*(N+1)
visited[R] = 1
dfs(R)

# 쿼리마다 호출
for q in qs:
    print(cnts[q])
