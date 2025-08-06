"""
[조건]
하루에 여러 상담 불가
N+1이 넘는 날에 상담불가

[목표]
받을 금액 맥스

[아이디어]
재귀
1일부터 하도록 padding

"""

def dfs(start, sm): # start 상담 여부 고려 시작일, sm 번돈
    global ans

    # print(start, sm)
    # 종료조건
    if start >= N+1:
        ans = max(ans, sm)
        return

    for i in range(start, N+1): # start~N 까지 고려
        # i일의 상담을 한다면
        end = i+lst[i][0]-1 # (ex) 1일 시작 3일짜리 -> 3일에 종료)
        nstart = end+1      # 다음 상담 가능일 (ex) 1일 시작 3일짜리 -> 4일부터 가능)
        if end<=N:          # N일전에 종료된다면 (N포함)
            dfs(nstart, sm+lst[i][1])   # 다음 상담 가능일, 이번 상담 선택으로 벌게된 돈까지 고려한 총합
        else:               # N일을 초과한다면
            dfs(nstart, sm)             # 다음 상담 가능일만 갱신 (종료되도록)

N = int(input())
# 인덱스 시작일
lst  = [()] + [tuple(map(int, input().split())) for _ in range(N)] # padding
ans = 0
dfs(1, 0) # 1일차부터 상담 여부 고려
print(ans)
