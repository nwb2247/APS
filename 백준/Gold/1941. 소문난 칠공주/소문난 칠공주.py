"""
이다솜파 4명이상

25개 중 7개 고르고 (25C7 * (7(v) + 28(e))이므로 ok?

1. 임도연파 4명 이상이면 가지치기
2. 7명 완성되면
    모두 연결되어 있는지 확인 bfs
"""
from collections import deque

ds = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():
    visited = [[0]*5 for _ in range(5)] # bfs위한 방문리스트
    q = deque()
    
    sr, sc = member[0]
    visited[sr][sc] = 1     # 시작점 방문 및 큐에 넣기
    q.append((sr, sc))

    cnt = 0 # (D) 꺼내면서 카운트
    while q:
        cr, cc = q.popleft()
        cnt += 1            # 연결 요소 1추가

        for dr, dc in ds:               # 네 방향에 대해서
            nr, nc = cr+dr, cc+dc
            if 0<=nr<5 and 0<=nc<5 and is_selected[nr][nc] == 1:        # 범위 내에 있고 멤버로 선택되었으며
                if visited[nr][nc] == 0:                                # 아직 bfs에서 방문하지 않았다면
                    visited[nr][nc] = 1                                 # 방문처리하고
                    q.append((nr, nc))                                  # 큐에 추가

    if cnt == 7:                                                        # 연결요소가 7이면 True 반환
        return True
    else:
        return False


def dfs(depth, start, Y):
    # depth: 지금까지 몇명 뽑았는지, 
    # start: 이번 멤버는 몇번 부터 뽑을 건지
    # Y:지금까지 임도연파가 몇명인지
    global ans
    if Y >= 4:  # 가지치기 : 임도연파 4명이상이면 불가능
        return

    if depth == 7:  # 종료조건 : 7명 완성되면
        if bfs():   # 서로 연결되있는지 확인하고 연결되어있으면 +1
            ans += 1
        return

    for i in range(start, 25):  # 좌표를 숫자로 표현, 
        r, c = i//5, i%5        # 좌표로 변환
        member[depth] = (r, c)  # depth번째 멤버 추가
        is_selected[r][c] = 1   # 멤버로 선택되었음을 표시
        dfs(depth+1, i+1, Y + int(arr[r][c] == "Y"))    # 임도연파면 1추가하고 dfs 재귀 호출
        is_selected[r][c] = 0                           # 복구


arr = [list(input()) for _ in range(5)]
member = [()]*7                             # 뽑힌 멤버
is_selected = [[0]*5 for _ in range(5)]     # bfs 위해 좌표로 기록
ans = 0
dfs(0, 0, 0)                                # 0명 뽑았고, 0부터 뽑을거고, 아직 임도연파 0
print(ans)