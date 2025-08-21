"""

"""
from collections import deque

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
arr_init = [list(map(int, input().split())) for _ in range(N)]
arr = [[x for x in lst] for lst in arr_init]

visited = [[-1 for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = 0
nq = deque()
melt_amount = []
while q:

    while q:
        cr, cc = q.popleft()

        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc): continue
            if visited[nr][nc] == -1:
                if arr[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc]
                    q.append((nr, nc))
                else:
                    visited[nr][nc] = visited[cr][cc] + 1
                    nq.append((nr, nc))

    if not nq:  # 치즈가 없다면 종료
        break

    cnt = 0
    for nr, nc in nq:
        cnt += 1
        arr[nr][nc] = 0
    melt_amount.append(cnt)


    # for l in arr:
    #     print(*l)
    # print()
    #
    # for l in visited:
    #     print(*l)
    # print()
    #
    # print(q)
    # print(nq)

    q, nq = nq, deque()

print(len(melt_amount))
print(melt_amount[-1])

