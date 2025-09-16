"""
[2차 풀이]

NM -> RC

1열에 설치 되어있음

1. 먼지가 4방향으로 확신됨,
    oob거나  시공돌풍있으면 그곳으로는 확산안됨
    //5
    원래칸의 먼지양은 확산된 먼지만큼 줄어듦
    확산 먼지는 모든 먼지 확산 끝난 다음 더해짐 nm 사용

2. 시공돌풍이 청소 시작 (두칸을 차지)
    윗칸은 반시계
    아래칸은 시계로 돎

    먼지가 한칸씩 이동함
    나오는 바람은 깨끗한 바람
    들어오는 바람은 0이 됨

    원래 자리(0)에서 rotate하고
    원래 자리에 들어온 먼저를 0으로 만들어주자

R*C (50*50) *1000
"""


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def init():
    for cr in range(R):  # 두칸 이므로 먼저 나오는 칸이 윗칸, 그 아래가 아랫칸
        if m[cr][0] == -1:
            up = (cr, 0)
            down = (cr + 1, 0)
            # 0으로도 만들어 줘야함
            m[cr][0] = 0
            m[cr + 1][0] = 0
            break  # 맨 위만 찾고 break

    top = [up]
    cr, cc = up
    for cd in [0, 1, 2, 3]:
        while True:
            dr, dc = ds[cd]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or (nr, nc) == up:
                break  # while break하고 다음 방향으로
            top.append((nr, nc))
            cr, cc = nr, nc

    bot = [down]
    cr, cc = down
    for cd in [0, 3, 2, 1]:
        while True:
            dr, dc = ds[cd]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or (nr, nc) == down:
                break  # while break하고 다음 방향으로
            bot.append((nr, nc))
            cr, cc = nr, nc

    return top, bot


def spread():
    added = [[0 for _ in range(C)] for _ in range(R)]

    for cr in range(R):
        for cc in range(C):
            val = m[cr][cc]
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc) or (nr, nc) == top[0] or (nr, nc) == bot[0]:  # 범위 벗어나거나, 돌풍위치라면 건너뜀
                    continue
                added[nr][nc] += val // 5
                m[cr][cc] -= val // 5  # 더해준 만큼 crcc에서 빼줌
    for cr in range(R):
        for cc in range(C):
            m[cr][cc] += added[cr][cc]  # added에 더해뒀던걸 더해줌

    return


def clean():
    # 초기엔 시공돌풍위치 0인 상태
    tmp = []
    for idx in range(len(top)):
        cr, cc = top[idx]
        nr, nc = top[(idx + 1) % len(top)]  # 다음 위치
        tmp.append((nr, nc, m[cr][cc]))  # 다음 위치에 현재 위치의 먼저를 넣어줌
    for idx in range(len(bot)):
        cr, cc = bot[idx]
        nr, nc = bot[(idx + 1) % len(bot)]  # 다음 위치
        tmp.append((nr, nc, m[cr][cc]))  # 다음 위치에 현재 위치의 먼저를 넣어줌

    for cr, cc, a in tmp:
        m[cr][cc] = a
    # 시공 돌풍 위치는 0으로 만들어줌
    m[top[0][0]][top[0][1]] = 0  # top[0]이 청소기의 위치
    m[bot[0][0]][bot[0][1]] = 0
    return


def solve():
    for _ in range(T):
        spread()
        # for l in m:
        #     print(l)
        clean()
        # for l in m:
        #     print(l)
    res = sum(map(sum, m))

    return res


ds = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 0우 1상 2좌 3하
R, C, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]  # 시공돌풍 위치는 0으로 만들어주자
top, bot = init()  # top[0], bot[0]은 시공돌풍의 위치, 나머지는 다음 경로들

ans = solve()
print(ans)


