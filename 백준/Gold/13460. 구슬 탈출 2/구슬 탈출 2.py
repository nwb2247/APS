"""
[2차 풀이]

NM -> RC
사탕은 다른 사탕, 벽에 부딪히기 전까지 미끄러짐

빨간색 사탕이 밖으로 나와야함
파란색이 먼저 나오거나 동시에 나오는 것 안됨

빨강, 파랑이 동일한 위치로 오는 경우는 어떻게 진행해도 똑같으므로 동일
=> 백트래킹 대신 BFS를 사용하자 (최소 횟수)

바깥 부분은 다 막혀있으므로 oob 신경안써도 됨

구멍일때는 막히는 거 없이 나와야하므로 구멍인지 먼저 확인하고 그 다음에 벽이나 구슬인지 확인하자

뭘먼저 움직일지 정해야함
"""
from collections import deque


def dprint(crr, crc, cbr, cbc, cnt):
    print(crr, crc, cbr, cbc, cnt)
    tmp = [lst[:] for lst in arr]
    if (crr, crc) != (er, ec):
        tmp[crr][crc] = "R"
    if (cbr, cbc) != (er, ec):
        tmp[cbr][cbc] = "B"
    for l in tmp:
        print(*l)
    print()


def init():
    global rr, rc, br, bc, er, ec
    for cr in range(R):
        for cc in range(C):
            if arr[cr][cc] == "R":
                rr, rc = cr, cc
                arr[cr][cc] = "."
            elif arr[cr][cc] == "B":
                br, bc = cr, cc
                arr[cr][cc] = "."
            elif arr[cr][cc] == "O":
                er, ec = cr, cc
    return


def tilt(crr, crc, cbr, cbc, cd):
    red_first = False
    if ((cd == 0 and crr < cbr) or  # 상 # 움직이는 방향을 기준으로 맨끝과 더 가깝다면 먼저 움직임
            (cd == 1 and crr > cbr) or  # 하
            (cd == 2 and crc < cbc) or  # 좌
            (cd == 3 and crc > cbc)):  # 우
        red_first = True

    nrr, nrc, nbr, nbc = crr, crc, cbr, cbc
    dr, dc = ds[cd]
    if red_first:  # 빨강 먼저 움직이는 경우
        cr, cc = crr, crc  # 빨강 움직임
        while True:
            nr, nc = cr + dr, cc + dc
            if arr[nr][nc] == "O":
                nrr, nrc = er, ec
                break
            elif arr[nr][nc] == "#":
                nrr, nrc = cr, cc
                break
            else:
                cr, cc = nr, nc
        cr, cc = cbr, cbc  # 파랑 움직임
        while True:
            nr, nc = cr + dr, cc + dc
            if arr[nr][nc] == "O":  # nrr, nrc와 같은지 확인하는 것보다, 구멍인지 확인하는게 우선 (그래야 빠질 수 있음)
                nbr, nbc = er, ec
                break
            elif arr[nr][nc] == "#" or (nr, nc) == (nrr, nrc):  # 벽이거나 빨강과 부딪힌다면
                nbr, nbc = cr, cc
                break
            else:
                cr, cc = nr, nc
    else:  # 파랑 먼저 움직이는 경우
        cr, cc = cbr, cbc  # 파랑 움직임
        while True:
            nr, nc = cr + dr, cc + dc
            if arr[nr][nc] == "O":
                nbr, nbc = er, ec
                break
            elif arr[nr][nc] == "#":
                nbr, nbc = cr, cc
                break
            else:
                cr, cc = nr, nc

        cr, cc = crr, crc  # 빨강 움직임
        while True:
            nr, nc = cr + dr, cc + dc
            if arr[nr][nc] == "O":  # nrr, nrc와 같은지 확인하는 것보다, 구멍인지 확인하는게 우선 (그래야 빠질 수 있음)
                nrr, nrc = er, ec
                break
            elif arr[nr][nc] == "#" or (nr, nc) == (nbr, nbc):  # 벽이거나 파랑과 부딪힌다면
                nrr, nrc = cr, cc
                break
            else:
                cr, cc = nr, nc

    return nrr, nrc, nbr, nbc


