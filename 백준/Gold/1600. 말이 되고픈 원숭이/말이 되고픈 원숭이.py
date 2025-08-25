"""

"""
from collections import deque


monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
horse = [(-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2)]


def oob(r, c):
    return not (0 <= r < H and 0 <= c < W)


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(H)]

v = [[[-1 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

q = deque()
v[0][0][0] = 0
q.append((0, 0, 0))

while q:
    cr, cc, ck = q.popleft()

    if ck < K:
        for dr, dc in horse:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) or arr[nr][nc] == 1:
                continue

            for i in range(ck+2):
                if v[nr][nc][i] != -1 and v[nr][nc][i] <= v[cr][cc][ck] + 1:
                    break
            else:
                v[nr][nc][ck+1] = v[cr][cc][ck] + 1
                q.appendleft((nr, nc, ck+1))

    for dr, dc in monkey:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc) or arr[nr][nc] == 1:
            continue

        for i in range(ck+1):
            if v[nr][nc][i] != -1 and v[nr][nc][i] <= v[cr][cc][ck] + 1:
                break
        else:
            v[nr][nc][ck] = v[cr][cc][ck] + 1 # (D) v[nr][nc][ck]를 v[nr][nc] 로 씀;;
            q.append((nr, nc, ck))

# for l in v:
#     print(v)

ans = float('inf')
for i in range(K+1):
    if v[H-1][W-1][i] != -1 and ans >= v[H-1][W-1][i]:
        ans = v[H-1][W-1][i]

if ans == float("inf"):
    print(-1)
else:
    print(ans)

