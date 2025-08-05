"""
[조건]

[목표]
모든 순열을 사전순으로 출력 (1~N으로 이뤄진)

[접근]
조합
"""
def dfs(depth):    # depth 인덱스 위치
    if depth == N: # 종료조건, 정답처리
        print(*ans)
        return

    for selected in range(1, N+1):
        if visited[selected] == 0:  # 넣지 않은 경우만 넣기
            visited[selected] = 1   # 넣은 경우 방문처리
            ans[depth] = selected   
            dfs(depth+1)
            visited[selected] = 0   # 넣은 경우 다 확인했으면 방문처리 복구

N = int(input())
visited = [0]*(N+1)
ans = [0]*N
dfs(0)