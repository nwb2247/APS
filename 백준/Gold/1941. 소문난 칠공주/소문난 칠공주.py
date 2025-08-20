"""
DFS 응용
인접한 블록에서 하나씩 계속 넣기

=> 시작점 하나 넣고 시작, visited처리, 배열에 넣기 등
다음으로 넘어갈때, 원상복구하지 않음. (시작점이 들어간 모든 경우는 확인하였음. 즉 더 확인할 필요 없음)
시작점을 넣고 경우는 모두 시작점이 포함되어 있고, 아닌 것은 모두 포함되어 있지 않음
단, 한 시작점에서 넣은 것중에 중복이 있을 수 잇으므로 처리 필요

"""
DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = 5
K = 7
arr = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
contained = [() for _ in range(K)]

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def backtrack(depth, Y):

    if Y >= 4:
        return

    if depth == K:
        tmp = contained[:] # 깊은 복사
        tmp.sort()
        lst.append(tuple(tmp))
        return

    for cr, cc in contained[:depth]:
        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) : continue
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                contained[depth] = (nr, nc)
                backtrack(depth + 1, Y + (1 if arr[nr][nc] == "Y" else 0))
                visited[nr][nc] = 0
                contained[depth] = 0




cnt = 0
for sr in range(N):
    for sc in range(N):
        visited[sr][sc] = 1
        contained[0] = (sr, sc)
        lst = []
        backtrack(1, 1 if arr[sr][sc] == "Y" else 0)
        cnt += len(set(lst))
print(cnt)




# --------- 백트래킹 풀이 (560ms) --------------
# """
# 이다솜파 4명이상
#
# 25개 중 7개 고르고 (25C7 * (7(v) + 28(e))이므로 ok?
#
# 1. 임도연파 4명 이상이면 가지치기
# 2. 7명 완성되면
#     모두 연결되어 있는지 확인 bfs
# """
# from collections import deque
#
# ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
#
# def bfs():
#     visited = [[0] * 5 for _ in range(5)]  # bfs위한 방문리스트
#     q = deque()
#
#     sr, sc = member[0]
#     visited[sr][sc] = 1  # 시작점 방문 및 큐에 넣기
#     q.append((sr, sc))
#
#     cnt = 0  # (D) 꺼내면서 카운트
#     while q:
#         cr, cc = q.popleft()
#         cnt += 1  # 연결 요소 1추가
#
#         for dr, dc in ds:  # 네 방향에 대해서
#             nr, nc = cr + dr, cc + dc
#             if 0 <= nr < 5 and 0 <= nc < 5 and is_selected[nr][nc] == 1:  # 범위 내에 있고 멤버로 선택되었으며
#                 if visited[nr][nc] == 0:  # 아직 bfs에서 방문하지 않았다면
#                     visited[nr][nc] = 1  # 방문처리하고
#                     q.append((nr, nc))  # 큐에 추가
#
#     if cnt == 7:  # 연결요소가 7이면 True 반환
#         return True
#     else:
#         return False
#
#
# def dfs(depth, start, Y):
#     # depth: 지금까지 몇명 뽑았는지,
#     # start: 이번 멤버는 몇번 부터 뽑을 건지
#     # Y:지금까지 임도연파가 몇명인지
#     global ans
#     if Y >= 4:  # 가지치기 : 임도연파 4명이상이면 불가능
#         return
#
#     if depth == 7:  # 종료조건 : 7명 완성되면
#         if bfs():  # 서로 연결되있는지 확인하고 연결되어있으면 +1
#             ans += 1
#         return
#
#     for i in range(start, 25):  # 좌표를 숫자로 표현,
#         r, c = i // 5, i % 5  # 좌표로 변환
#         member[depth] = (r, c)  # depth번째 멤버 추가
#         is_selected[r][c] = 1  # 멤버로 선택되었음을 표시
#         dfs(depth + 1, i + 1, Y + int(arr[r][c] == "Y"))  # 임도연파면 1추가하고 dfs 재귀 호출
#         is_selected[r][c] = 0  # 복구
#
#
# arr = [list(input()) for _ in range(5)]
# member = [()] * 7  # 뽑힌 멤버
# is_selected = [[0] * 5 for _ in range(5)]  # bfs 위해 좌표로 기록
# ans = 0
# dfs(0, 0, 0)  # 0명 뽑았고, 0부터 뽑을거고, 아직 임도연파 0
# print(ans)