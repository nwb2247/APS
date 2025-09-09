"""
N*N
1~M 자연수 상어번호

1이 가장 셈 (숫자 작을 수록)

모든 상어 동시에 이동, 이동칸에 자기 냄새 뿌림, k번 이동시 사라짐
    => 처음 기록할때, 몇초까지 유효한 냄새인지 쓰자)

1. 인접한 칸 중 아무냄새 없는 칸
2. 자신의 냄새가 있는칸 (not 다른 상어의 냄새)
    -> 냄새도 이동하면서 표시하면 안되고, 상어 다 이동시키고 가장 작은 상어로 해야할듯
    -> 자기 냄새로 돌아가면 다시 k초로 갱신됨 즉 다시 뿌림 (그림 4)
3. 상어마다 보고 있는 방향에 따른 우선 순위가 다름

"""

SEC = 1000
ds = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}  # 1상 2하 3좌 4우
N, M, K = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
LST = [None] + list(map(int, input().split()))

smell = [[(0, 0) for _ in range(N)] for _ in range(N)]  # idx, sec : sec초 "미만"에서만 유효/ "이상"에서는 무효, (0, 0)은 냄새가 없는 상태
m = [[set() for _ in range(N)] for _ in range(N)]
pos = dict()  # 위치
rule = dict()  # 이동방법

for ZR in range(N):
    for ZC in range(N):
        IDX = ARR[ZR][ZC]
        if IDX == 0:
            continue
        pos[IDX] = (ZR, ZC, LST[IDX])
        m[ZR][ZC].add(IDX)

for IDX in range(1, M + 1):
    TMP = dict()
    for CD in range(1, 4 + 1):
        TMP[CD] = list(map(int, input().split()))
    rule[IDX] = TMP

# -------------- 함수화 --------------

def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def spread(turn):
    """
    현재 상어 위치를 기준으로 냄새를 뿌림
    """
    for idx in pos:
        cr, cc, cd = pos[idx]
        smell[cr][cc] = (idx, turn + K)  # turn + K 미만까지 유효, (K번 이동하면 사라짐)

    for cr in range(N):
        for cc in range(N):
            if smell[cr][cc][1] - turn <= 0:
                smell[cr][cc] = (0, 0)

    return



def move():  # 이동 못하는 경우도 있나?
    for idx in pos:
        cr, cc, cd = pos[idx]

        found = False
        for td in rule[idx][cd]:  # 일단 빈냄새부터 찾기
            dr, dc = ds[td]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or smell[nr][nc] != (0, 0):  # 밖이거나 빈냄새 아니라면
                continue
            # 밖도 아니고, 빈냄새 맞다면
            m[cr][cc].remove(idx)
            m[nr][nc].add(idx)
            pos[idx] = (nr, nc, td)
            found = True
            break  # 종료
        if found:
            continue  # 빈 냄새 찾았다면 다음 상어 idx로 넘어감

        # 못찾았다면 자기 냄새 탐색
        for td in rule[idx][cd]:
            dr, dc = ds[td]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or smell[nr][nc][0] != idx:  # 밖이거나 자기 냄새 아니라면
                continue
            # 밖도 아니고 자기 냄새 맞다면
            m[cr][cc].remove(idx)
            m[nr][nc].add(idx)
            pos[idx] = (nr, nc, td)
            found = True
            break  # 다음 상어 idx로 넘어감
        if not found:
            continue  # 못찾았다면 아무것도 안하고 다음 상어dix로 넘어감
    return


def kill():
    for cr in range(N):
        for cc in range(N):
            if len(m[cr][cc]) <= 1:  # 한마리 이하라면 넘어감
                continue
            survived = min(m[cr][cc])
            killed = list(m[cr][cc].difference({survived}))
            for idx in killed:
                m[cr][cc].remove(idx)
                pos.pop(idx)
                rule.pop(idx)
    return


def check():  # 1번 상어만 남았는지 확인
    if len(pos) == 1:
        return True
    else:
        return False


def solve():
    for turn in range(SEC + 1):  # 1000초까지 확인
        if check():
            return turn
        spread(turn)  # 시작하자마자 냄새 뿌리기
        move()
        kill()
        # print(turn)
        # print(pos)
        # for l in smell:
        #     print(l)
        # for l in m:
        #     print(l)

    # 1001초 (1000초 행동이 끝났으면)
    return -1


res = solve()
print(res)
