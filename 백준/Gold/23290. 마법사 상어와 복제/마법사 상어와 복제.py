"""
[반드시 다시 풀기]

- 고려해야할 엣지 상황 많았음
    (1) 3번 이동할때 왔던 곳을 다시 선택하는 경우 (물고기는 한번만 추가)
    (2) 상어는 한마리도 못먹을 수 있음 (이때는 oob가 아닌, 최우선 루트)
- 구상하면서 실수할만한 사항들, 주의할 사항들 까먹지 말고 꼭 적어두자..
- list(range(cd, 0, -1)) + list(range(8, cd, -1))
            쓰지 말고
        nd = (cd-1-dd)%8 + 1
- 상어랑 물고기가 같이 있을수 있다?
    물고기는 상어가 있는곳에 이동은 못하지만, 복제시엔 그대로 생김, 상어는 물고기 자리 이동가능 (+격자에서 소멸)

[타임라인]
이해 및 구상 25분
    문제 이해하는데 급급해서 주의할 사항 놓침
        (왔던 곳 다시 오더라도 먹을 물고기수는 두번 더하면 안됨)
        (상어는 한마리도 못먹더라도 이동 가능) => mx -1로 둬야함
    문제에서는 시계 방향으로 방향을 줬지만, 실제로는 반시계 방향으로 물고기 회전

구현 49분
    cd, nd 실수, 등..

디버깅 31분
    테케 다 맞더라도, 문제 다시 읽으면서 엣지 더 생각해야함
    인덴트, 변수 등 더 확인해야하지
-----------------
총 105분
"""

"""
물고기 별도의 인덱스 관리는 필요없음...

복제
    복제는 새 배열에 넣고 기다리자

모든 물고기 한칸 이동
    상어, 물고기, 냄새 -> 이동불가
    이동 칸 있을때까지 반시계 45도 (8방향)
    없으면 이동 X

    동시에 처리 (죽을때만 냄새남김)
    각 위치에 list로 표시하자
    단 움직였던애 다시 움직이지 않게 nm에 추가

상어이동
    상하좌우 인접 칸으로 이동 (상어는 4방향)
    연속해서 3칸 이동할때 oob면 불가능한방법
    이동 중에 물고기 있는 칸으로 이동하면
        물고기는 격지에서 제외, 냄새를 남김
        가능한 이동방법 중에 제외물고기가 가장 많은 방법으로 이동
    =>
    ways, 3칸에 대해서 oob 조사
    물고기 죽이고 현재 턴을 입력하자

두번전 사이클에서의 물고기 냄새가 사라짐
    (별도 함수처리 없이 차이 2인지 확인하기) X
    그냥 안전하게 4*4보면서 지금턴이랑 2차이 나는거 지워주자

복제 완료, 모든 물고기 그 자리에서 방향 그대로 가짐

상어의 이동방법 사전순
상1 좌2 하3 우4로 변환 수를 이어붙여서 정수로 변환

물고기 위치는 패딩 없이 가고, 입력시 -1로 받자...


상어랑 물고기랑 어떻게 같이 있을 수 있는지?

"""
from itertools import product

ways = []
for I in product(range(1, 5), repeat = 3):
    ways.append(I)

