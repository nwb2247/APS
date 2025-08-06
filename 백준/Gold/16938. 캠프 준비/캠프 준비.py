"""
[조건]
문제 수 N<=15

[목표]
문제 난이도의 합 범위로 주어짐
최대차이 X보다 크도록

[아이디어]
R 조건 가지치기
(L, X 조건은 주가되는 문제에 따라 극복 가능, R는 불가능)
두문제 이상 조건
방법의 수 1씩 추가
문제의 수는 정해져 있지 않음 (powerset)
"""

# def dfs(depth, sm, mn, mx, cnt, lll):
def dfs(depth, sm, mn, mx, cnt):
    # depth : 직전까지 포함여부 검토한 문제 수
    global ans

    if sm > R:  # R 조건으로만 가지치기
        return

    if depth == N:
        if sm >= L and mx - mn >= X and cnt>=2:
            # print(sm, mn, mx, cnt, lll)
            ans += 1  # 합, L조건, 두 문제 이상 모두 만족했다면 ans += 1
        return
    # 포함
    # dfs(depth + 1, sm + lst[depth], min(mn, lst[depth]), max(mx, lst[depth]), cnt + 1, lll + [[lst[depth]], depth])
    dfs(depth + 1, sm + lst[depth], min(mn, lst[depth]), max(mx, lst[depth]), cnt + 1)
    # 미포함
    # dfs(depth + 1, sm, mn, mx, cnt, lll)
    dfs(depth + 1, sm, mn, mx, cnt)


N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
dfs(0, 0, 1000001, 0, 0)
# dfs(0, 0, 100001, 0, 0, [])
print(ans)
