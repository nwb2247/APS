"""
엣지
1 4
0fF1 nown으로 구별하지 말고 own에 바로 적용
"""

"""
리팩토링, 2차원 visited
첫방문이거나 키가 추가된 키가 있는 경우에만 더 나아가기

진리표
a b
1 1 0
0 1 1
1 0 0
0 0 0
=> ((~a) & b) != 0 이라면 새 키가 추가 되었다는 뜻 


"""
from collections import deque

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 미방문을 0, 열쇠없이 방문을 1로 두기 위해 A를 1로둠
doors = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6}
keys = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6}

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
sr, sc = -1, -1

f = 0
for zr in range(N):
    for zc in range(M):
        if arr[zr][zc] == "0":
            sr, sc = zr, zc
            arr[zr][zc] = "."
            f = 1
            break
    if f:
        break

q = deque()
v = [[0]*M for _ in range(N)]

v[sr][sc] = 1
q.append((sr, sc, 0, 1))
ans = -1
while q:
    cr, cc, cdist, own = q.popleft()
    # print(cr, cc, cdist, own)
    val = arr[cr][cc]

    if val == "1":
        ans = cdist
        break
    elif val in keys:
        key = keys[val]
        own = own | (1<<key)

    for dr, dc in ds:
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc):
            continue
        if arr[nr][nc] == "#":
            continue
        if (~v[nr][nc]) & own == 0: # 새 key가 추가되지 않았다면 미방문
            continue
        if arr[nr][nc] in doors:
            key = doors[arr[nr][nc]]
            if own & (1 << key) == 0:
                continue
        v[nr][nc] = own
        q.append((nr, nc, cdist+1, own))

print(ans)





# """
# 3차원 (각 가능한 masking 별로 따로만들기, 정답 O)
# """
# from collections import deque
#
# def oob(r, c):
#     return not (0<=r<N and 0<=c<M)
#
# ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# doors = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}
# keys = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5}
#
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(N)]
# sr, sc = -1, -1
#
# f = 0
# for zr in range(N):
#     for zc in range(M):
#         if arr[zr][zc] == "0":
#             sr, sc = zr, zc
#             arr[zr][zc] = "."
#             f = 1
#             break
#     if f:
#         break
#
# q = deque()
# v = [[[0]*(1<<6) for _ in range(M)] for _ in range(N)]
#
# v[sr][sc][0] = 1
# q.append((sr, sc, 0, 0))
# ans = -1
# while q:
#     cr, cc, cdist, own = q.popleft()
#     # print(cr, cc, cdist, own)
#     val = arr[cr][cc]
#
#     if val == "1":
#         ans = cdist
#         break
#     elif val in keys:
#         key = keys[val]
#         own = own | (1<<key)
#
#     for dr, dc in ds:
#         nr, nc = cr+dr, cc+dc
#         if oob(nr, nc):
#             continue
#         if arr[nr][nc] == "#" or v[nr][nc][own] == 1:
#             continue
#         if arr[nr][nc] in doors:
#             key = doors[arr[nr][nc]]
#             if own & (1 << key) == 0:
#                 continue
#         v[nr][nc][own] = 1
#         q.append((nr, nc, cdist+1, own))
#
# print(ans)
