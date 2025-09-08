"""
+ 는 90도로 못돌고, 수직, 수평으로만 돌수 있음

항상답이 존재, 가스의 흐름이 유일한 경우만 입력으로 주어짐
M, Z는 하나의 블록으로만 이어져 있고 불필요한 블록이 존재하지 않음

없어진 블록을 추가하면 모든 블록에 가스가 흐름

"""
from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)] #0상 1하 2좌 3우
exits = {"|":[0, 1],
         "-":[2, 3],
         "+":[0, 1, 2, 3],
         "1":[1, 3],
         "2":[0, 3],
         "3":[2, 0],
         "4":[2, 1]}
# for TR in range(R):
#     for TC in range(C):
#         if arr[TR][TC] == "Z":
#             zr, zc = TR, TC
#         elif arr[TR][TC] == "M":
#             mr, mc = TR, TC

# ------------------ 함수 ------------------

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

def check(sr, sc):
    # 추가한 점으로부터 뻗어 나가서 Z, M에 모두 닿으면 True, 그전에 .에 닿으면 False
    # 둘중 하나라도 닿지 못해도 False
    Z, M = False, False

    v, q = [[0 for _ in range(C)] for _ in range(R)], deque()
    v[sr][sc] = 1
    q.append((sr, sc))

    while q:
        cr, cc = q.popleft()
        val = arr[cr][cc]
        if val == "Z":
            Z = True
            continue
        elif val == "M":
            M = True
            continue

        for dr, dc in map(lambda x: ds[x], exits[val]):
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                return False
            if arr[nr][nc] == ".":
                return False
            if arr[nr][nc] in ["|", "-", "+", "1", "2", "3", "4"] and (cr, cc) not in set(map(lambda x: (nr + ds[x][0], nc + ds[x][1]), exits[arr[nr][nc]])):
                return False
            if v[nr][nc] == 1:
                continue
            v[nr][nc] = 1
            q.append((nr, nc))

    if Z and M:
        return True
    else:
        return False

def solve():
    for cr in range(R):
        for cc in range(C):
            if arr[cr][cc] != ".":
                continue
            for st in ["|", "-", "+", "1", "2", "3", "4"]:
                arr[cr][cc] = st
                if check(cr, cc):
                    print(cr+1, cc+1, st)
                    return
                arr[cr][cc] = "."

solve()