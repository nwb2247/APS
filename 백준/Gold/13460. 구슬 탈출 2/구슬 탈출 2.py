"""
빨강 , 파랑 동일 이동시에 같이 빠져나와도 실패
빨강만 빠져 나와야함

바깥행열을 모두 막혀 있음

tilt() : red blue만을 움직이는 방식으로

움직히는 방향쪽으로 더 앞에 있는 것을 먼저 움직임 (일렬, 일렬X 모두 동일)

K = 10 (K번이하로만 움직일 수 있음)
ans = K+1로 초기화하고
마지막에도 K+1이면 -1
depth를 0부터 시작 (직전에 몇번 움직였는지..)
종료 조건 [1] 타겟과 동일하다면 종료
종료 조건 [2] 10 직전에 10번 움직였는데 아직도 다르면 종료
순서 안바뀌게 주의


# 일땐 막히고, O일땐 거기에 멈춰야함
+ R, B는 원래거에서만 없애고 표시 하지 않음


red, blue 위치를 항상 기억
"""
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


# //2 == 0 : 종방향
# //2 == 1 : 횡방향
# %2 == 0 : 감소방향 => 감소방향이면 작은게 더 우선
# %2 == 1 : 증가방향 => 증가방향이면 큰게 더 우선


def move(pos, cd, x): # x: 불가한 자리 (먼저 간 애)
    dr, dc = ds[cd]
    cr, cc = pos
    while True:
        nr, nc = cr + dr, cc + dc
        if (nr, nc) == target:
            return nr, nc
        if arr[nr][nc] == "#":
            return cr, cc
        if arr[nr][nc] == "." and (nr, nc) == x:
            return cr, cc

        cr, cc = nr, nc


def tilt(red, blue, cd):
    blue_first = 0  # 0이면 red먼저 1이면 blue먼저 움직임 (D) blue_first
    if cd % 2 == 0:  # 감소방향이면 (상좌)
        if blue[cd // 2] < red[cd // 2]:  # 종횡 방향
            blue_first = 1
    else:  # 증가방향이면 (하우)            # (D) if cd%1 == 0 으로 씀;;;
        if blue[cd // 2] > red[cd // 2]:
            blue_first = 1
    # 아예 red, blue가 같은 경우는 없으므로 등호조건 고려 안해도 OK

    if blue_first:  # 빨강먼저면
        nblue = move(blue, cd, (-1, -1))
        nred = move(red, cd, nblue)
    else:
        nred = move(red, cd, (-1, -1))
        nblue = move(blue, cd, nred)

    return nred, nblue


def backtrack(depth, red, blue):
    global ans

    if depth >= ans:  # 가지치기 (먼저 찾은 ans보다 같거나 크면)
        return

    if blue == target:  # (D)
        return

    if red == target and blue != target:  # 종료조건 [1]
        ans = min(ans, depth)  # min 안전하게 쓰자 일단
        return

    if depth == K:  # 종료조건 [2] # 가지치기 와 합칠 수 있는지..?
        return

    for cd in range(4):
        # [1] 일단 새 위치 구함 + 지도에 반영해줌

        nred, nblue = tilt(red, blue, cd)

        # [2] 하부 재귀 호출
        if v[nred[0]][nred[1]][nblue[0]][nblue[1]] > depth+1:
            v[nred[0]][nred[1]][nblue[0]][nblue[1]] = depth+1
            backtrack(depth + 1, nred, nblue)


R, C = map(int, input().split())
K = 10
arr = [list(input()) for _ in range(R)]
r = (-1, -1)
b = (-1, -1)
target = (-1, -1)

for zr in range(R):
    for zc in range(C):
        if arr[zr][zc] == "R":
            arr[zr][zc] = "."
            r = (zr, zc)
        if arr[zr][zc] == "B":
            arr[zr][zc] = "."
            b = (zr, zc)
        if arr[zr][zc] == "O":
            target = (zr, zc)

v = [[[[K+1 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]


ans = K + 1
backtrack(0, r, b)
if ans == K + 1:
    print(-1)
else:
    print(ans)
