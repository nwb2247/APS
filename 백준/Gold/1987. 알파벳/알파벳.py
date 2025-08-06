"""
[조건]
1 <= R, C <=20
(0,0)에서 시작
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 알파벳과 달라야함

[목표]
말이 최대 몇칸 이동가능한지 카운트, (시작점 포함)

[접근]
백트래킹
입력 받을때 정수로 치환해서 받음
26짜리 visited 배열을 이용

"""
from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

R, C = map(int, input().split())
arr = [list(map(lambda x: ord(x) - ord("A"), input().rstrip())) for _ in range(R)]

contained = [0] * 26


def dfs(pos, cnt, contained, ans, arr):
    cr, cc = pos
    no_way = 0
    for dr, dc in ds:
        nr, nc = cr + dr, cc + dc
        if (0 <= nr < R and
                0 <= nc < C and
                contained[arr[nr][nc]] == 0):
            contained[arr[nr][nc]] = 1
            dfs((nr, nc), cnt + 1, contained, ans, arr)
            contained[arr[nr][nc]] = 0
        else:
            no_way += 1
    if no_way == 4:
        ans[0] = max(ans[0], cnt)


contained[arr[0][0]] = 1

ans = [0]

dfs((0, 0), 1, contained, ans, arr)
print(ans[0])
