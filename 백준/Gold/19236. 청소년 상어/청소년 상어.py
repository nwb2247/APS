"""
[2차 풀이] -> [3차 반드시 다시 풀기]

- 1차는 문제에서 빼먹은 부분이 있어서 틀렸던 문제
- 2차 어느시점에서 어떤 부분을 원복할건지 명확히 잡아야함 (구상단계에서 된다면 더 바람직)

술래
 도둑 잡을때마다 도둑의 방향을 가짐

 r, c

 1~16의 번호가 매겨져 있음

- 술래가 0, 0 말을 잡으면서 시작
- 도둑말은 번호 작은 순서대로 본인이 가지고 있는 이동방향대로 한칸 이동
    술래나, 격가밖은 이동 불가
    이동할 수 있을때까지 45도 반시계 회전
    이동할 수 있는 칸이 없다면 이동하지 않음
    이동시 도둑말이 있다면 해당 말과 위치를 바꿈

- 도둑말의 이동이 모두 끝나면 술래말이 이동
    술래는 이동 가능 방향의 어느칸이나 이동가능 (여러칸도 이동가능)
    도착말 말고 지나가는 말들은 잡지 않음
    도둑말이 없는 곳으로는 이동할 수 없음

- 술래말이 이동할 수 있는 곳에 도둑말이 더 이상 존재하지 않으면 게임 종료

- 점수는 해당말의 번호만큼 획득
- 얻을 수 있는 점수의 최댓값 출력
"""