def solve():
    global rr, rc, br, bc

    res = -1
    v, q = set(), deque()  # 빨간공, 파란공의 위치를 기준으로 방문 처리, 빨간공파란공의 위치가 동일한 경우는 두번 봐줄 필요 없음
    v.add((rr, rc, br, bc))
    q.append((rr, rc, br, bc, 0))  # 0: 몇번 tilt했는지
    while q:
        crr, crc, cbr, cbc, cnt = q.popleft()
        # dprint(crr, crc, cbr, cbc, cnt)

        if cnt > 10:  # 이미 10을 넘어가기 시작했다면 -1 반환해야하므로 break
            break
        if (cbr, cbc) == (er, ec):  # 파란색이 빠졌다면 (혼자 or 빨간색과 동시에)
            continue
        if (crr, crc) == (er, ec):  # 파란색은 빠지지 않았는데, 빨간색만 빠졌다면
            res = cnt
            break

        for cd in range(4):
            nrr, nrc, nbr, nbc = tilt(crr, crc, cbr, cbc, cd)  # 현재 위치 + 방향을 기준으로 기울여줌
            if (nrr, nrc, nbr, nbc) in v:
                continue
            v.add((nrr, nrc, nbr, nbc))
            q.append((nrr, nrc, nbr, nbc, cnt + 1))

    return res


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]  # # 벽, O 구멍, 구슬은 지워줌
rr, rc = 0, 0
br, bc = 0, 0
er, ec = 0, 0
init()
# print((rr, rc), (br, bc), (er, ec))

ans = solve()
print(ans)


