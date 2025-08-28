"""
[요약평]
백트래킹 -> 복구 로직 구상 단계에서 완벽하게 가져가자
다른 말의 경로는 복구 시에 지우면 안됨,,,,

[1] restore_pos : 복구할 좌표만을 기억해둠 (원래 코드에선 make_pos
[2] l을 이용해 길이를 늘려가며 추가하기
이 2개는 백트래킹 시 나중에도 활용할 수 있을 듯

[타임라인]
이해 및 구상 : 11분
구현 : 22분
디버깅 5분
-----
총 38분

[이해 및 구상]
+) units, L, ways 등 전처리에 대한 구상 + 변수명까지 정해놓고 들어가니
    자잘한 부분에 신경을 덜 쓰고 구현에 집중가능해짐

[구현]
-) 집중력이 흐려져서 make_pos에 원래 1이었던 것도 넣을 뻔 했음
    (1이 된것은 이전에 다른 말의 경로이므로 이는 나중에 복구 되면 안됨)
+) 변수명, 변수 자료형 잘 정리하고 들어감 (방향 관리 등)
+) 다른 로직 수행전에 restore_pos 함수 단위 테스트 먼저 진행해서 확신을 얻음

[디버깅]
-) bt 함수 정의해놓고 실행부를 주석처리해서 헤맴 (계속 반복되는 실수...)
+) 3*3 만들어놓고 각 말을 가운데에 하나씩 두고, 장애물을 넣었다 뺏다 하면서 잘 구현이 됐는지 확인 후 제출

"""

# [구상 내용]
#
# 주의사항
# 본인 말 넘기 가능, 상대말 넘기 불가능
# 각 말마다 최대 3개의 방법
#
# 갈수 없는 넓이의 총합의 최소
#
# 최대 8개 + 맵넓이 크지 않으므로 백트래킹 ㄱ
# (가지치기는 나중에 생각)
#
# units = [(종류, r, c)]
# L = len(units)
#
# ways = dict() (0 패딩 귀찮)
#
# bt(depth)
#     pos = 갈수 있는 곳
#     bt(depth)
#     pos -> 0으로 복구

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서
ways = dict()
ways[1] = [[0], [1], [2], [3]]
ways[2] = [[0, 2], [1, 3]]
ways[3] = [[0, 1], [1, 2], [2, 3], [3, 0]]
ways[4] = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
ways[5] = [[0, 1, 2, 3]]


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def restore_pos(cr, cc, w):
    pos = []
    for d in w:
        dr, dc = ds[d]
        l = 1
        while True:
            nr, nc = cr + l * dr, cc + l * dc
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
        sm = sum(map(lambda x: x.count(0), v))

        # for l in v:
        #     print(*l)
        # print(sm)

        ans = min(ans, sm)
        return

    t, sr, sc = units[depth]
    way = ways[t]
    for w in way:  # 가능한 방법들 w == [0, 1, 2]...
        pos = restore_pos(sr, sc, w)
        for nr, nc in pos:
            v[nr][nc] = 1
        backtrack(depth + 1)
        for nr, nc in pos:
            v[nr][nc] = 0


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

v = [[0] * C for _ in range(R)]  # 1 자기말, 2 벽

units = []
for zr in range(R):
    for zc in range(C):
        if arr[zr][zc] == 6:
            v[zr][zc] = 2
        elif 1 <= arr[zr][zc] <= 5:
            v[zr][zc] = 1
            units.append([arr[zr][zc], zr, zc])
L = len(units)
ans = R * C
backtrack(0)
# for l in v:
#     print(l)
# print(make_pos(4, 3, [3, 0]))
print(ans)



# ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서
# ways = dict()
# ways[1] = [[0], [1], [2], [3]]
# ways[2] = [[0, 2], [1, 3]]
# ways[3] = [[0, 1], [1, 2], [2, 3], [3, 0]]
# ways[4] = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
# ways[5] = [[0, 1, 2, 3]]
#
#
# def oob(r, c):
#     return not (0 <= r < R and 0 <= c < C)
#
#
# def make_pos(cr, cc, w):
#     pos = []
#     for d in w:
#         dr, dc = ds[d]
#         l = 1
#         while True:
#             nr, nc = cr + l * dr, cc + l * dc
#             if oob(nr, nc) or v[nr][nc] == 2:
#                 break
#             if v[nr][nc] == 0:
#                 pos.append((nr, nc))
#             # elif v[nr][nc] == 1: # 원래 내 말 있던 곳은 아무것도 안함 (중요!!!)
#             #     pass
#             l += 1
#
#     return pos
#
#
# def backtrack(depth):
#     global ans
#
#     if depth == L:
#         sm = sum(map(lambda x: x.count(0), v))
#
#         # for l in v:
#         #     print(*l)
#         # print(sm)
#
#         ans = min(ans, sm)
#         return
#
#     t, sr, sc = units[depth]
#     way = ways[t]
#     for w in way:  # 가능한 방법들 w == [0, 1, 2]...
#         pos = make_pos(sr, sc, w)
#         for nr, nc in pos:
#             v[nr][nc] = 1
#         backtrack(depth + 1)
#         for nr, nc in pos:
#             v[nr][nc] = 0
#
#
# R, C = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(R)]
#
# v = [[0] * C for _ in range(R)]  # 1 자기말, 2 벽
#
# units = []
# for zr in range(R):
#     for zc in range(C):
#         if arr[zr][zc] == 6:
#             v[zr][zc] = 2
#         elif 1 <= arr[zr][zc] <= 5:
#             v[zr][zc] = 1
#             units.append([arr[zr][zc], zr, zc])
# L = len(units)
# ans = R * C
# backtrack(0)
# # for l in v:
# #     print(l)
# # print(make_pos(4, 3, [3, 0]))
# print(ans)
