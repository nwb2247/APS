"""
[2차 풀이]
1차와 거의 동일
끝점만 중복으로 들어가므로 제외해주고, set대신 list로 append
어떤 점이 기준이 되어 회전시키고, 기준점을 어떻게 새롭게 갱신하는지 확인하면 됨

[이해 및 구상]
드래곤 커브의 갯수를 의미하는 정수 N
시작점 방향 차수 주어짐
끝점을 관리해야함
0우 1상 2좌 3하

x는 행, 아래로 갈수록 증가
y는 열, 오른쪽으로 갈수록 증가

주어지는 드래곤 커브의 모든 꼭지점은 좌표평면 범위를 넘지 않는다. 0<= <= 100

출력 : 네꼭지점이 모두 드래곤 커브의 일부인 1*1정사각형의 수
"""

def rotate(cx, cy, bx, by):
    dx, dy = cx-bx, cy-by
    return bx-dy, by+dx # (백준), 백준에서는 x가 열 y가 행
    # return bx+dy, by-dx # (코드트리)

def make_curve(X, Y, d, g):

    sx, sy = X, Y
    ex, ey = sx+ds[d][0], sy+ds[d][1]
    pos = [(sx, sy), (ex, ey)]
    for _ in range(g):
        tmp = pos[:]
        # [1] 돌린 좌표들 구하기
        for cx, cy in pos:
            if (cx, cy) == (ex, ey): # (ex, ey)를 기준으로 돌리기때문에 그대로 있음. 한번더 들어갈 필요없음
                continue
            tmp.append(rotate(cx, cy, ex, ey))
        # [2] 시작점을 돌려서 새로운 끝점으로 만들고, pos도 tmp로 갱신
        ex, ey = rotate(sx, sy, ex, ey)
        pos = tmp

    # print(pos)

    for cx, cy in pos:
        m[cx][cy] = 1

    return

def solve():
    global ans
    for X, Y, d, g in info:
        make_curve(X, Y, d, g)


    for x in range(100): # x, x+1 확인할것이므로 99까지만
        for y in range(100):
            if m[x][y] == 1 and m[x+1][y] == 1 and m[x][y+1] == 1 and m[x+1][y+1] == 1:
                ans += 1
    return

ds = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 0우 1상 2좌 3하 (백준)
# ds = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 0우 1상 2좌 3하 (코드트리)
N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]
m = [[0 for _ in range(101)] for _ in range(101)]
ans = 0
solve()
print(ans)

# -----------------------------------------------------------------------------
# [1차 풀이]
#
#
# # 리팩토링
# # 회전 -> 기준점 (회전해도 그대로인)을 offset으로 생각하고,
# # 회전 시키려는 점이 기준점에서 얼마나 떨어져 있는지를 a, b로 생각
# # 문제에서 x, y로 주어졌고, 생각하는 방향이나 좌표 순서가 평소와 다르다면 그냥 문제를 따르자
#
# ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#
# def rotate(base, pos):
#     bx, by = base
#     cx, cy = pos
#     a, b = cx-bx, cy-by
#     # bx, by 기준점 (회전해도 그대로 있는)
#     # a, b 기준점으로부터 얼마나 떨어져 있는지,,,
#     # cx == bx + a
#     # cy == by + b
#     return bx - b, by + a
#
# def generate_dragon(sx, sy, d, g):
#     global res
#
#     ex, ey = sx+ds[d][0], sy+ds[d][1]
#     sset = set([(sx, sy), (ex, ey)])
#
#     for _ in range(g):
#         added = set()
#         for pos in sset:
#             added.add(rotate((ex, ey), pos))
#         sset = sset.union(added)
#         ex, ey = rotate((ex, ey), (sx, sy))
#
#     # print(sset)
#     res = res.union(sset)
#
# res = set()
# N = int(input())
# for _ in range(N):
#     generate_dragon(*map(int, input().split()))
#
# # 좌상 꼭지점, 유효 좌표 100이므로 99까지 확인 range(100)
# ans = 0
# for zx in range(100):
#     for zy in range(100):
#         if (zx, zy) in res and (zx+1, zy) in res and (zx, zy+1) in res and (zx+1, zy+1) in res:
#             ans += 1
# print(ans)
#
# # 원래 코드
# """
# ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#
# def rotate(x, y):
#     return -y, x
#
# def gen(sx, sy, d, g):
#
#     ex, ey = ds[d][0], ds[d][1]
#
#     sset = set()
#     sset.add((0, 0))
#     sset.add((ex, ey))
#
#     for _ in range(g):
#         dx, dy = ex-rotate(ex, ey)[0], ey-rotate(ex, ey)[1]
#         pos = []
#         for cx, cy in sset:
#             a, b = rotate(cx, cy)
#             pos.append((a+dx, b+dy))
#         ex, ey = dx, dy
#         for a, b in pos:
#             sset.add((a, b))
#         # print("sset", sset)
#
#     for a, b in sset:
#         res.add((sx+a, sy+b))
#
# res = set()
#
# N = int(input())
# for i in range(N):
#     gen(*map(int, input().split()))
#
# cnt = 0
# for x in range(100):
#     for y in range(100):
#         if (x, y) in res and (x+1, y) in res and (x, y+1) in res and (x+1, y+1) in res:
#             cnt += 1
# print(cnt)
# """
#
