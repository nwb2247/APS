"""
내부에 있을때는 회전이 무의미
외부로 나가는 경우에 어떻게 맞닿아 있는지가 중요

현재 초에 따라서 어디로 나가야하는지 결정됨


2
########
###S.###
########
...#E###
#####.##
########
###.####
########
---------
17?

"""

from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def rotate(r, c):
    i = r // 4
    a = r % 4
    j = c // 4
    b = c % 4
    return 4 * i + b, 4 * j + (3 - a)


K = int(input())
R, C = 4 * K, 4 * K
arr = [list(input()) for _ in range(R)]

# for l in arr:
#     print(l)

v = [[[-1 for _ in range(4)] for _ in range(C)] for _ in range(R)]
q = deque()
for tr in range(R):
    for tc in range(C):
        if arr[tr][tc] == "S":
            q.append((tr, tc, 0))  # 0번회전
            v[tr][tc][0] = 0

ans = -1
while q:

    cr, cc, crot = q.popleft()

    if arr[cr][cc] == "E":
        ans = v[cr][cc][crot]
        break

    f = 0

    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if (nr // 4, nc // 4) == (cr // 4, cc // 4):
            if oob(nr, nc):
                continue
            if arr[nr][nc] == "#":
                continue
            if v[nr][nc][(crot+1)%4] != -1:
                continue
            v[nr][nc][(crot + 1) % 4] = v[cr][cc][crot] + 1
            q.append((nr, nc, (crot + 1) % 4))

            # for r in range(R):
            #     for c in range(C):
            #         print(v[r][c][(crot + 1) % 4], end="\t")
            #     print()
            # print()

            if arr[nr][nc] == "E":
                ans = v[nr][nc][(crot + 1) % 4]
                f = 1
                break
            # print(cr, cc, "|", nr, nc)
        if f:
            break
    if f:
        break

    tr, tc = cr, cc
    for _ in range(crot):
        tr, tc = rotate(tr, tc)
    for dr, dc in ds:
        nr, nc = tr+dr, tc+dc
        if oob(nr, nc):
            continue
        if (nr // 4, nc // 4) == (cr // 4, cc // 4):
            continue
        if arr[nr][nc] == "#":
            continue
        if v[nr][nc][1] != -1:
            continue
        v[nr][nc][1] = v[cr][cc][crot] + 1
        q.append((nr, nc, 1))

        # for r in range(R):
        #     for c in range(C):
        #         print(v[r][c][0], end="\t")
        #     print()
        # print()

        # print(cr, cc, "|", tr, tc, "|", nr, nc)
        if arr[nr][nc] == "E":
            ans = v[nr][nc][1]
            f = 1
            break
        if f:
            break
    if f:
        break



    # for r in range(R):
    #     for c in range(C):
    #         print(v[r][c][0], end=" ")
    #     print()

def deb(lst):
    ans = float('inf')
    for n in lst:
        if n != -1:
            ans = min(ans, n)
    if ans != float('inf'):
        return ans
    else:
        return "#"


# for r in range(R):
#     print(*map(deb , v[r]))
#
# for r in range(R):
#     print(v[r])



print(ans)

"""
3
............
............
............
............
....S.......
............
............
............
...E........
............
............
............
"""