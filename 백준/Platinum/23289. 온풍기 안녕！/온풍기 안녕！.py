"""
[반드시 다시 풀기]

- 방향 마다 벽의 위치 회전되기때문에 규칙성 찾는게 좋았음
- 바깥쪽 온도가 1씩 감소 -> 4꼭지 두번 빼지 않게 조심해야함
- 출력 조건, 방향 순서 확실하게 보자... 방향 1부터 시작한다면 그냥 dict써서 keyerror나도록 확인하거나
- list로 쓸거면 None으로 가는게 안전
- 패딩 유리, 필요없음 확인하기
- 원본을 변형하지 않은채 퍼지고 줄어들고 하는 문제 -> 뭐랑 뭐를 비교하고 뭐는 바뀌면 안되고, += 인지 = 인지 잘 확인하자....
- 이해하는데 좀 걸리고, 입력 받는데 너무 많은 힘을 썼다...


[엣지 케이스]
7 8 1
5 0 0 0 0 0 0 5
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
5 0 0 0 3 0 0 5
3
4 4 1
5 4 0
5 6 0
--------
정답 17
오답 24 => 4꼭지 두번씩 빼주는 경우

[시간 복잡도]
1001*(R*C) (BFS는 일정 범위까지만 뻗어가므로 미미함)

[타임라인]
이해 및 구상 41분
    -) 일단 이해하는데 오래 걸렸고 (그림 확인까지)...
    ?) 입력 어떻게 받아야 나중에 안헷갈릴지 고민하는데에도 시간을 많이 투자함
구현 및 디버깅 84분
    -) 방향 순서 착각, BFS 벽이 아니라면! 인데 !=0으로 해줌 (빈칸이 아니라면)
        주석을 적어뒀으면 더 빨리 찾았을듯
    -) adjust에서 += val해야하는데 ==val로 적음
    -) 테케를 좀 더 풍부하게 생각하거나, 각 함수의 단위테스트를 좀 더 많이 진행했더라면...
    +) dprint()를 잘 구성하였음
    ?) added 안써도 된다는 거 나중에 깨달았지만, 일단 안전하게 냅둬보기로 함
---------
총 125 분

"""

"""
R*C
    [송풍] => BFS?
    벽있으면 안됨
    (손구상)
    바로 앞은 바람 방향의 방향만 확인
    양대각은 일단 내 위치에서 옆칸의 벽이 있는지 보고, 옆칸(zr, zc)에서 바람 방향에 벽이 있는지 확인
    => 없으면 가능 (물론 oob는 조사 필요)

    [조정]
    동시에
    벽이 있으면 X
    온도의 "차이" // 4

    [-1씩 감소]
    가장 바깥쪽 온도가 1씩 감소

    [초콜릿 먹음]

    [조사하려는 모든 칸의 온도가 K 이상인지 검사]

- 온풍기 하나 이상
- 조사하는 칸 하나 이상
- 입력 좌표들 -1로 받는다.
- 온풍기가 있는 칸과 바람이 나오는 방향에 있는칸 (5) 사이에는 벽이 없다. + 칸이 항상 존재한다. (oob 아님)
- 같은 벽은 두번 주지 않음,
- 벽은 유효하게 주어줌 (oob 나가지 않음)


[출력]
먹은 초콜릿의 개수 세기
초코 개수가 100 넘어가면 101 출력

[시간 복잡도]
1000*R*C (BFS는 일정 범위까지만 뻗어가므로 미미함)

[예상 엣지]
벽, 온풍기 있는 칸도 상승, 벽있으면 조절 안됨, 차이//4
"""
from collections import deque

# ------------------------- 입력, 전처리 ---------------------------

ds = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]  # 1우 2좌 3상 4하 (D) 방향 순서 꼭 지킵시다!

R, C, K = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(R)]
heaters = []  # 온풍기 (r, c, 방향)
targets = []  # K도 이상인지 조사해야하는 칸
for ZR in range(R):
    for ZC in range(C):
        if ARR[ZR][ZC] == 5:
            targets.append((ZR, ZC))
        elif 1 <= ARR[ZR][ZC] <= 4:
            heaters.append((ZR, ZC, ARR[ZR][ZC]))

W = int(input())
walls = [[[0 for _ in range(5)] for _ in range(C)] for _ in range(R)]  # 상하좌우의 벽
for _ in range(W):
    A, B, TT = map(int, input().split())
    x, y = A - 1, B - 1
    if TT == 0:  # (x, y)의 위, (x-1, y)의 아래 즉 가로모양 벽, 위아래를 막음
        walls[x][y][3] = 1
        walls[x - 1][y][4] = 1
    else:  # t==1 (x, y)의 오른쪽, (x, y+1)의 왼쪽 즉 세로모양 벽, 좌우를 막음
        walls[x][y][1] = 1
        walls[x][y + 1][2] = 1

