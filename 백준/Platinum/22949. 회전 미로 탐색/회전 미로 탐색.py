"""
내부에 있을때는 회전이 무의미
외부로 나가는 경우에 어떻게 맞닿아 있는지가 중요

현재 초에 따라서 어디로 나가야하는지 결정됨

br, bc : 회전해도 변하지 않는 기준점 (정수 좌표가 되도록 잡자)
dr, dc : 현재 위치가 기준점과 떨어진 정도 (방향 배열 ds의 dr, dc와 혼동하면 안됨)
즉 cr, cc == br+dr, bc+dc 가 되기 위해서
=> dr, dc = cr-br, cc-bc
offset_r, offset_c : 원하는 위치가 되도록 하기 위해 더해줘야하는 크기

"""

from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def rotate(cr, cc): # rotate 로직 test
    i, j = cr//4, cc//4 # (영역의 좌상단)
    br, bc = 4 * i - 1, 4 * j - 1 # 회전 기준을 정수로 잡으려면 좌상단의 왼쪽위로 잡아야함 (offset of r : 5)
    dr, dc = cr - br, cc - bc
    offset_r = 5
    return br + dc, bc - dr + offset_r


# def rotate(r, c):
#     i = r // 4
#     a = r % 4
#     j = c // 4
#     b = c % 4
#     return 4 * i + b, 4 * j + (3 - a)


K = int(input())
R, C = 4 * K, 4 * K
arr = [list(input()) for _ in range(4 * K)]
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

    for dr, dc in ds:
        nr, nc = cr + dr, cc + dc
        if (nr // 4, nc // 4) == (cr // 4, cc // 4):
            if oob(nr, nc):
                continue
            if arr[nr][nc] == "#":
                continue
            if v[nr][nc][(crot + 1) % 4] != -1:
                continue
            v[nr][nc][(crot + 1) % 4] = v[cr][cc][crot] + 1
            q.append((nr, nc, (crot + 1) % 4))

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

    # print(q)
    #
    # for rr in range(4):
    #     print(f"{rr * 90}도")
    #     for r in range(R):
    #         for c in range(C):
    #             print(v[r][c][rr], end=" ")
    #         print()
    #     print()

print(ans)





# arr = [[()]*12 for _ in range(12)]
# for i in range(4, 8):
#     for j in range(8, 12):
#         arr[i][j] = (i, j)
# for l in arr:
#     print(l)
# print()
#
#
# new_arr  = [[()]*12 for _ in range(12)]
# for r in range(12):
#     for c in range(12):
#         i = r//4
#         a = r%4
#         j = c//4
#         b = c%4
#         new_arr[4*i+b][4*j + (3-a)] = arr[4*i+a][4*j+b]
# for l in new_arr:
#     print(l)
# print()