ds_shark = [None, (-1, 0), (0, -1), (1, 0), (0, 1)] # 상1 좌2 하3 우4
ds_fish = [None, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # 물고기 방향 (시계방향, 실제 이동은 반시계방향)

smell = [[0 for _ in range(4)] for _ in range(4)]
m = [[[] for _ in range(4)] for _ in range(4)]  # 각 위치별 물고기들
M, S = map(int, input().split())
for _ in range(M):
    FX, FY, D = map(int, input().split())
    m[FX-1][FY-1].append(D)
sr, sc = map(lambda x:int(x)-1, input().split())

# ----------------- 함수 ----------------

def dprint():
    print("srsc", sr, sc)
    for l in m:
        print(l)
    for s in smell:
        print(s)

def oob(r, c):
    return not (0<=r<4 and 0<=c<4)

def fish_move():
    global m
    nm = [[[] for _ in range(4)] for _ in range(4)]
    for cr in range(4):
        for cc in range(4):
            for cd in m[cr][cc]:
                for dd in range(8):      # (D) 반시계 회전, 주어진 입력은 시계 회전;;;;
                    nd = (cd-1-dd)%8 + 1
                    dr, dc = ds_fish[nd]
                    nr, nc = cr + dr, cc + dc
                    if oob(nr, nc) or (nr, nc) == (sr, sc) or smell[nr][nc] != 0:   # 격자 벗어나거나, 상어와 같은 위치이거나, 냄새가 존재한다면 continue
                        continue
                    nm[nr][nc].append(nd)       # (D) cd가 아니라 nd
                    break
                else:                       # (D) else 사용
                    nm[cr][cc].append(cd)   # nr, nc, nd는 for문 내에서 할당 되믜로 cr, cc, cd로 가야함
    m = nm
    return

def shark_move(turn):
    global sr, sc

    mx = -1     # (D) 한마디로 안먹는 경우라도, 이동은 발생함
    path = []
    # 어차피 ways는 사전순으로 정렬되어 있음, mx가 갱신되는 경우에만 path를 갱신하면 됨 (커지는 경우만, 같은 경우는 X)
    for w in ways:
        nr0, nc0 = sr + ds_shark[w[0]][0], sc + ds_shark[w[0]][1]       # 첫번쨰 이동좌표
        nr1, nc1 = nr0 + ds_shark[w[1]][0], nc0 + ds_shark[w[1]][1]     # 두번째 이동좌표
        nr2, nc2 = nr1 + ds_shark[w[2]][0], nc1 + ds_shark[w[2]][1]     # 세번째 이동좌표
        if oob(nr0, nc0) or oob(nr1, nc1) or oob(nr2, nc2):         # 셋중 하나라도 oob면 이동 불가
            continue

        cnt = 0       # 각 칸의 물고기 갯수
        sset = {(nr0, nc0), (nr1, nc1), (nr2, nc2)}         # 중복 제거 # (D) 같은 곳은 두번 세면 안됨..
        for zr, zc in sset:
            cnt += len(m[zr][zc])
        if cnt > mx:                # 큰 경우만 갱신하면 자동으로 사전순으로 가장 빠른 것이 path에 들억마
            mx = cnt
            path = [(nr0, nc0), (nr1, nc1), (nr2, nc2)]

    for cr, cc in path:
        if len(m[cr][cc]) >= 1:     # (I) 물고기가 들어있는 경우만 냄새 넣어주고 []
            smell[cr][cc] = turn
            m[cr][cc] = []


    sr, sc = path[-1][0], path[-1][1]    # (D) path는 항상 생김

    return

def remove_smell(turn):
    for cr in range(4):
        for cc in range(4):
            if smell[cr][cc] <= turn - 2:       # 지금 턴수와 2개 차이나는 경우는 0으로 만들어줌
                smell[cr][cc] = 0
    return


def solve():

    for turn in range(1, S+1):  # 냄새 빈칸을 0으로 했으므로...
        # [1] 복제 (딥카피 주의)
        reproduced = [[m[cr][cc][:] for cc in range(4)] for cr in range(4)]
        # [2] 물고기 이동
        fish_move()
        # [3] 상어 이동
        shark_move(turn)        # (D) 1에서 turn 으로 안바꾸고 돌림
        # [4] 냄새 제거 (2턴지난)
        remove_smell(turn)
        # [5] [1]에서 복사했던 것들 extend (이어 붙이기)
        for cc in range(4):
            for cr in range(4):
                m[cr][cc].extend(reproduced[cr][cc])
        #
        # print(turn)
        # dprint()

    res = 0
    for cr in range(4):
        for cc in range(4):
            res += len(m[cr][cc])

    return res

ans = solve()
print(ans)