# """
# [1차 풀이]
#
# [반드시 다시 풀기]
#
# [요약평]
# - 이걸 왜 백트래킹으로 풀었는지???
#     "최소 몇번 만에 빼낼 수 있는지"를 보고 처음엔 BFS를 먼저생각했는데,
#     어떤 것을 기준으로 방문처리를 해줘야하는지 생각했으나 쉽게 떠오르지 않음
#     처음에는 각 기울인 방법?을 튜플로 담아 (최대 10자리) set에 담으면서 방문처리할까 생각했는데,
#     그럴거면 백트래킹이랑 다를바가 없다고 생각해서 백트래킹으로 진행
#
#     => 문제의 핵심은 기울인 방법을 방문 기준으로 하는게 아니라, 빨간공과 파란공의 위치 (즉 4차원)을 방문 기준으로 삼아야 했음
#     => 경험했던 방식이 아니다 보니 쉽게 떠오르지 않았음.... 10**4라서 충분히 가능.... (물론 비트마스킹등도 있긴함..)
#
# - arr에 표시하는 것이 구현에 방해가 된다면, 맵은 비워두고, 디버깅시에만 맵에 표시해주는 방법을 써야함... (연습필요)
#     ex) 파란공과 빨간공 한 위치 동시에 오는 경우
#
# - 방향 인덱스를 이용한 일반화해서 기울인 것은 좋았음..
# # //2 == 0 : 종방향
# # //2 == 1 : 횡방향
# # %2 == 0 : 감소방향 => 감소방향이면 작은게 더 우선
# # %2 == 1 : 증가방향 => 증가방향이면 큰게 더 우선
#     => 떠오르지 않는다면 한방향으로 이동하는 것을 만들고 배열을 회전하는 것도 좋음 (시간 상 문제가 없다면...)
#
# - 구현량 많아지다 보니 말도 안되는 실수를 함 (cd%1 == 0등..),
#     머리가 뜨거워질때 집중력 되찾는 연습 해야함
# - 마찬가지로 구현량이 많아지다보니 종료조건, 실패조건 등 적어둔 것을 놓침
# => 글로 작성가능한 부분은 손구상 말고 주석 구상으로 시작하고, 도형 등만 손구상하자..
#
# [타임라인]
# 이해 및 구상 18분
# 구현 및 디버깅 110분
# -----
# 총 128분
#
# [이해 및 구상]
# -) 글씨가 나빠서 손구상으로 보는게 한계가 있음 -> 주석 구상과 함께 사용
# +) 실수 가능한 부분들을 최대한 많이 생각해냄
#
# [구현 및 디버깅]
# -) 멥에 바로 표시해서 디버깅을 효과적으로 하기 위해 draw라는 좌표바꿔찍는 함수를 써보려고 했는데,
#     구멍에 파란거 빨간거 동시에 들어오는 것을 처리하는게 너무 어려웠음
# +) 상하좌우 인덱스를 이용한 일반화 (상좌의 경우에 %2==0인것을, -1로만 바꿔주는 처리한다면...)
#
# [백트래킹 시간복잡도]
# 4**10 * max(R, C) # 빨강, 파랑을 최대 max(R, C만큼 이동시킬 수 있으므로...)
#
# 싹 지우고 BFS로 다시 풀어보자
# """
# """
# 손구상 내용
# 빨강 , 파랑 동일 이동시에 같이 빠져나와도 실패
# 빨강만 빠져 나와야함
#
# 바깥행, 렬은 모두 막혀 있음
#
# tilt() : red blue만을 움직이는 방식으로
#
# red, blue 움직히는 방향쪽에서 더 앞에 있는 것을 먼저 움직임 (일렬, 일렬X 모두 동일)
#
# K = 10 (K번이하로만 움직일 수 있음)
# ans = K+1로 초기화하고
# 마지막에도 K+1이면 -1
# depth를 0부터 시작 (직전에 몇번 움직였는지..)
#
# (D) (종료조건 : 파란색이 들어가면 실패)
#
# 종료 조건 [1] 타겟과 동일하다면 종료
# 종료 조건 [2] 10 직전에 10번 움직였는데 아직도 다르면 종료
#
# 순서 안바뀌게 주의
#
# # 일땐 막히고, O일땐 거기에 멈춰야함
# O일때는 R, B는 원래 위치에서 없애고 새로운 자리에는 표시하지 않음
# (D) 위치표시는 디버깅시에만 사용하고, arr에는 표시하지 말자.. (원상복구가 더 복잡해짐;;)
#
#
# red, blue 위치를 항상 기억
# """
#
# ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
#
#
# # //2 == 0 : 종방향
# # //2 == 1 : 횡방향
# # %2 == 0 : 감소방향 => 감소방향이면 작은게 더 우선
# # %2 == 1 : 증가방향 => 증가방향이면 큰게 더 우선
#
# # pos 에 위치한 것을 cd 방향으로 옮겨줌. (단 x에는 위치할 수 없음)
# def move(pos, cd, x):  # x: 불가한 자리 (먼저 간 애)
#     dr, dc = ds[cd]
#     cr, cc = pos
#     while True:
#         nr, nc = cr + dr, cc + dc
#         if (nr, nc) == target:  # nr, nc가 구멍이라면 구멍으로 옮기고 return
#             return nr, nc
#
#         # 벽이거나 다른 공이라면, 옮기고 return
#         if arr[nr][nc] == "#":
#             return cr, cc
#         if arr[nr][nc] == "." and (nr, nc) == x:
#             return cr, cc
#
#         cr, cc = nr, nc
#
#
# # 기울이기, 빨강, 파랑, 방향 정보를 받고 새 빨강, 새 파랑 좌표를 반환
# def tilt(red, blue, cd):
#     blue_first = 0  # 0이면 red먼저 1이면 blue먼저 움직임
#     # (D) blue_first라써야하는데 red_first라 쓰고 빨강을 먼저 넣어줌
#     if cd % 2 == 0:  # 감소방향이면 (상좌)
#         if blue[cd // 2] < red[cd // 2]:  # 각 방향에 대한 종횡 방향을 생각해서 넣어줌
#             blue_first = 1
#     else:  # 증가방향이면 (하우)            # (D) if cd%1 == 0 으로 쓰는 어처구니 없는 짓을 함 (cd%2 == 1)라고 쓰려다가 마음이 급했었던듯
#         if blue[cd // 2] > red[cd // 2]:
#             blue_first = 1
#     # 아예 red, blue가 같은 경우는 없으므로 등호조건 고려 안해도 OK
#
#     if blue_first:  # 파랑 먼저 움직여야 한다면
#         nblue = move(blue, cd, (-1, -1))
#         nred = move(red, cd, nblue)
#     else:
#         nred = move(red, cd, (-1, -1))
#         nblue = move(blue, cd, nred)
#
#     return nred, nblue
#
#
# def backtrack(depth, red, blue):
#     global ans
#
#     if depth >= ans:  # 가지치기 (먼저 찾은 ans보다 같거나 크면)
#         return
#
#     if blue == target:  # (D) 파랑이 구멍에 떨어지면 실패처리해야하는데 하지 않음!!!!!!!!!!!!!!!!!!
#         return
#
#     if red == target and blue != target:  # 종료조건 [1]
#         ans = min(ans, depth)  # min 안전하게 쓰자 일단
#         return
#
#     if depth == K:  # 종료조건 [2] # 가지치기 와 합칠 수 있는지..?
#         return
#
#     for cd in range(4):
#         # [1] 일단 새 위치 구함 + 지도에 반영해줌
#
#         nred, nblue = tilt(red, blue, cd)
#
#         # [2] 하부 재귀 호출
#         if v[nred[0]][nred[1]][nblue[0]][nblue[1]] > depth + 1:
#             v[nred[0]][nred[1]][nblue[0]][nblue[1]] = depth + 1
#             backtrack(depth + 1, nred, nblue)
#
#
# R, C = map(int, input().split())
# K = 10
# arr = [list(input()) for _ in range(R)]
# r = (-1, -1)
# b = (-1, -1)
# target = (-1, -1)
#
# for zr in range(R):
#     for zc in range(C):
#         if arr[zr][zc] == "R":
#             arr[zr][zc] = "."
#             r = (zr, zc)
#         if arr[zr][zc] == "B":
#             arr[zr][zc] = "."
#             b = (zr, zc)
#         if arr[zr][zc] == "O":
#             target = (zr, zc)
#
# # (R) [rr][rc][br][bc] 빨강과 파랑의 현재 위치를 몇번의 횟수만에 도달했었는지
# v = [[[[K + 1 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
#
# ans = K + 1
# backtrack(0, r, b)
# if ans == K + 1:
#     print(-1)
# else:
#     print(ans)
#