def dprint():
    ddd = ["", "↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]
    tmp = [[str() for _ in range(N)] for _ in range(N)]
    for cr in range(N):
        for cc in range(N):
            if len(mmap[cr][cc]) == 0:
                tmp[cr][cc] = ".".rjust(5)
            else:
                idx = list(mmap[cr][cc])[0]
                tmp[cr][cc] = f"{idx}:{ddd[info[idx][2]]}".rjust(5)
    for l in tmp:
        print(*l)


def init():
    global zr, zc, zd, fidx
    arr = [list(map(int, input().split())) for _ in range(4)]
    for cr in range(4):
        for cc in range(4):
            idx, d = arr[cr][2 * cc], arr[cr][2 * cc + 1]
            info[idx] = [cr, cc, d]
            mmap[cr][cc].add(idx)

    # [0] 0, 0 도둑잡기
    idx = list(mmap[0][0])[0]  # 0, 0의 도둑번호
    zd = info[idx][2]  # 방향가져오고
    info[idx] = []  # 없앰
    mmap[0][0].remove(idx)
    fidx = idx

    return


# ------------------------------ 함수 -----------------------------
def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def move():
    for idx in range(1, 16 + 1):
        if not info[idx]:
            continue
        cr, cc, cd = info[idx]
        for i in range(cd, cd + 8):
            td = (i - 1) % 8 + 1
            dr, dc = ds[td]
            tr, tc = cr + dr, cc + dc
            if oob(tr, tc) or (tr, tc) == (zr, zc):
                continue
            if len(mmap[tr][tc]) != 0:
                old = list(mmap[tr][tc])[0]
                mmap[tr][tc].remove(old)
                mmap[cr][cc].add(old)
                info[old][0], info[old][1] = cr, cc
            # 원래 위치에 있던 없던 idx는 옮겨 줘야함
            mmap[cr][cc].remove(idx)
            mmap[tr][tc].add(idx)
            info[idx] = [tr, tc, td]
            break

    return


def backtrack(score):
    global info, mmap, zr, zc, zd, ans

    ans = max(ans, score)

    move()
    ozr, ozc, ozd = zr, zc, zd
    origin_info = [lst[:] for lst in info]
    origin_mmap = [[mmap[cr][cc].copy() for cc in range(N)] for cr in range(N)]

    dr, dc = ds[zd]
    for l in range(1, 4):   # 최대 3칸까지 나아갈수 있음..
        nzr, nzc = ozr + dr * l, ozc + dc * l
        if oob(nzr, nzc):       # oob면 더이상 못감
            break
        if len(mmap[nzr][nzc]) == 0:  # 비어 있으면 갈 수 없는 칸
            continue

        # [1] idx 꺼내서 없애줌
        idx = list(mmap[nzr][nzc])[0]
        # print("before", idx)
        # dprint()
        zr, zc, zd = nzr, nzc, info[idx][2]  # [2]가 방향
        info[idx] = []
        mmap[nzr][nzc].remove(idx)

        # [2] 하부 재귀 호출
        backtrack(score + idx)

        # [3] 원복
        # 하부 재귀에 의해 move가 실행되고, mmap과 info가 싹 바뀐다... 전부 빡센 원복이 필요
        # 단순히 info[idx], mmap[nzr][nzc]만 바꾸는 것으로는 복구 안됨
        zr, zc, zd = ozr, ozc, ozd
        info = [lst[:] for lst in origin_info]
        mmap = [[origin_mmap[cr][cc].copy() for cc in range(N)] for cr in range(N)]

        # print("after", idx) # 원복 확인용
        # dprint()

    return


def solve():
    backtrack(fidx)
    return


ds = [None, (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
N = 4
info = [[] for _ in range(17)]  # 0이면 잡힌것, 1~8까지가 방향
mmap = [[set() for _ in range(N)] for _ in range(N)]
zr, zc, zd = 0, 0, 0
fidx = 0

init()

ans = 0
solve()
print(ans)

# ----------------------------------1차풀이--------------------------------------
# """
# [반드시 다시 풀기]
#
# - 문제를 잘 읽고, 차분히 검증하고 제출
# - 시뮬 + 백트래킹에서 각 정보를 어떻게 갱신하고, 넘기고, 원복할건지 생각해야함
#
#
# [타임라인]
# 이해 및 구상 22분
# 구현 60분
# 구상 디버깅 27분
# ---------------------------------
# 총 109분
#
# [이해 및 구상]
#
# [구현]
# -) FINFO 변수명 불편
# +) 시뮬 + 백트래킹에서 각 정보를 어떻게 갱신하고, 넘기고, 원복할건지 생각
#     인자로 넘길건지, global에서 관리 할건지, 어떤 것을 원복할건지...
#
# 4*4
# 물고기는 번호와 방향
# 한칸에는 한마리씩 존재
# 1~16
# 상하좌우 대각선
#
# 상어방향은 0,0 물고기를 먹고 0,0에 들어감 방향과 같아짐
# 그 이후 물고기 이동
#
# 물고기는 작은 순서대로 이동
#     물고기는 한칸이동
#     이동 가능 : 빈칸, 다른 물고기
#     불가능 : 경계,  상어 있는 곳
#     (이동 가능칸을 향할때까지 45도반시계 회전)
#     이동할칸 없으면 이동하지 않음 (8방향 다보고도)
#     for brealk
#
#     물고기가 다른 물고기가 있는 곳으로 갈땐 서로의 위치를 바꿈
#
# 그 다음 상어 이동
#     한번에 여러개의 칸을 이동가능 (그 방향으로 쭉 선택가능)
#     물고기 있는 칸으로 이동했다면
#         물고기 먹으면 그 물고기의 방향을 가짐
#         이동중에 지나치는 물고기 먹지 않음
#     물고기가 없는 칸으로 이동했다면
#         방향 유지
#     이동할 수 있는 칸이 없다면 종료
#
# 위 과정을 반복
# """
# ds = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}
#
# M = [[0] * 4 for _ in range(4)]
#
# FINFO = [None] + [()] * 16
# for ZR in range(4):
#     inp = list(map(int, input().split()))
#     for ZC in range(4):
#         NUM, D = inp[2 * ZC], inp[2 * ZC + 1]
#         M[ZR][ZC] = NUM
#         FINFO[NUM] = (ZR, ZC, D)  # 0 1위치, 2 방향
#
# # SR, SC = 0, 0
# # 상어의 번호는 -1으로 표시..
# # 빈칸은 0으로 표시
# SR, SC = 0, 0
# first = M[SR][SC]
# SD = FINFO[first][2]
# M[SR][SC] = -1
# FINFO[first] = None
#
#
# def oob(r, c):
#     return not (0 <= r < 4 and 0 <= c < 4)
#
#
# def fish(m, finfo):
#     nm = [lst[:] for lst in m]
#     nfinfo = finfo[:]
#
#     for num in range(1, 16 + 1):  # (I) 16
#         if nfinfo[num] is None:  # 죽었으면
#             continue
#
#         cr, cc, cd = nfinfo[num]
#         for nd in list(range(cd, 9)) + list(range(1, cd)):
#             dr, dc = ds[nd]
#             nr, nc = cr + dr, cc + dc
#             if oob(nr, nc) or nm[nr][nc] == -1:
#                 continue  # 이동 못하면 반시계 45도 회전
#             else:
#                 break
#         else:  # 이동 가능 칸이 없다면 아무것도 안함
#             continue
#         # [이동]
#         if nm[nr][nc] == 0:
#             nm[nr][nc] = num
#
#             nfinfo[num] = (nr, nc, nd)
#             nm[cr][cc] = 0
#         elif 1 <= nm[nr][nc] <= 16:  # 물고기 칸
#             other = nm[nr][nc]
#             nfinfo[other] = (cr, cc, nfinfo[other][2])
#             nfinfo[num] = (nr, nc, nd)
#             nm[nr][nc], nm[cr][cc] = num, other
#
#     return nm, nfinfo
#
# def shark(sr, sc, sd, m, finfo): # (D) 물고기가 없는 칸은 이동못함
#     dr, dc = ds[sd]
#     tmp = []
#     nr, nc = sr + dr, sc + dc
#     while not oob(nr, nc):
#         if m[nr][nc] != 0:
#             tmp.append((nr, nc))
#         nr += dr
#         nc += dc
#     return tmp
#
#
# def backtrack(score, m, finfo, sr, sc, sd):
#     global ans
#
#     nm, nfinfo = fish(m, finfo)
#
#     lst = shark(sr, sc, sd, nm, nfinfo)
#
#     if len(lst) == 0:
#         ans = max(ans, score)
#         return
#
#     for nsr, nsc in lst:
#         if nm[nsr][nsc] == 0:  # 빈칸이라면
#             nm[nsr][nsc], nm[sr][sc] = -1, 0
#             backtrack(score, nm, nfinfo, nsr, nsc, sd)
#             nm[nsr][nsc], nm[sr][sc] = 0, -1  # 원복
#         else:  # 물고기가 있다면
#             num = nm[nsr][nsc]
#             num_info = nfinfo[num]
#
#             nm[nsr][nsc], nm[sr][sc] = -1, 0
#             nfinfo[num] = None
#
#             backtrack(score + num, nm, nfinfo, nsr, nsc, num_info[2])
#
#             nm[nsr][nsc], nm[sr][sc] = num, -1  # 원복
#             nfinfo[num] = num_info
#
#
# ans = first
# backtrack(first, M, FINFO, SR, SC, SD)
# print(ans)
