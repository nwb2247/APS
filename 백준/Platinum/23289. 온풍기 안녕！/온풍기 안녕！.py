"""
R*C
    [송풍] => BFS?
    벽있으면 안되기도 함 (조건 확인)

    [조정]
    동시에
    벽이 있으면 X
    온도의 "차이" // 4

    [-1씩 감소]
    가장 바깥쪽 온도가 1씩 감소

    [초콜릿 먹음]

    [조사하려는 모든 칸의 온도가 K 이상인지 검사]

- 온풍기 하나 이상
- 조사하는 칸 하나 이상
- 입력 좌표들 -1로 받는다.
- 온풍기가 있는 칸과 바람이 나오는 방향에 있는칸 (5) 사이에는 벽이 없다. + 칸이 항상 존재한다. (벽이 아님)
- 같은 벽은 두번 주지 않음,
- 벽은 유효하게 주어줌 (벽 나가지 않음)


[출력]
먹은 초콜릿의 개수 세기
초코 개수가 100 넘어가면 101 출력

[시간 복잡도]
1000*R*C

[예상 엣지]
벽, 온풍기 있는 칸도 상승, 벽있으면 조절 안됨, 차이//4
"""
from collections import deque

# ------------------------- 입력 ---------------------------

ds = [None, (0, 1), (0, -1), (-1, 0), (1, 0)] # 1우 2좌 3상 4하

R, C, K = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(R)]
heaters = []    # 온풍기 (r, c, 방향)
targets = []    # 조사해야하는 칸
for ZR in range(R):
    for ZC in range(C):
        if ARR[ZR][ZC] == 5:
            targets.append((ZR, ZC))
        elif 1 <= ARR[ZR][ZC] <= 4:
            heaters.append((ZR, ZC, ARR[ZR][ZC]))

W = int(input())
walls = [[[0 for _ in range(5)] for _ in range(C)] for _ in range(R)] # 상하좌우의 벽
for _ in range(W):
    A, B, TT = map(int, input().split())
    x, y = A - 1, B - 1
    if TT == 0: # (x, y)의 위, (x-1, y)의 아래 즉 가로모양 벽, 위아래를 막음
        walls[x][y][3] = 1
        walls[x-1][y][4] = 1
    else: # t==1 (x, y)의 오른쪽, (x, y+1)의 왼쪽 즉 세로모양 벽, 좌우를 막음
        walls[x][y][1] = 1
        walls[x][y+1][2] = 1

# ---------------------- 자료 ----------------------------

# ds = [None, (0, 1), (0, -1), (-1, 0), (1, 0)] # 1우 2좌 3상 4하
m = [[0 for _ in range(C)] for _ in range(R)] # 현재 온도
# R, C, K = map(int, input().split())   # R, C, 조사칸 K도 이상이어야함
# heaters = []                          # 온풍기 (r, c, 방향)
# targets = []                          # 조사해야하는 칸
# W = int(input())
# walls = [[[0 for _ in range(5)] for _ in range(C)] for _ in range(R)] # 우좌상하의 벽
sides = [None, [3, 4], [3, 4], [1, 2], [1, 2]]

# ----------------------- 함수화 -------------------------


def dprint():

    for l in m:
        print(*map(lambda x:str(x).rjust(4), l))
    for zr in range(R):
        for zc in range(C):
           print( "".join(map(lambda x:str(x), walls[zr][zc][1:])), end = " ")
        print()
    print()


def oob(r, c):
    return not (0<=r<R and 0<=c<C)

def wind():
    added = [[0 for _ in range(C)] for _ in range(R)]
    for br, bc, d in heaters:
        q, v = deque(), set()
        dr, dc = ds[d]
        sr, sc = br+dr, bc+dc # 5가 칠해질 곳
        v.add((sr, sc))
        q.append((sr, sc, 5))
        while q:
            cr, cc, a = q.popleft()
            if a == 0:
                continue
            added[cr][cc] += a

            # 정면
            nr, nc = cr+dr, cc+dc
            if walls[cr][cc][d] == 0 and not oob(nr, nc) and (nr, nc) not in v:
                v.add((nr, nc))
                q.append((nr, nc, a-1))

            # 대각
            for nd in sides[d]:
                zr, zc = cr+ds[nd][0], cc+ds[nd][1]
                if walls[cr][cc][nd] == 0 and not oob(zr, zc) and walls[zr][zc][d] == 0:
                    nr, nc = zr+dr, zc+dc
                    if not oob(nr, nc) and (nr, nc) not in v:
                        v.add((nr, nc))
                        q.append((nr, nc, a-1))

    for cr in range(R):
        for cc in range(C):
            m[cr][cc] += added[cr][cc]

    return

def adjust():

    nm = [[0 for _ in range(C)] for _ in range(R)]
    for cr in range(R):
        for cc in range(C):
            val = m[cr][cc]
            for cd in range(1, 5):
                dr, dc = ds[cd]
                nr, nc = cr+dr, cc+dc
                if oob(nr, nc) or m[nr][nc] >= m[cr][cc] or walls[cr][cc][cd] == 1:
                    continue
                nm[nr][nc] += (m[cr][cc] - m[nr][nc])//4
                val -= (m[cr][cc] - m[nr][nc])//4
            nm[cr][cc] += val

    for cr in range(R):
        for cc in range(C):
            m[cr][cc] = nm[cr][cc]

    return

def subtract_edge():

    for cc in range(C):
        for cr in [0, R-1]:
            if m[cr][cc] >= 1:
                m[cr][cc] -= 1
    for cr in range(1, R-1):
        for cc in [0, C-1]:
            if m[cr][cc] >= 1:
                m[cr][cc] -= 1
    return

def check():
    for cr, cc in targets:
        if m[cr][cc] < K:
            return False
    return True

def solve():
    # dprint()
    for choco in range(1, 102): # (D) 1001이 아니라 101 ;;;;;;;;;;;;;;;;;;;;;;
        wind()
        adjust()
        subtract_edge()
         # 초코 :choco
        if check():
          break

    return choco


res = solve()
print(res)

