"""
[조건]
P[i][j] : i직원 j번 일을 했을 때 성공확률

[목표]
주어진 모든일이 성공할 확률 최대값 구하기

[아이디어]
일단 정수 상태에서 곱계산하고 마지막에 100^N으로 나눠주기 (출력형식도 신경쓰기)
=> X

=> int float의 비교를 많이 해야해서 오히려 더 오래걸림 -> 차라리 처음부터 float으로 계산

가지치기 : 확률이 이미 최대값보다 낮아졌다면 가지치기
(단 100^(depth)로 나눠주고 비교 => 1번 정했다면 100으로 나눔)

"""
def dfs(depth, mul):
    # depth : 정한 사람의 수, mul : 직전까지의 곱
    global ans

    # 가지치기 (이미 확률이 ans보다 작아졌다면 더 커질 순 없으므로)
    if mul <= ans:
        return

    if depth == N:                  # 종료조건 : 모든 사람의 일을 정했다면
        ans = max(ans, mul)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1, mul*arr[depth][i])
            # depth번째 사람이 i번째 일을 하게 하기
            visited[i] = 0

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    ans = 0
    visited = [0]*N
    dfs(0, 1) # 곱해나가므로 1로 시작
    print(f"#{tc} {ans*100:.6f}")