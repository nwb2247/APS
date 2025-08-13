"""
지뢰 없는 칸 => 주변에 몇개의 지뢰가 있는지 표시됨.

지뢰 칸 -> 게임 오버

0이면 bfs 계속
0아니면 더 이상 append X

=> r, c 돌면서 이렇게 총몇번을 해야하는지 확인
단, 주변에 지뢰없는 곳 눌러야 한번에 연속적으로 많은 곳 확인 가능

눌렀는데도, 남은 빈칸이 있다면 마지막에 더해줘야함

"""
from collections import deque

def check(r, c):
    cnt = 0
    for dr, dc in ds:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == "*":
            cnt += 1
    return cnt

ds = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    click_cnt = 0 # 몇번 눌렀는지,

    visited = [[-1]*N for _ in range(N)]    # 미방문 : -1, 지뢰 수 기록

    for sr in range(N):
        for sc in range(N):
            if visited[sr][sc] != -1 or \
                    arr[sr][sc] == "*" or \
                    check(sr, sc) > 0: # 방문했거나, 본인이 지뢰거나, 주변에 지뢰가 있다면 패스
                continue

            q = deque()
            q.append((sr, sc))        # 시작점에 대해서 삽입, 방문처리
            visited[sr][sc] = 0       # 주변에 지뢰 없는 곳 선택했으므로 0 넣기
            click_cnt += 1                    # 클릭 횟수 추가
            
            while q:
                cr, cc = q.popleft()

                if visited[cr][cc] > 0: # 지뢰가 주변에 있다면 주변 더이상 append X
                    continue

                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                        visited[nr][nc] = check(nr, nc)
                        q.append((nr, nc))

    # for lst in arr:
    #     print(lst)
    #
    # for lst in visited:
    #     print(lst)

    # 남은 건 클릭시 한칸만 오픈되는 지뢰 -> 오픈 하기
    for sr in range(N):
        for sc in range(N):
            if arr[sr][sc] == "." and visited[sr][sc] == -1:    # 방문하지 않았고, 지뢰가 아니라면
                click_cnt += 1

    print(f"#{tc} {click_cnt}")



                

