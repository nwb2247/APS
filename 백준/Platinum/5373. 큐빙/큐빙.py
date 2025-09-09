def clockwise(arr, time): # 시계방향으로 90도 회전
    res = [l[:] for l in arr]
    for _ in range(time):
        res = [list(lst[::-1]) for lst in zip(*res)]
    # for l in res:
    #     print(l)
    return res

def rotate(side, direction):
    if side == "U":
        tmp = None
        if direction == "+":
            tmp = clockwise([lst[2:7] for lst in cube[2:7]], 1)
        else:
            tmp = clockwise([lst[2:7] for lst in cube[2:7]], 3)
        for cr in range(5):
            for cc in range(5):
                cube[cr+2][cc+2] = tmp[cr][cc]
    elif side == "L":
        tmp = []
        if direction == "+":
            for cr in range(12):
                tmp.append(cube[cr-3][:4])
            for cr in range(12):
                for cc in range(4):
                    cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[0:3] for lst in cube[6:9]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+3][cc] = tmp[cr][cc]
            for cr in range(6, 9):
                for cc in range(3):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[3:6] for lst in cube[9:12]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc + 9] = TMP[cr][cc]
        else:  #-
            for cr in range(12):
                tmp.append(cube[(cr+3)%12][:4])
            for cr in range(12):
                for cc in range(4):
                    cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[0:3] for lst in cube[0:3]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc] = tmp[cr][cc]
            for cr in range(3):
                for cc in range(3):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[3:6] for lst in cube[9:12]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc + 9] = TMP[cr][cc]

    elif side == "R":
        tmp = []
        if direction == "+":
            for cr in range(12):
                tmp.append(cube[(cr+3)%12][5:])
            for cr in range(12):
                for cc in range(7):
                    cube[cr][cc+5] = tmp[cr][cc]
            tmp = clockwise([lst[6:9] for lst in cube[0:3]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+3][cc+6] = tmp[cr][cc]
            for cr in range(0, 3):
                for cc in range(6, 12):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[3:6] for lst in cube[9:12]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc + 9] = TMP[cr][cc]
        else:  #-
            for cr in range(12):
                tmp.append(cube[(cr - 3) % 12][5:])
            for cr in range(12):
                for cc in range(7):
                    cube[cr][cc + 5] = tmp[cr][cc]
            tmp = clockwise([lst[6:9] for lst in cube[6:9]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc + 6] = tmp[cr][cc]
            for cr in range(6, 12):
                for cc in range(6, 12):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[3:6] for lst in cube[9:12]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 3][cc + 9] = TMP[cr][cc]
    elif side == "F":
        tmp = []
        if direction == "+":
            for cr in range(5, 12):
                tmp.append(cube[cr][-3:] + cube[cr][:-3])
            for cr in range(7):
                for cc in range(12):
                    cube[cr+5][cc] = tmp[cr][cc]
            tmp = clockwise([lst[6:9] for lst in cube[6:9]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+6][cc+3] = tmp[cr][cc]
            for cr in range(6, 12):
                for cc in range(6, 9):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[9:12] for lst in cube[3:6]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 9][cc + 3] = TMP[cr][cc]
        else: # -
            for cr in range(5, 12):
                tmp.append(cube[cr][3:] + cube[cr][:3])
            for cr in range(7):
                for cc in range(12):
                    cube[cr+5][cc] = tmp[cr][cc]
            tmp = clockwise([lst[0:3] for lst in cube[6:9]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+6][cc+3] = tmp[cr][cc]
            for cr in range(6, 12):
                for cc in range(0, 3):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[9:12] for lst in cube[3:6]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 9][cc + 3] = TMP[cr][cc]
    elif side == "B":
        tmp = []
        if direction == "+":
            for cr in range(4):
                tmp.append(cube[cr][3:] + cube[cr][:3])
            for cr in range(4):
                for cc in range(12):
                    cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[0:3] for lst in cube[0:3]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr][cc+3] = tmp[cr][cc]
            for cr in range(0, 3):
                for cc in range(0, 3):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[9:12] for lst in cube[3:6]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 9][cc + 3] = TMP[cr][cc]
        else:
            for cr in range(4):
                tmp.append(cube[cr][-3:] + cube[cr][:-3])
            for cr in range(4):
                for cc in range(12):
                    cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[6:9] for lst in cube[0:3]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr][cc+3] = tmp[cr][cc]
            for cr in range(0, 3):
                for cc in range(6, 9):
                    cube[cr][cc] = "."
            TMP = clockwise([lst[9:12] for lst in cube[3:6]], 2)
            for cr in range(3):
                for cc in range(3):
                    cube[cr + 9][cc + 3] = TMP[cr][cc]
    elif side == "D":
        tmp = []
        if direction == "+":
            tmp = clockwise([lst[:9] for lst in cube[:9]], 3)
            for cr in range(9):
                for cc in range(9):
                    if cr in [0, 8] or cc in [0, 8]:
                        cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[3:6] for lst in cube[9:12]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+9][cc+3] = tmp[cr][cc]
            tmp = clockwise([lst[9:12] for lst in cube[3:6]], 1)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+3][cc+9] = tmp[cr][cc]
        else:
            tmp = clockwise([lst[:9] for lst in cube[:9]], 1)
            for cr in range(9):
                for cc in range(9):
                    if cr in [0, 8] or cc in [0, 8]:
                        cube[cr][cc] = tmp[cr][cc]
            tmp = clockwise([lst[3:6] for lst in cube[9:12]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+9][cc+3] = tmp[cr][cc]
            tmp = clockwise([lst[9:12] for lst in cube[3:6]], 3)
            for cr in range(3):
                for cc in range(3):
                    cube[cr+3][cc+9] = tmp[cr][cc]







    return

def make_cube():
    # [0] 큐브 만들기
    cube = [["." for _ in range(12)] for _ in range(12)]

    starts = [(3, 3), (9, 3), (6, 3), (0, 3), (3, 0), (3, 6)]  # UDFBLR wyrogb
    colors = "wyrogb"
    pos_to_col = dict()
    for i in range(6):
        sr, sc = starts[i]
        col = colors[i]
        for cr in range(sr, sr + 3):
            for cc in range(sc, sc + 3):
                cube[cr][cc] = str(cr * 12 + cc)
                pos_to_col[str(cr * 12 + cc)] = col

    # [1] 아랫면 오른쪽에도 추가
    TMP = clockwise([lst[3:6] for lst in cube[9:12]], 2)
    for cr in range(3):
        for cc in range(3):
            cube[cr + 3][cc + 9] = TMP[cr][cc]
    return cube, pos_to_col

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ops = list(map(lambda x:tuple(x), input().split()))
    cube, pos_to_col = make_cube()
    for side, direction in ops:
        rotate(side, direction)

    # for l in cube:
    #     # print(list(map(lambda x: x.rjust(3), l)))
    #     print(*map(lambda x: x.rjust(3), l))
    #     # print(*map(lambda x: pos_to_col[x].rjust(3) if x != "." else ".".rjust(3), l))
    # print()
    # rotate("L", "+")
    # for l in cube:
    #     # print(list(map(lambda x: x.rjust(3), l)))
    #     print(*map(lambda x: x.rjust(3), l))
    #     # print(*map(lambda x: pos_to_col[x].rjust(3) if x != "." else ".".rjust(3), l))


    for l in cube[3:6]:
        print("".join(list(map(lambda x:pos_to_col[x], l[3:6]))))