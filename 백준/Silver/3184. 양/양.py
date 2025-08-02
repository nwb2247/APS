"""
[목표]
. 빈 필드, # 울타리, o앵,  v 늑대
울타리를 지나지 않고 4방으로 움직일 수 있으면 같은 영역
탈출가능한 칸은 영역에 속하지 ㅇ낳음
영역 안의 늑대와 양의 수를 비교해서 많은 쪽만 남김

[조건]
살아남은 양과 늑대의 수를 출력

[엣지케이스]
[접근]
sr, sc 순회하며 영역의 시작점 잡고
BFS를 이용해 내부의 늑대와 양의 수를 카운트, 비교하여 큰쪽만 전체 cnt에 추가

[주의]
양 > 늑대 면 양이 남고
둘이 같거나 양 < 늑대 : 라면 늑대가 남음 (양 <= 늑대)

빈칸(.)이 아니라, v, o 인경우에도 영역이 시작할 수 있어야 함
따라서 넣을때 '.'인지가 아니라, '#'가 아닌지를 확인해야함
"""
from collections import deque


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

visited = [[0]*C for _ in range(R)]

survived_o = 0  # 전체 o의 수 (양)
survived_v = 0  # 전체 v의 수 (늑대)

for sr in range(R):
    for sc in range(C):
        # 비어있고 방문하지 않았다면
        if arr[sr][sc] != '#' and visited[sr][sc] == 0:

            cnt_o = 0
            cnt_v = 0

            # 큐
            q = deque()
            visited[sr][sc] = 1
            q.append((sr, sc))
            while q:
                cr, cc = q.popleft()
                if arr[cr][cc] == 'o': # 양 혹은 늑대인 경우 카운트
                    cnt_o += 1
                elif arr[cr][cc] == 'v':
                    cnt_v += 1
                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<R and 0<=nc<C:
                        if arr[nr][nc] != '#' and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))

            if cnt_o > cnt_v:
                survived_o += cnt_o
            else: # cnt_o <= cnt_v
                survived_v += cnt_v

print(survived_o, survived_v)
