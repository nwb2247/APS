"""
[조건]
정렬된 상태로 주어짐

[목표]
k개의 수가 주어질 때 6개짜리 집합을 만들기, 조합

[접근]
백트래킹 조합
"""

def dfs(depth, start):
    # ans 몇번째 인덱스에 넣을 것인지 / lst의 몇번째부터 넣을 수 있는지
    if depth == 6:
        print(*ans)
        return

    for i in range(start, N):
        ans[depth] = lst[i]
        dfs(depth+1, i+1)
#

ans = [0]*6

st = input()
while st != "0":
    N, *lst = list(map(int, st.split()))
    dfs(0, 0) # (depth, start)
    print()

    st = input()