# ---------------------- 자료 ----------------------------

# ds = [None, (0, 1), (0, -1), (-1, 0), (1, 0)] # 1우 2좌 3상 4하
m = [[0 for _ in range(C)] for _ in range(R)]  # 현재 온도
# R, C, K = map(int, input().split())   # R, C, 조사칸 K도 이상이어야함
# heaters = []                          # 온풍기 (r, c, 방향)
# targets = []                          # 조사해야하는 칸
# W = int(input())
# walls = [[[0 for _ in range(5)] for _ in range(C)] for _ in range(R)] # 우좌상하의 벽
sides = [None, [3, 4], [3, 4], [1, 2], [1, 2]]


# ----------------------- 함수화 -------------------------


def dprint():
    # [0] 온도 출력
    for l in m:
        print(*map(lambda x: str(x).rjust(4), l))   # 벽이랑 온도 위치 맞추기 위해 rjust사용
    # [1] 벽 출력
    for zr in range(R):
        for zc in range(C):
            print("".join(map(lambda x: str(x), walls[zr][zc][1:])), end=" ")
        print()
    print()


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def wind():  # 온풍기 바람 보내기
    added = [[0 for _ in range(C)] for _ in range(R)]
    for br, bc, d in heaters:
        q, v = deque(), set()  # 매번 R*C 배열 만들기 부담스러우니 v는 set으로 만들자
        # v는 이번 온풍기에 대한 visited 배열
        dr, dc = ds[d]  # 온풍기 방향
        sr, sc = br + dr, bc + dc  # 5가 칠해질 곳
        v.add((sr, sc))
        q.append((sr, sc, 5))  # 꺼내면서 올려야할 온도
        while q:
            cr, cc, a = q.popleft()
            if a == 0:  # 0인 순간 더 나아갈 필요없으니 컽
                continue
            added[cr][cc] += a

            # [1] 정면
            nr, nc = cr + dr, cc + dc
            # nrnc까지 벽이 아니고, oob 아니고 방문하지 않았다면
            if walls[cr][cc][d] == 0 and not oob(nr, nc) and (nr, nc) not in v:
                v.add((nr, nc))
                q.append((nr, nc, a - 1))

            # [2] 양 대각
            for nd in sides[d]:
                zr, zc = cr + ds[nd][0], cc + ds[nd][1]  # zrzc : 현재 위치의 side 위치
                # zrzc까지 벽이 아니고, oob 아니고 zrzc에서 nrnc까지 벽이 아니라면
                if walls[cr][cc][nd] == 0 and not oob(zr, zc) and walls[zr][zc][d] == 0:
                    nr, nc = zr + dr, zc + dc
                    # nrnc도 벽이 아니고 방문하지 않았다면
                    if not oob(nr, nc) and (nr, nc) not in v:
                        v.add((nr, nc))
                        q.append((nr, nc, a - 1))

    for cr in range(R):
        for cc in range(C):
            m[cr][cc] += added[cr][cc]

    return


def adjust():
    nm = [lst[:] for lst in m]  # 새로운 배열 만들어두고,
    for cr in range(R):
        for cc in range(C):
            for cd in range(1, 5):
                dr, dc = ds[cd]
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc) or m[nr][nc] >= m[cr][cc] or walls[cr][cc][cd] == 1:
                    continue
                nm[cr][cc] -= (m[cr][cc] - m[nr][nc]) // 4
                nm[nr][nc] += (m[cr][cc] - m[nr][nc]) // 4

    for cr in range(R):
        for cc in range(C):
            m[cr][cc] = nm[cr][cc]

    return


def subtract_edge():  # 네꼭지 두번빼지 않도록 주의
    for cc in range(C):  # 맨 위, 아래 줄
        for cr in [0, R - 1]:
            if m[cr][cc] >= 1:
                m[cr][cc] -= 1
    for cr in range(1, R - 1):  # 오른, 왼 줄
        for cc in [0, C - 1]:
            if m[cr][cc] >= 1:
                m[cr][cc] -= 1
    return


def check():
    for cr, cc in targets:
        if m[cr][cc] < K:  # k이상이어야 합격, 즉 k미만인게 하나라도 있으면 바로 False
            return False
    return True


def solve():
    # dprint()
    for choco in range(1, 102):  # (D) 1001이 아니라 101 ;;;;;;;;;;;;;;;;;;;;;;
        wind()
        adjust()
        subtract_edge()
        # 초코 : choco
        if check():
            break

    # 1001에서도 실패하면 1001반환
    return choco


res = solve()
print(res)
