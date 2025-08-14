"""
스위치 칸 도착
스위치를 먼저 키고, 그다음 학생을 확인 (즉, 스위치칸에서는 기절할 일 없음)
스위치 키면 계속 켜져잇음
전진과 방향 전환

벽앞에서 전진은 무시됨

좀비들은 처음엔 아래보고 있음
좀비들은 벽에 부딪히면 반대 방향 바라봄(나아가는건 다음턴)

O는 빈캄
Z는 좀비 (N*2 최대 30이니까 그냥 매번 확인하자)
S는 스위치

"""
def oob(r, c):
    return not (0<=r<N and 0<=c<N)

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def move_ari(op):
    global cr, cc, cd
    if op == "F":
        dr, dc = ds[cd]
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            return
        else:
            cr, cc = nr, nc
    elif op == "R":
        cd = (cd+1)%4
    elif op == "L":
        cd = (cd+4-1)%4


def move_zombie():
    for i, (zr, zc, zd) in enumerate(zombies):
        nzr = zr + zd
        if oob(nzr, zc):
            zombies[i] = (zr, zc, -zd)    # 나아가지 않고 방향만
        else:
            zombies[i] = (nzr, zc, zd)


N = int(input())
A = list(input())

arr = [list(input()) for _ in range(N)]

zombies = []
for zr in range(N):
    for zc in range(N):
        if arr[zr][zc] == "Z":
            zombies.append((zr, zc, 1)) # 다 내려가는 방향

bright = [[0]*N for _ in range(N)]

cr, cc, cd = 0, 0, 2 # (아래를 바라보고 시작)

found = False
for op in A:

    # print(cr, cc, cd, )
    # 아리 움직임,
    # 스위치확인
    # (좀비랑 같은 칸인지 확인)
    # 좀비 움직임
    # (좀비랑 같은 칸인지 확인)

    # 아리 움직임
    move_ari(op)

    # 스위치 확인
    if arr[cr][cc] == "S":
        bright[cr][cc] = 1
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            vr, vc = cr+dr, cc+dc
            if oob(vr, vc):
                continue
            bright[vr][vc] = 1

    for zr, zc, _ in zombies:
        if (cr, cc) == (zr, zc) and bright[cr][cc] == 0:
            found = True
            break
        if found:
            break

    move_zombie()

    for zr, zc, _ in zombies:
        if (cr, cc) == (zr, zc) and bright[cr][cc] == 0:
            found = True
            break
        if found:
            break

if found:
    print("Aaaaaah!")
else:
    print("Phew...")


