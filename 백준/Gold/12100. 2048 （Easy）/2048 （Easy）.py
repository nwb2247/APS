from itertools import permutations

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 0상 1하 2좌 3우
rev = [1, 0, 3, 2]


def oob(r, c):
    return not (0 <= r < Z and 0 <= c < Z)


Z = int(input())
arr = [list(map(int, input().split())) for _ in range(Z)]


def move_each(sr, sc, er, ec, cd, arr):
    # [1] 담기
    cr, cc = sr, sc
    dr, dc = ds[rev[cd]]  # 반대방향
    blocks = []

    while not oob(cr, cc):
        nr, nc = cr + dr, cc + dc
        if arr[cr][cc] != 0:
            blocks.append(arr[cr][cc])
        cr, cc = nr, nc

    new_blocks = []
    ci = 0
    while ci < len(blocks):
        if ci+1 == len(blocks):
            new_blocks.append(blocks[ci])
            break
        if blocks[ci+1] == blocks[ci]:
            new_blocks.append(blocks[ci]*2)
            ci += 2
        else:
            new_blocks.append(blocks[ci])
            ci += 1

    # [2] 채우기
    cr, cc = sr, sc
    dr, dc = ds[rev[cd]]  # 역방향
    idx = 0
    while not oob(cr, cc):
        if idx < len(new_blocks):
            arr[cr][cc] = new_blocks[idx]
        else:
            arr[cr][cc] = 0
        idx += 1
        cr, cc = cr + dr, cc + dc


def move(cd, arr):
    if cd == 0:  # 상 이동
        for sc in range(Z):
            sr = 0
            ec = sc
            er = Z - 1
            move_each(sr, sc, er, ec, cd, arr)
    elif cd == 1:  # 하 이동
        for sc in range(Z):
            sr = Z - 1
            ec = sc
            er = 0
            move_each(sr, sc, er, ec, cd, arr)
    elif cd == 2:  # 좌 이동
        for sr in range(Z):
            sc = 0
            er = sr
            ec = Z - 1
            move_each(sr, sc, er, ec, cd, arr)
    elif cd == 3:  # 우 이동
        for sr in range(Z):
            sc = Z - 1
            er = sr
            ec = 0
            move_each(sr, sc, er, ec, cd, arr)


# 최대! 5번 but 움직여서 더 작아지는 경우는 없으므로 5번 움직여보자
K = 5
way = [-1]*K
ans = 0
def backtrack(depth):
    global ans

    if depth == K:
        narr = [lst[:] for lst in arr]
        for i in way:
            move(i, narr)
        ans = max(ans, max(map(max, narr)))
        return

    for i in range(4):
        way[depth] = i
        backtrack(depth+1)

backtrack(0)
print(ans)

