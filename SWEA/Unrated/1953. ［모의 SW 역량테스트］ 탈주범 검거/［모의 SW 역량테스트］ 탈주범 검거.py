"""
"""
from collections import deque

ds = [(-1, 0), (0, 1),  (1, 0), (0, -1)] # 상0 우1 하2 좌3
ways = dict()
ways[1] = [0, 1, 2, 3]
ways[2] = [0, 2]
ways[3] = [1, 3]
ways[4] = [0, 1]
ways[5] = [2, 1]
ways[6] = [2, 3]
ways[7] = [0, 3]

def oob(r, c):
    return not (0<=r<R and 0<=c<C)


def connected(cr, cc, nr, nc):
    if arr[nr][nc] == 0:
        return False
    for dr, dc in map(lambda x: ds[x], ways[arr[cr][cc]]):
        tr, tc = cr+dr, cc+dc
        if not oob(tr, tc) and (tr, tc) == (nr, nc):
            break
    else:
        return False

    for dr, dc in map(lambda x: ds[x], ways[arr[nr][nc]]):
        tr, tc = nr + dr, nc + dc
        if not oob(tr, tc) and (tr, tc) == (cr, cc):
            break
    else:
        return False

    return True


TC = int(input())
for tc in range(1, TC+1):
    R, C, sr, sc, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    v = [[0]*C for _ in range(R)]

    q = deque()
    v[sr][sc] = 1 # 항상 터널이 있음이 보장
    q.append((sr, sc))

    cnt = 0
    while q:

        cr, cc = q.popleft()

        if v[cr][cc] > L:
            break

        cnt += 1

        for dr, dc in map(lambda x:ds[x], ways[arr[cr][cc]]):
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if v[nr][nc] != 0:
                continue
            if not connected(cr, cc, nr, nc):        # (D) 단순히 0인게 아니라 연결되었는지가 중요
                continue
            v[nr][nc] = v[cr][cc] + 1
            q.append((nr, nc))

    # for l in v:
    #     print(l)

    print(f"#{tc} {cnt}")




