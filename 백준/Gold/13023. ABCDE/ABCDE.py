"""
[조건]
N명이 참가중
0 ~ N-1 인덱싱
같은 친구 관계는 한번만 주어짐

[목표]
A - B - C - D - E 의 친구 관계가 존재하는지

[아이디어]
5명 골라서 서로 친구관계
고른 사람의 친구중에서 방문하지 않은 사람에게 나아가기
depth가 5가 되면 관계가 존재

"""

# def dfs(depth, prev, lll): # 직전까지 고른 친구의 수, 직전에 고른 친구번호
def dfs(depth, prev):  # 직전까지 고른 친구의 수, 직전에 고른 친구번호

    global ans
    if ans == 1:        # 가치치기 (이미 찾았으면 스탑)
        return

    if depth == 5: # 5명 다 골랐다면 종료
        # print(lll)
        ans = 1 # 존재하면 1로 바꿈
        return

    for cur in adj[prev]:   # 친구관계중에
        if visited[cur] == 0:   # 방문하지 않은 사람있다면
            visited[cur] = 1        # 방문하고 다음 사람으로 넘어감
            # dfs(depth+1, cur, lll + [cur])
            dfs(depth + 1, cur)
            visited[cur] = 0


N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*N
ans = 0
for i in range(N):          # 시작 점 정하기
    visited[i] = 1          # 방문처리하고 dfs
    # dfs(1, i, [i])
    dfs(1, i)
    visited[i] = 0
print(ans)