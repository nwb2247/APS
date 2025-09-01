"""
[요약평]
문제에 주어진 조건을 가능한 따르자
(임의로 하면 불필요한 분기가 많아짐...)
    => to_addsub -> removed로 리팩토링

손 구상 했던건 자주 확인하기 (놓친 조건 없는지,,)

패딩 반드시 해야되는거 아니면 그냥 하지말자... (더 헷갈림)

[타임라인]
이해 및 구상 10분
구현 및 디버깅 39분
    디버깅
        bfs 방문처리 해결 5분
        평균 조건 구현 안했음 해결 3분
        0으로 나누기 해결 2분
--------
총 49분
[이해 및 구상]
-) 배수 조건 때문에 패딩을 넣었는데 패딩 신경쓰느라고 더 복잡해짐
    차라리 +1 더해준 상태에서 배수확인하는게 더 쉬웠을듯
    열의 개수 M에 대해서는 패딩 안해줬기 때문에 통일성도 없음...

[구현]
-) 문제에서 주어진 대로 분기 안함
    했다면 zero division error 신경 안써도 됐음,,
+) pos에 언제 넣어주고 빼줄지, pos 길이 1보다 클때 지우기 등,,,
+) 크다 작다 if elif 로 처리 (같은 경우는 아무것도 안하므로 if else로 하면 안됨...)

[디버깅]
-

[시간복잡도]
N*M*T

돌리는 횟수 T
    각 행마다 rotate N*M
    BFS 대략 5*N*M?

"""


# 손 구상 내용
#
# 인접하면서 수가 같은 것 모두 지움 -> BFS
# 지울거 없으면 평균 구해서 크면 1빼고 작으면 1더해줌
#
# 인접 조건 처리가 관건
# 0자리 패딩


# 리팩토링 ver (removed 사용해서 문제에 주어진 방법으로 분기)

from collections import deque

q = deque([1, 2, 3, 4])

ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def oobr(r):
    return not (1<=r<=R)

def bfs():
    v = [[]] + [[0 for _ in range(C)] for _ in range(R+1)]

    removed = 0
    # to_addsub = True
    for sr in range(1, R+1):
        for sc in range(C):
            if v[sr][sc] == 1:
                continue
            if arr[sr][sc] == 0:
                continue

            pos = deque() # pos 길이 1이상인 것만 지워줌
            q = deque()
            q.append((sr, sc))
            v[sr][sc] = 1
            while q:
                cr, cc = q.popleft()
                pos.append((cr, cc))
                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    nc %= C
                    if oobr(nr):
                        continue
                    if arr[nr][nc] != arr[sr][sc]:
                        continue
                    if v[nr][nc] == 1: # (D) 방문확인 까먹음;;;;
                        continue
                    v[nr][nc] = 1
                    q.append((nr, nc))


            if len(pos) > 1:
                # to_addsub = False
                for nr, nc in pos:
                    removed += 1
                    arr[nr][nc] = 0

    # if to_addsub:
    if removed == 0:    # 지워진게 없다면,,,,
        sm = sum(map(sum, arr))
        cnt = R*C - sum(map(lambda x:x.count(0), arr[1:]))
        if cnt == 0: # 이미 전부 0이면 종료
            return
        mean = sm/cnt
        # print(cnt, sm)
        for cr in range(1, R+1):
            for cc in range(C):
                if arr[cr][cc] == 0: # 빈칸은 패스
                    continue
                if arr[cr][cc] > mean:
                    arr[cr][cc] -= 1
                # 같은 경우도 있으므로 elif 로 써야함
                elif arr[cr][cc] < mean:
                    arr[cr][cc] += 1


R, C, T = map(int, input().split())
arr = [deque()] + [deque(list(map(int, input().split()))) for _ in range(R)]
ops = [tuple(map(int, input().split())) for _ in range(T)]

for x, d, k in ops:

    # [1] 회전
    if d == 0:
        d = 1
    else:
        d = -1
    for i in range(x, R+1, x):
        arr[i].rotate(d*k)

    # [2] 인접부분 확인
    bfs()

    # for q in arr[1:]:
    #     print(q)
    # print()

print(sum(map(sum, arr[1:])))

# from collections import deque
#
# q = deque([1, 2, 3, 4])
#
# ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#
# def oobr(r):
#     return not (1<=r<=R)
#
# def bfs():
#     v = [[]] + [[0 for _ in range(C)] for _ in range(R+1)]
#
#     to_addsub = True
#     for sr in range(1, R+1):
#         for sc in range(C):
#             if v[sr][sc] == 1:
#                 continue
#             if arr[sr][sc] == 0:
#                 continue
#
#             pos = deque() # pos 길이 1이상인 것만 지워줌
#             q = deque()
#             q.append((sr, sc))
#             v[sr][sc] = 1
#             while q:
#                 cr, cc = q.popleft()
#                 pos.append((cr, cc))
#                 for dr, dc in ds:
#                     nr, nc = cr+dr, cc+dc
#                     nc %= C
#                     if oobr(nr):
#                         continue
#                     if arr[nr][nc] != arr[sr][sc]:
#                         continue
#                     if v[nr][nc] == 1: # (D) 방문확인 까먹음;;;;
#                         continue
#                     v[nr][nc] = 1
#                     q.append((nr, nc))
#
#
#             if len(pos) > 1:
#                 to_addsub = False
#                 for nr, nc in pos:
#                     arr[nr][nc] = 0
#
#     if to_addsub:
#         sm = sum(map(sum, arr))
#         cnt = R*C - sum(map(lambda x:x.count(0), arr[1:]))
#         if cnt == 0: # 이미 전부 0이면 종료
#             return
#         mean = sm/cnt
#         # print(cnt, sm)
#         for cr in range(1, R+1):
#             for cc in range(C):
#                 if arr[cr][cc] == 0: # 빈칸은 패스
#                     continue
#                 if arr[cr][cc] > mean:
#                     arr[cr][cc] -= 1
#                 # 같은 경우도 있으므로 elif 로 써야함
#                 elif arr[cr][cc] < mean:
#                     arr[cr][cc] += 1
#
#
# R, C, T = map(int, input().split())
# arr = [deque()] + [deque(list(map(int, input().split()))) for _ in range(R)]
# ops = [tuple(map(int, input().split())) for _ in range(T)]
#
# for x, d, k in ops:
#
#     # [1] 회전
#     if d == 0:
#         d = 1
#     else:
#         d = -1
#     for i in range(x, R+1, x):
#         arr[i].rotate(d*k)
#
#     # [2] 인접부분 확인
#     bfs()
#
#     # for q in arr[1:]:
#     #     print(q)
#     # print()
#
# print(sum(map(sum, arr[1:])))