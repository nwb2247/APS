"""
[조건]
구역 간 이동의 배터리 사용량 주어짐
다시 사무실(0번)로 돌아와야함
모든 구역을 한번 꼭 돌아야하고 한번씩만 돌아야함
N <= 10

[목표]
최소 소비량 구하기

[아이디어]
N짜리 순열 만들고 마지막에 자기 자신(0)으로 돌아오도록 (종료조건에서 반영하자)
10! (visited 사용하면 10^10)
가지치기 적용 (이미 소비량이 최소 소비량을 넘어선 경우)

"최대값 지정 잘하기"

"""
# def dfs(depth, prev, sm, lll):
def dfs(depth, prev, sm):
    # depth : 몇번 이동했는지, prev : 어디서 왔는지 sm : 그전까지의 소비량 합계
    global ans

    if sm >= ans:   # 가지치기
        return

    if depth == N-1:                          # 종료조건
        # print(lll + [0])
        ans = min(ans, sm+arr[prev][0])     # 0번으로 돌아가는거까지 넣어서 고려
        return

    for i in range(N): # 지금 어디인지
        if visited[i] == 0:
            visited[i] = 1
            # dfs(depth+1, i, sm+arr[prev][i], lll + [i])
            dfs(depth + 1, i, sm + arr[prev][i])
            visited[i] = 0




TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1      # (debug) # 처음에 0도 방문처리해야함 (마지막에만 돌아올것이므로)
    ans = N*100 # 가능한 최대값으로 초기화 (N-1번의 이동 + 1번더 (사무실로 돌아옴))
    # dfs(0, 0, 0, [0])
    dfs(0, 0, 0)
    print(f"#{tc} {ans}")