"""
[조건]

[목표]
중복없이 M개 고른 순열 (즉 한번 고른 원소는 다시 고를수 없음), 사전 순 출력
[접근]
백트래킹
"""
def btk(depth):
    if depth == M:      # [1] 종료 조건
        print(*ans)     # 종료 조건에서 정답처리 (출력)
        return
    for num in range(1, N+1):   # 1~N
        if visited[num] == 0:   # 아직 넣지 않은 숫자라면
            visited[num] = 1    # 넣음 표기하고
            ans[depth] = num    # 넣어줌
            btk(depth+1)        # 넣은 후 경우 다 돌았으면
            visited[num] = 0    # 복원 (빼줌)
            # 어차피 ans[depth]는 나중에 덧씌워지므로 수행할 필요 X

N, M = map(int, input().split())

visited = [0]*(N+1)
ans = [0]*M
btk(0)