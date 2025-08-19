"""
방향 전환 LR 시에는 움지기이지 않음

지나간 영역을 모두 포함하는 가장 작은 직사각형 넓이 구하기
-> 이동할때마다 maxx, maxy minx, miny를 갱신

(0, 0) 북쪽

x, y 축 인거 신경쓰기

"""
DS = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 북서남동 (L 기준, xy 좌표 기준)

TC = int(input())
for _ in range(TC):
    ops = list(input())

    cx, cy, cd = 0, 0, 0

    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for op in ops:
        # print(cx, cy, cd)
        if op == "L":
            cd = (cd + 1)%4
        elif op == "R":
            cd = (cd + 4 - 1)%4
        elif op == "F":
            dx, dy = DS[cd]
            cx, cy = cx+dx, cy+dy
            min_x = min(min_x, cx)
            min_y = min(min_y, cy)
            max_x = max(max_x, cx)
            max_y = max(max_y, cy)
        elif op == "B":
            dx, dy = DS[cd]
            cx, cy = cx - dx, cy - dy
            min_x = min(min_x, cx)
            min_y = min(min_y, cy)
            max_x = max(max_x, cx)
            max_y = max(max_y, cy)
        else:
            print("!!")

    print((max_x-min_x)*(max_y-min_y))


