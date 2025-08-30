# 리팩토링
# 회전 -> 기준점 (회전해도 그대로인)을 offset으로 생각하고,
# 회전 시키려는 점이 기준점에서 얼마나 떨어져 있는지를 a, b로 생각
# 문제에서 x, y로 주어졌고, 생각하는 방향이나 좌표 순서가 평소와 다르다면 그냥 문제를 따르자

ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def rotate(base, pos):
    bx, by = base
    cx, cy = pos
    a, b = cx-bx, cy-by
    # bx, by 기준점 (회전해도 그대로 있는)
    # a, b 기준점으로부터 얼마나 떨어져 있는지,,,
    # cx == bx + a
    # cy == by + b
    return bx - b, by + a

def generate_dragon(sx, sy, d, g):
    global res

    ex, ey = sx+ds[d][0], sy+ds[d][1]
    sset = set([(sx, sy), (ex, ey)])

    for _ in range(g):
        added = set()
        for pos in sset:
            added.add(rotate((ex, ey), pos))
        sset = sset.union(added)
        ex, ey = rotate((ex, ey), (sx, sy))

    # print(sset)
    res = res.union(sset)

res = set()
N = int(input())
for _ in range(N):
    generate_dragon(*map(int, input().split()))

# 좌상 꼭지점, 유효 좌표 100이므로 99까지 확인 range(100)
ans = 0
for zx in range(100):
    for zy in range(100):
        if (zx, zy) in res and (zx+1, zy) in res and (zx, zy+1) in res and (zx+1, zy+1) in res:
            ans += 1
print(ans)

# 원래 코드
"""
ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def rotate(x, y):
    return -y, x

def gen(sx, sy, d, g):

    ex, ey = ds[d][0], ds[d][1]

    sset = set()
    sset.add((0, 0))
    sset.add((ex, ey))

    for _ in range(g):
        dx, dy = ex-rotate(ex, ey)[0], ey-rotate(ex, ey)[1]
        pos = []
        for cx, cy in sset:
            a, b = rotate(cx, cy)
            pos.append((a+dx, b+dy))
        ex, ey = dx, dy
        for a, b in pos:
            sset.add((a, b))
        # print("sset", sset)

    for a, b in sset:
        res.add((sx+a, sy+b))

res = set()

N = int(input())
for i in range(N):
    gen(*map(int, input().split()))

cnt = 0
for x in range(100):
    for y in range(100):
        if (x, y) in res and (x+1, y) in res and (x, y+1) in res and (x+1, y+1) in res:
            cnt += 1
print(cnt)
"""

