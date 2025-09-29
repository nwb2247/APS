"""


"""
from collections import deque

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

def solve():

    origin = 0
    for cr in range(R):
        for cc in range(C):
            if mmap[cr][cc] == "*" or mmap[cr][cc] == "#":
                origin += 1


    q = deque()
    for cr in range(R):
        for cc in range(C):
            if mmap[cr][cc] == "@":
                mmap[cr][cc] = "."
                for dr, dc in ds:
                    for l in range(1, 3):
                        nr, nc = cr + dr*l, cc + dc*l
                        # print((cr, cc), (nr, nc))
                        if oob(nr, nc) or mmap[nr][nc] == "|":
                            break
                        if mmap[nr][nc] == "*" or mmap[nr][nc] == "#":
                            q.append((nr, nc))

    while q:
        cr, cc = q.popleft()

        if mmap[cr][cc] == "*":
            mmap[cr][cc] = "."
            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if oob(nr, nc) or mmap[nr][nc] == "|":
                    continue
                if mmap[nr][nc] == "*" or mmap[nr][nc] == "#":
                    q.append((nr, nc))
        if mmap[cr][cc] == "#":
            mmap[cr][cc] = "*"

        # print(q)
        # print(cr, cc)
        # for l in mmap:
        #     print(*l)
        # print()

    new = 0
    for cr in range(R):
        for cc in range(C):
            if mmap[cr][cc] == "*" or mmap[cr][cc] == "#":
                new += 1
    print(origin-new, new)

    return

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
R, C = map(int, input().split())
mmap = [list(input()) for _ in range(R)]

solve()