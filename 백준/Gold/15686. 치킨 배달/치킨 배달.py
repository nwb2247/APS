"""
[조건]
1,1부터 시작
치킨 거리 - 집과 가장 가까운 치킨집과의 맨해튼 거리
도시의 치킨거리 : 모든 집의 치킨거리의 합
N*N (N<=50 한 변 크기)
M : 남길 시킨집
나머지 모두 폐업
0 빈곳 1 집 2 치킨집

[목표]
M를 골랐을 때 도시의 치킨거리

[접근]
치킨집 좌표와 집 좌표를 리스트로 관리
dfs로 치킨집에서 M개 고르고 치킨거리 계산

가지치기 불가 (치킨집을 선택하는 것에 따라 각 집별 치킨 거리 달라짐)
"""
def citydist():
    sm = 0
    for hr, hc in house:
        mn = 2*N # 최대 집의 치킨거리
        for cr, cc in selected_chicken:
            mn = min(mn, abs(hr-cr) + abs(hc-cc))
        sm += mn
    return sm


def dfs(depth, start):
    # depth : 직전까지 고른 치킨집 수 , start : 포함을 고려할 치킨집의 시작 인덱스
    global ans

    if depth == M:      # M개 치킨집 다 골랐으면 도시별 치킨집 고르고 ans 반영
        ans = min(ans, citydist())
        return

    for selected in range(start, len(chicken)):     # start인덱스부터 depth에 넣을 치킨집 고르기
        selected_chicken[depth] = chicken[selected]
        dfs(depth+1, selected+1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
selected_chicken = [()]*M

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            house.append((r+1, c+1))
        elif arr[r][c] == 2:
            chicken.append((r+1, c+1))
        else:
            continue

ans = 2*N*2*N # 최대 집의 수 * 최대 각 집별 치킨 거리
dfs(0, 0)
print(ans)


