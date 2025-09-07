"""
12*6
RGBPY + 빈칸
입력은 다 떨어져 있는 상태로 줌
동시에 터지는게 있다면 동시에 처리해야함 (BFS를 전부 돌려야함)

12*6으로 한번에 4개씩만 터진다도 연쇄 수 많지 않음

"""

from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
R, C = 12, 6
arr = [list(input()) for _ in range(R)]


# ------------- 함수 ------------------

def dprint():
    for l in arr:
        print(*map(lambda x:x.rjust(2), l))
    print()

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

def explode():
    found = False
    v = [[0 for _ in range(C)] for _ in range(R)]
    for sr in range(R):
        for sc in range(C):
            if arr[sr][sc] == ".":
                continue
            if v[sr][sc] == 1:
                continue

            q = deque()
            v[sr][sc] = 1
            val = arr[sr][sc]
            q.append((sr, sc))

            tmp = []
            while q:
                cr, cc = q.popleft()
                tmp.append((cr, cc)) # 꺼내면 없애줌

                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if oob(nr, nc):
                        continue
                    if arr[nr][nc] != val:
                        continue
                    if v[nr][nc] == 1:
                        continue
                    v[nr][nc] = 1
                    q.append((nr, nc))

            if len(tmp) >= 4:
                found = True
                for cr, cc in tmp:
                    arr[cr][cc] = "."

    return found



def gravity():
    for cc in range(C):
        tmp = []
        for cr in range(R):
            if arr[cr][cc] != ".":
                tmp.append(arr[cr][cc])
        for cr in range(R-1, -1, -1):
            if tmp:
                arr[cr][cc] = tmp.pop()
            else:
                arr[cr][cc] = "."
    return

def solve():
    turn = 0
    while True:
        # print(turn)
        # dprint()
        if not explode():
            return turn # 처음부터 터질게 없다면 turn은 0으로 종료
        gravity()
        turn += 1
# --------------- 실행 ---------------
print(solve())
