"""
bfs 최소 이동횟수
3칸 내에서만 기물이 있는지 확인하면 된다.
다른 기물은 왕밖에 없으므로 왕의 위치만 확인하자
"""

from collections import deque
ds = [[[-1,0],[-2,-1],[-3,-2]],   # 양 좌표에 -1 곱한것도 확인
      [[-1,0],[-2,1],[-3,2]],
      [[0,1],[1,2],[2,3]],
      [[0,1],[-1,2],[-2,3]]]

R = 10
C = 9
visited = [[-1]*C for _ in range(R)]
sr, sc = map(int, input().split())
kr, kc = map(int, input().split())
visited[sr][sc] = 0
q = deque()
q.append((sr, sc))

while q:
    cr, cc = q.popleft()
    if cr == kr and cc == kc:
        break

    for trail in ds:
        rdest, cdest = trail[-1]
        nr, nc = cr+rdest, cc+cdest
        if 0<=nr<R and 0<=nc<C and visited[nr][nc] == -1:
            for rmid, cmid in trail[:-1]:
                if kr == cr+rmid and kc == cc+cmid:
                    break
            else: #끝이 범위내에 있고, 방문하지 않았고 중간에 다른말 (왕)이 없으면
                visited[nr][nc] = visited[cr][cc]+1
                q.append((nr, nc))

    for trail in ds:
        rdest, cdest = trail[-1]
        nr, nc = cr-rdest, cc-cdest
        if 0<=nr<R and 0<=nc<C and visited[nr][nc] == -1:
            for rmid, cmid in trail[:-1]:
                if kr == cr-rmid and kc == cc-cmid:
                    break
            else: #끝이 범위내에 있고, 방문하지 않았고 중간에 다른말 (왕)이 없으면
                visited[nr][nc] = visited[cr][cc]+1
                q.append((nr, nc))

print(visited[kr][kc])

