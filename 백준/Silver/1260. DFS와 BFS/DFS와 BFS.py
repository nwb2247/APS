from collections import deque

def do_dfs(cur, visited):   # 재귀 함수
    ans_dfs.append(cur)     # ans에 추가
    
    for nxt in adj[cur]:    # 아직 방문 안 한 인접 정점이 있다면 방문처리후 재귀 호출    
        if visited[nxt] == 0:
            visited[nxt] = 1
            do_dfs(nxt, visited)


def dfs():
    visited = [0] * (N + 1)     # dfs 수행을 위한 visited 배열 생성
    visited[V] = 1              # 시작 정점 방문 처리

    do_dfs(V, visited)  # do_dfs : 재귀로 dfs를 수행하는 함수


def bfs():              # 큐를 이용한 방문처리
    q = deque()
    q.append(V)         # 시작 정점 큐 삽입

    visited = [0] * (N + 1)
    visited[V] = 1      # 시작 정점 방문 처리

    while q:
        cur = q.popleft()   # pop하고 ans에 추가
        ans_bfs.append(cur)
        
        for nxt in adj[cur]:    # 아직 방문 안한 정점이 있다면 방문 처리후 큐에 삽입
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
for lst in adj:
    lst.sort()

ans_dfs = []
ans_bfs = []

dfs()   # 재귀를 이용한 dfs
bfs()   # 큐를 이용한 bfs
print(*ans_dfs)
print(*ans_bfs)
