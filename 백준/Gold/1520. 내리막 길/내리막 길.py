"""
BFS + 위상정렬
양끝에서 BFS로 도달 가능한 부분 확인
서로 겹치는 것이 경우의 수에 포함가능한 것들

겹치는 부분 확인되면 위상정렬
"""
from collections import deque
import sys


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)


DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
sys.setrecursionlimit(10000)
arr = [list(map(int, input().split())) for _ in range(N)]

overlapped = [[0] * M for _ in range(N)]
q = deque()

q.append((0, 0))
overlapped[0][0] = 1

while q:
    cr, cc = q.popleft()

    for dr, dc in DS:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            continue
        if arr[nr][nc] < arr[cr][cc] and overlapped[nr][nc] == 0:
            overlapped[nr][nc] = 1
            q.append((nr, nc))

q.append((N-1, M-1))
overlapped[N - 1][M - 1] = 2
while q:
    cr, cc = q.popleft()

    for dr, dc in DS:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            continue
        if arr[nr][nc] > arr[cr][cc] and overlapped[nr][nc] == 1:
            overlapped[nr][nc] = 2
            q.append((nr, nc))

# for l in VISITED: # 2 가 겹치는 것들
#     print(l)

indegree = [[0]*M for _ in range(N)]

for cr in range(N):
    for cc in range(M):
        if overlapped[cr][cc] != 2:
            continue
        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if overlapped[nr][nc] == 2 and arr[nr][nc] > arr[cr][cc]:
                indegree[cr][cc] += 1

# for l in indegree:
#     print(l)

cnts = [[0]*M for _ in range(N)]
cnts[0][0] = 1

def dfs(cr, cc):

    for dr, dc in DS:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            continue

        if overlapped[nr][nc] == 2 and arr[nr][nc] < arr[cr][cc]:
            indegree[nr][nc] -= 1
            cnts[nr][nc] += cnts[cr][cc]
            if indegree[nr][nc] == 0:
                dfs(nr, nc)

dfs(0, 0)
# for l in cnts:
#     print(l)
print(cnts[N-1][M-1])
