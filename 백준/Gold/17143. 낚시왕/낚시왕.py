ds = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 위 아래 오른쪽 왼쪽
rev = {1: 2, 2: 1, 3: 4, 4: 3}

R, C, K = map(int, input().split())
arr = [[set() for _ in range(C)] for _ in range(R)]
info = dict()
for _ in range(K):  # 모든 물고기 크기 다르므로 id 대신 b 사용
    r, c, s, d, b = map(int, input().split())  # r, c, 스피드, 방향, 크기
    info[b] = (r - 1, c - 1, s, d)  # 좌표랑 1씩 빼줘야함
    arr[r - 1][c - 1].add(b)

def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def catch(cc):
    global ans
    for cr in range(R):
        if arr[cr][cc]:
            b = arr[cr][cc].pop()  # 어차피 한개
            info.pop(b)  # info에서도 지워야함
            ans += b
            break


def next_pos(cr, cc, s, cd):
    if cd == 1:
        fb, sb, cur, mod, axis = 0, R-1, cr, s % (2 * R - 2), 0
    elif cd == 2:
        fb, sb, cur, mod, axis = R-1, 0, cr, s % (2 * R - 2), 0
    elif cd == 3:
        fb, sb, cur, mod, axis = C-1, 0, cc, s % (2 * C - 2), 1
    elif cd == 4:
        fb, sb, cur, mod, axis = 0, C-1, cc, s % (2 * C - 2), 1

    if mod <= abs(fb - cur):
        nxt = cur + ds[cd][axis]*mod
        nd = cd
        # print(mod, (2 * C - 2), s)
        # print(1)
    elif mod <= abs(fb-cur) + abs(fb-sb):
        nxt = fb + ds[rev[cd]][axis] * (mod - abs(fb-cur))
        nd = rev[cd]
        # print(2)
    else:
        nxt = sb + ds[cd][axis] * (mod -(abs(fb-cur) + abs(fb-sb)))
        nd = cd
        # print(3)

    if cd == 1 or cd == 2:
        return nxt, cc, nd
    else:
        return cr, nxt, nd




def move():
    # for l in arr:
    #     print(l)
    # print(info)
    for b, v in info.items():
        cr, cc, s, cd = v
        arr[cr][cc].remove(b)


        # print("before", cr, cc, s, cd)
        nr, nc, nd = next_pos(cr, cc, s, cd)

        # print("after", nr, nc, s, nd)
        # print()
        arr[nr][nc].add(b)
        info[b] = (nr, nc, s, nd)

    # for l in arr:
    #     print(l)
    # print(info)


# for l in arr:
#     print(l)
# print(info)

ans = 0
for cc in range(C):  # (D) cr, cc 순서 바뀜
    # [1] 채취
    catch(cc)

    # print("채취")
    # print(info)
    # for l in arr:
    #     print(l)

    # [2] 이동
    move()

    # print("이동")
    # print(info)
    # for l in arr:
    #     print(l)

    # [3] 한마리만 남기기
    for zr in range(R):
        for zc in range(C):
            if len(arr[zr][zc]) <= 1:
                continue
            mx = max(arr[zr][zc])
            removed = []
            for k in arr[zr][zc]:
                if k == mx:
                    continue
                info.pop(k)  # info에서 지우기
                removed.append(k)
            for k in removed:  # arr에서 지우기
                arr[zr][zc].remove(k)

print(ans)

# d = dict()
# d[10] = (1, 2, 3)
# print(d[10])
# print(d.pop(10)[2])
# print(d)
