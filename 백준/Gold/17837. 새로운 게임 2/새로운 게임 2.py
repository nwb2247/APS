"""
[2차 풀이]
- 1, 1로 주어진다면 패딩하자
- 디버깅 눈에 보기 쉽게 , rjust, 방향 표시
- 파란색에 왔을때, 다음 이동이 빨강, 흰색일때 어떻게 이동할지도 고려
- 4개 완성 즉시, 게임 종료 => global end로 관리

[이해 및 구상]

N*N
말 1~K번 까지, 순서대로 이동


이동하려는 칸이 흰색인 경우 해당칸으로 이동

이동하려는 칸이 흰색
    해당 칸으로 이동,
    이동하려는 칸에 말이 이미 있는 경우
        그 위로 올려둠
빨간색
    이동하기 전 순서를 뒤집음
    이동하려는 칸에 말이 이미 있는 경우
        그 위로 올려둠
파란색인 경우
    파란색으로 이동하지 않고 방향 전환
    한번 더 이동시도, 이동하려는 칸이 파란색이면
        가만히 있음
    파란색 아니면 이동

oob -> 파란색과 동일하게 처리
1, 1부터 시작이므로 그냥 패딩하자

4개가 되는 순간 즉시 게임을 종료

출력 : 게임이 종료되는 순간의 턴 번호
1000을 넘어가면 -1을 출력

입력에서는 같은 칸에 두말이 주어지지 않음

"""

ddd = [" ", "우", "좌", "상", "하"]


class Unit:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d

    def __repr__(self):
        return f"[r:{self.r} c:{self.c} d:{ddd[self.d]}]"


def init():
    for idx in range(1, K + 1):
        r, c = info[idx].r, info[idx].c
        mmap[r][c].append(idx)


def dprint():
    for i in range(1, K + 1):
        print(f"{i}:{info[i]}", end=" / ")
    print()
    for l in mmap[1: N + 1]:
        print(*map(lambda x: str(x).rjust(5), l[1:N + 1]))
    for l in color[1:N + 1]:
        print(*map(lambda x: str(x).rjust(2), l[1:N + 1]))
    print("----------------------------------------------------")

    return


def move_upper(cr, cc, nr, nc, pos, reverse):
    global end
    # [1] 옮길거 떼놓기
    moving = mmap[cr][cc][pos:]

    # [2] 빨강이면 역순
    if reverse:
        moving.reverse()

    # [3] mmap에 반영 cr, cc에선 떼주고 nr, nc엔 붙이기
    mmap[cr][cc] = mmap[cr][cc][:pos]
    mmap[nr][nc].extend(moving)

    # [4] info에도 위치 반영
    for idx in moving:
        info[idx].r, info[idx].c = nr, nc
    if len(mmap[nr][nc]) >= 4:
        end = True


def move(idx):
    cr, cc, cd = info[idx].r, info[idx].c, info[idx].d
    pos = mmap[cr][cc].index(idx)

    nr, nc = cr + ds[cd][0], cc + ds[cd][1]

    if color[nr][nc] == 0:
        move_upper(cr, cc, nr, nc, pos, reverse=False)
    elif color[nr][nc] == 1:
        move_upper(cr, cc, nr, nc, pos, reverse=True)
    elif color[nr][nc] == 2:  # 파랑이라면
        nd = rev[cd]
        nr, nc = cr + ds[nd][0], cc + ds[nd][1]
        info[idx].d = nd  # nd는 바로 바꿔줌
        if color[nr][nc] == 0:
            move_upper(cr, cc, nr, nc, pos, reverse=False)
        elif color[nr][nc] == 1:
            move_upper(cr, cc, nr, nc, pos, reverse=True)
        # 2(파란색)이라면 그냥 제자리에 있자

    return


def solve():
    turn = 1
    while True:
        if turn == 1000 + 1:
            break
        for idx in range(1, K + 1):
            move(idx)
            if end:  # 1턴이 끝나기 전이라도, 4개 이상 겹치는 경우가 생긴 경우에는 즉시 종료
                break
        if end:
            break
        turn += 1
    if turn == 1000 + 1:
        print(-1)
    else:
        print(turn)

    return