# ---------------------- 1차 풀이 -----------------------
# """
# [요약평]
# 1. 배열 돌리기 같은 문제 연습,, (회전용 배열 만드는 전처리가 너무 오래걸림)
#  => 돌리기 문제는 종이에 한번 그려보자 (돌리기 + 처리 로직 둘다)
# 2. 중간에 구상의 변화가 생겼을때 어떻게 다른 로직을 같이 잘 수정할 수 있을지 고민
# 
# [타임라인]
# 이해 및 구상 : 9분
# 구현 및 디버깅 : 37분 (20분 이상을 돌리기에서 사용...)
# 
# [이해 및 구상]
# -) 회전용 좌표 리스트를 출력으로만 보려다보니 확신이 안서서 오래 들여다봄
#     종이에 그려보는게 단축에 더 좋았을 듯
# +) 회전용 좌표 리스트를 만드는 아이디어 자체는 좋았음
# 
# [구현]
# -) 구상했던 구현 방식에 수정이 생기면서 수정할 것은 없는지 확인하느라 시간이 오래걸림
# -) new_top.reverse()이게 굳이 필요했나 싶음 (어차피 new_top, top 둘다 만들건데)
# +) 방향 배열 하나 만들어서 위아래 같이 사용하기 위해 [0, 1, 2, 3] [0, 3, 2, 1]로 사용
# +) top = new_top[1:] + [new_top[0]] 로 빠르게 작성 (for문대신)
# 
# [디버깅]
# -) 에러 떴다면 몇번째 라인에서 뜬건지를 확인하자...
#     cr, cc = bottom[i]              # (D) top
#     여기서도 시간 한참 사용
# +) 문제 특성상 arr을 출력하면 쉽게 디버깅은 가능했음
# 
# [시간 복잡도]
# N**2*T = 2500000
# 
# 안퍼지는 조건을 좀더 신경썼으면 좋았을 듯
# if arr[cr][cc] == 0:         # (D) <5로하면 빠를듯
#     continue
# 
# 
# -----
# 총 46분
# 
# """
# 
# """
# 구상 과정
# 확산 규칙 이해
# 공기청정기는 움직이지 않음
# 청정기 위치 m으로 받아오자
# 회전은 회전이 이뤄지는 좌표들로 관리 (계속사용되므로)
# (마지막에 공기청정기 위치 더해주면 안됨)
#     => 0으로 바꾸는 것으로 수정했음
# 
# 50*50*1000 가능할듯
# """
# 
# def oob(r, c):
#     return not (0<=r<R and 0<=c<C) # (D) c를 R로 씀 (빠르게 찾음)
# 
# def spread():
#     plus = [[0]*C for _ in range(R)]
#     for cr in range(R):
#         for cc in range(C):
#             if arr[cr][cc] < 5: # 시간 비교용 제출
#             # if arr[cr][cc] == 0:         # (D) <5로하면 빠를듯
#                 continue
#             a = arr[cr][cc] // 5
#             for dr, dc in ds:
#                 nr, nc =  cr+dr, cc+dc
#                 if oob(nr, nc) or ((nr, nc) in [(m[0], 0), (m[1], 0)]):
#                     continue
#                 arr[cr][cc] -= a
#                 plus[nr][nc] += a
#     for cr in range(R):
#         for cc in range(C):
#             arr[cr][cc] += plus[cr][cc]
# 
# def rotate():
#     for i in range(len(new_top)):
#         nr, nc = new_top[i]
#         cr, cc = top[i]
#         arr[nr][nc] = arr[cr][cc]
# 
#     arr[m[0]][0] = 0
#     arr[m[0]][1] = 0                    # (D) 새바람도 0
#     for i in range(len(new_bottom)):
#         nr, nc = new_bottom[i]
#         cr, cc = bottom[i]              # (D) top
#         arr[nr][nc] = arr[cr][cc]
#     arr[m[1]][0] = 0
#     arr[m[1]][1] = 0                    # (D) 새바람도 0
# 
# 
# R, C, T = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(R)]
# 
# # ---------- 전처리 -----------
# m = []  # 청정기 좌표
# for zr in range(R):
#     if arr[zr][0] == -1:
#         m.append(zr)
#         arr[zr][0] = 0
# 
# ds = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 동북서남
# 
# new_top = []
# cr, cc = m[0], 0
# for zd in [0, 1, 2, 3]:
#     while True:
#         dr, dc = ds[zd]
#         nr, nc = cr+dr, cc+dc
#         if oob(nr, nc) or nr>m[0]:
#             break
#         new_top.append((nr, nc))
#         cr, cc = nr, nc
# new_top.reverse()
# top = new_top[1:] + [new_top[0]]
# 
# new_bottom = []
# cr, cc = m[1], 0
# for zd in [0, 3, 2, 1]:
#     while True:
#         dr, dc = ds[zd]
#         nr, nc = cr+dr, cc+dc
#         if oob(nr, nc) or nr<m[1]:
#             break
#         new_bottom.append((nr, nc))
#         cr, cc = nr, nc
# 
# new_bottom.reverse()
# bottom = new_bottom[1:] + [new_bottom[0]]
# 
# for i in range(T):
#     spread()
#     rotate()
#     # for l in arr:
#     #     print(l)
#     # print()
# 
# print(sum(map(sum, arr)))