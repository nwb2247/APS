ds = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서
ways = dict()
ways[1] = [[0], [1], [2], [3]]
ways[2] = [[0, 2], [1, 3]]
ways[3] = [[0, 1], [1, 2], [2, 3], [3, 0]]
ways[4] = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
ways[5] = [[0, 1, 2, 3]]

def oob(r, c):
    return not (0<=r<R and 0<=c<C)


def make_pos(cr, cc, w):
    pos = []
    for d in w:
        dr, dc = ds[d]
        l = 1
        while True:
            nr, nc = cr+l*dr, cc+l*dc
            if oob(nr, nc) or v[nr][nc] == 2:
                break
            if v[nr][nc] == 0:
                pos.append((nr, nc))
            # elif v[nr][nc] == 1: # 원래 내 말 있던 곳은 아무것도 안함 (중요!!!)
            #     pass
            l += 1

    return pos



def backtrack(depth):
    global ans

    if depth == L:
        sm = sum(map(lambda x:x.count(0), v))

        # for l in v:
        #     print(*l)
        # print(sm)

        ans = min(ans, sm)
        return

    t, sr, sc = units[depth]
    way = ways[t]
    for w in way: # 가능한 방법들 w == [0, 1, 2]...
        pos = make_pos(sr, sc, w)
        for nr, nc in pos:
            v[nr][nc] = 1
        backtrack(depth+1)
        for nr, nc in pos:
            v[nr][nc] = 0


        




R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

v = [[0]*C for _ in range(R)] # 1 자기말, 2 벽


units = []
for zr in range(R):
    for zc in range(C):
        if arr[zr][zc] == 6:
            v[zr][zc] = 2
        elif 1 <= arr[zr][zc] <= 5:
            v[zr][zc] = 1
            units.append([arr[zr][zc], zr, zc])
L = len(units)
ans = R*C
backtrack(0)
# for l in v:
#     print(l)
# print(make_pos(4, 3, [3, 0]))
print(ans)