ds = [(None, None), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 1우 2좌 3상 4하
rev = [None, 2, 1, 4, 3]
N, K = map(int, input().split())
color = [[2] * (N + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N + 2)]
info = [Unit(None, None, None)] + [Unit(*map(int, input().split())) for _ in range(K)]
mmap = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
init()

end = False
solve()


# ------------------------- 1차 -----------------------------
# """
# [시간나면 다시 풀기]
#
#
# - 문제에서 조건 분기를 제시하더라도 한차원 더 생각해야함 (분기의 순서 등)
# - 파란 칸에 부딪혀 이동하는 다음칸이 빨강, 횐색인 경우도 따로 분기해줘야함
#
# - 입력 및 전처리는 대문자로 받자
# - 지도는 m으로 쓰자, 유닛은 u로 씆자 (arr은 지도인지 유닛인지 헷갈림)
#
# - 구현 과정에서 구상이 바뀌는 것은 매우 자연스러운 일이니까 당황하지 않기
#     구상 변경 시 고려해야할 사항 정리 필요:
#         단순 복붙 자제.. 반환값에 대해서 고민
# - 이해 구상 주석에 적어두는 것은 실수 방지 + 큰 흐름 바꾸지 않기 위한 참고용
#     실제 구현은 문제를 직접 읽으면서 해야함
# - print, 디버거 찍어보기전에 무조건 문제 정독 + 코드 확인 부터 공들이고 시작
#
# - 함수화가 잘 됐다면 단위테스트는 모든 함수 다 짜고 해도되니까
#     흐름 끊길 것 같으면 테스트는 나중에하고 하기
#     (어차피 중간에 구상 변화 생기면 return 값 등 때문에 수정할요한 일이 생길 수 있음)
#
# - 시험때는 제출 전에 남은 시간 동안 계속 코드, 문제 보면서 검증해야함
#     연습때도 최소 20분은 확인하고 제출하자
#
# [타임라인]
# 이해 및 구상 15분
# 구현 43분
# 디버깅 24분
# 엣지 고민 코드, 문제 점검 18분
# ------------------
# 총 100분
#
# [이해 및 구상]
# +) 실수 사항, 큰 흐름 위주로 정리
#
# [구현]
# -) 구상 수정 과정에서 move_white, red를 추가하면서 return값을 그대로 두어서 문제 방생
#     구상 수정 과정에서 다른 부분을 어떻게 고쳐야하는지 잘 봐야함
# +) 구상 적어둔 것에 의존하지 않고 참고만, 구현에 집중
#
# [디버깅]
# -) 여전히 print에 의존함, 코드와 문제를 잘살피는 것이 우선
#
# [엣지 고민 코드, 문제 점검]
# 벽에 부딪히면서 새로운 것 계속 만나는 경우 고민해봄
# 입력 케이스에서 만들지는 못했지만 중간 과정을 보면서 예상대로 움직이는 지 확인
#
#
# """
#
# ds = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 우0 좌1 상2 하3
# rev = [1, 0, 3, 2] # 반대방향
# N, K = map(int, input().split())
# m = [list(map(int, input().split())) for _ in range(N)] # 0, 1, 2 지도
#
# # 말 정보
# u = [[[] for _ in range(N)] for _ in range(N)] # 각 위치에 어떤 유닛이 있는지 + 방향
# pos = [None] + [(-1, -1) for _ in range(K)] # 각 유닛이 현재 어디에 있는지 (유닛번호는 1부터 K)
# dirs = [None] + [0 for _ in range(K)] # 방향 정보 !!!!!! 움직일 때 위의 말들도 같이 움직이므로 같이 pos를 수정해야함
#
# # 좌표 방향 모두 -1 씩 받기
# for NUM in range(1, K+1): # 유닛 번호는 헷갈리니까 1부터 받자
#     CR, CC, CD = map(lambda x:int(x)-1, input().split())
#     u[CR][CC].append(NUM)
#     pos[NUM] = (CR, CC)
#     dirs[NUM] = CD
#
# # -------------- 함수 ----------------
#
# def oob(r, c):
#     return not(0<=r<N and 0<=c<N)
#
# def move_white(num, cr, cc, nr, nc):
#     lst = u[cr][cc][u[cr][cc].index(num):]  # num말 포함 위의 모든 말들
#     u[cr][cc] = u[cr][cc][:u[cr][cc].index(num)]  # num 아래 말들만 남김
#     u[nr][nc] = u[nr][nc] + lst
#     for i in lst:
#         pos[i] = (nr, nc)
#     return len(u[nr][nc])
#
# def move_red(num, cr, cc, nr, nc):
#     lst = u[cr][cc][u[cr][cc].index(num):]  # num말 포함 위의 모든 말들
#     u[cr][cc] = u[cr][cc][:u[cr][cc].index(num)]  # num 아래 말들만 남김
#     lst.reverse()  # INPLACE
#     u[nr][nc] = u[nr][nc] + lst
#     for i in lst:
#         pos[i] = (nr, nc)
#     return len(u[nr][nc])
#
# def move(num):
#     """
#     :param num: 현재 움직일 말 번호
#     :return: 4이상 쌓이는 순간 True 반환, 잘 진행되면 False 반환
#     """
#
#     # [1] 정보 가져오기
#     cr, cc = pos[num]
#     cd = dirs[num]
#
#     # [2] 이동하려는 칸 확인
#     dr, dc = ds[cd]
#     nr, nc = cr+dr, cc+dc
#     length = 0
#     if oob(nr, nc) or m[nr][nc] == 2:       # 벽이거나 파란 칸
#         cd = rev[cd]    # 역방향으로 바꿈
#         dirs[num] = cd  # dirs에도 반영
#         dr, dc = ds[cd]
#         tr, tc = cr+dr, cc+dc
#         if oob(tr, tc) or m[tr][tc] == 2: # 반대방향으로 한칸 이동한 것도 벽이거나 2라면
#             pass    # 이동하지 않고 가만히 있는다. (방향은 위에서 바꿨음)
#         elif m[tr][tc] == 0:
#             length = move_white(num, cr, cc, tr, tc)
#         elif m[tr][tc] == 1:
#             length = move_red(num, cr, cc, tr, tc)
#
#     elif m[nr][nc] == 0:
#         length = move_white(num, cr, cc, nr, nc)
#     elif m[nr][nc] == 1:
#         length = move_red(num, cr, cc, nr, nc)
#
#     if length >= 4:
#         return True
#     return False
#
# def solve():
#     turn = 1
#     while turn <= 1000: # 첫 루프 첫번째 턴, 1001번째 턴 되는 순간 종료 (마지막에 turn 더해줌)
#         # [1] 순서대로 움직이기
#         for num in range(1, K+1):
#
#             res = move(num)
#             # print(turn, num)
#             # for i in u:
#             #     print(i)
#             # print(pos)
#             # print(dirs)
#             # print()
#             if res:
#                 return turn
#
#         # [2] 턴 수 증가
#         turn += 1
#
#     return -1   # 1001번째 되면 -1 반환
#
# print(solve())
#
# """
# 조건 분기 : 문제에 나오는 그대로 하기
#
# [이해]
# N*N (흰, 빨, 피로 칠해져 있음)
# 말의 개수 K
# 하나의 말 위에 다른 말을 올릴 수 있음
# 상하좌우 한칸 이동 (각 말마다 미리 정해져 있음)
#
# 턴한번 :
#     1번말부터 K번말 "순서대로" 이동
#     한 말이 이동하면 "위!!에 올려져 있는" 말도 이동
#
#     A말의 "이동 하려는 칸"이
#         흰색 0:
#             A말 위 모든 말과 같이
#             그 칸의 맨 위로 이동
#         빨강 1:
#             A말과 모든 말이 같이 뒤집힌 순서로
#             그 칸의 맨 위로 이동 (!!! "이동 하려는 칸"의 말들은 그대로)
#         파랑 2 or 벽 oob:
#             A번말의 이동방향을 반대로 하고 (다른 말은 그대로)
#             반대로 바꾼 후 이동하려는 칸도 파랑이라면
#                 가만히 있음
#             아니라면
#                 한칸 이동
#
# 말이 4개 이상 쌓이는 순간 : 게임 종료
# 값이 1000보다 크거나 종료되지 않는 경우는 -1 출력
#
# [구상]
# 행열방향 전부 -1해서 받기 (우좌상하)
# 입력에서는 처음부터 같은것 두개 X
# 턴 1번부터 시작
#
# solve
#     move : 움직임의 결과도 네개 이상이 되었는지 아닌지 반환
#         움직일 때 위의 말들도 같이 움직이므로 같이 pos를 수정해야함
# """
#
#
