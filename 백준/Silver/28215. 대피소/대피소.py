"""
기존에 집 위치 대피소를 설치

K<=3 , K 3이므로 가지치기 없이 마지막에 처리 (가까운집 and 거리 계산)
"""
def cal():
    mx = 0
    for cr, cc in lst:
        nearest = float('inf')
        for zr, zc in selected:
            nearest = min(nearest, abs(cr-zr)+abs(cc-zc))
        mx = max(mx, nearest)
    return mx


def dfs(depth, idx): # 직전까지 선택한 집의 갯수, idx 몇번째 집부터 고려할건지
    global ans
    if depth == K:
        ans = min(ans, cal())
        return

    for s in range(idx, N):
        selected[depth] = lst[s]
        dfs(depth+1, s+1)


N, K = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(N)]
ans = float('inf')
selected = [()]*K
dfs(0, 0)
print(ans)
