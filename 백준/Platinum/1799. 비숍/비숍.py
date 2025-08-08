"""
[조건]
한변 N <= 10
놓을 수 없는 곳 0으로 주어짐
비숍은 대각으로 웁직임

[목표]
비숍 놓을 수 있는 최대 개수 구하기

[접근]
놓을 수 있는 자리 (1인) 리스트를 만들어둔다
대신 같은 대각에 있는 것까리 모아두고 거기서 하나를 고를지 말지 결정
그리고 반대 모양의 대각에서 겹치는지 확인
0~2N-2 -> 2N-1개이므로 가능

(D) 가지치기
    if (2*N-1)-depth + cnt <= ans:
        # 가지치기 (남은 거 넣을수 있어도 ans보다 같거나 작으면 스탑)
        return

"""

def backtrack(depth, cnt):
    # depth : down 중 몇 개 결정했는지 (몇 번째 인덱스 넣을 차롄지)
    # cnt : 지금까지 몇개인지
    global ans

    if (2*N-1)-depth + cnt <= ans:
        # (D) 가지치기 (남은 거 넣을수 있어도 ans보다 같거나 작으면 스탑)
        return

    if depth == 2*N-1:
        ans = max(ans, cnt)
        return

    for cr, cc in down[depth]:
        if up[cr+cc] == 0:
            up[cr+cc] = 1
            backtrack(depth+1, cnt+1)
            up[cr+cc] = 0
    backtrack(depth+1, cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

down = [[] for _ in range(2*N-1)] # 우하향 (r-c)
up = [0]*(2*N-1) # 우상향 (r+c) (0 ~ 2N-2)

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            down[r-c].append((r,c))
# for i, pos in enumerate(down):
#     print(i, pos)

backtrack(0, 0)
print(ans)




