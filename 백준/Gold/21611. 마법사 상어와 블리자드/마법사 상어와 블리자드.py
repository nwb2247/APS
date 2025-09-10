"""
N*N N홀수
1, 1부터 시작 ~ N, N
상어 (N+1)/2에서 시작
1상 2하 3좌 4우

    [마법]
    얼음 파괴되면 상어쪽으로 밀려 들어옴

    [폭발]
    구슬 폭발 연속 4칸... -> 폭발이 없을때까지 계속 진행 (폭발 -> 당김)

    [변화]
    하나의 그룹(3이하,4이상은 폭발에서 터짐) 은 A, B 구슬로 바뀜 (A: 4구슬의 개수, B 구슬의 번호)
    => 주의 1개짜리도 그룹이다!!!!!
    => 구슬의 개수가 초과하는 경우 나머지는 사라짐

    [점수계산]
    1*(1번개수) + 2*(2번개수) + 3*(3번개수) (D) 남아있는게 아니라 폭발된 것을 세는거임;;
    상어가 있는 칸은 0으로 주어짐

[구상]
숫자는 1차원으로 관리
블라지드 쏘는거는 2차원에서 쏘고 해당하는 칸의 1차원에서 인덱스를 비움
마법 (중력로직 비슷하게)

[시간복잡도]
100 (M) * 500 (N*N) => 가능

"""
from collections import deque

ds = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}  # 1상 2하 3좌 4우

N, K = map(int, input().split())  # N*N, K:마법의 수
ARR = [list(map(int, input().split())) for _ in range(N)]
ops = [tuple(map(int, input().split())) for _ in range(K)]

types = {1, 2, 3}


# ------- 함수 -------

def dprint():
    tmp = [[0] * N for _ in range(N)]
    for cr in range(N):
        for cc in range(N):
            tmp[cr][cc] = info[box[cr][cc]]
    for l in tmp:
        print(*l)
    print("info", info)
    print()


def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def make_box():
    # 문제는 1~N이라 되어 있는데 0~N-1로 생각하면 N//2를 시작으로 두면 됨
    m = [[0] * N for _ in range(N)]
    cr, cc = N // 2, N // 2  # (상어자리)
    order = [3, 2, 4, 1]  # 좌하우상
    l = 1
    co = 0
    cur = 0
    while not oob(cr, cc):
        for _ in range(l):
            m[cr][cc] = cur
            cur += 1
            dr, dc = ds[order[co]]
            cr, cc = cr + dr, cc + dc
        co = (co + 1) % 4
        if co % 2 == 0:
            l += 1

    return m


def magic(d, s):  # s는 범위밖으로 벗어나지 않음
    sr, sc = N // 2, N // 2
    dr, dc = ds[d]
    for i in range(1, s + 1):  # 상어는 포함 아님, s는 포함
        idx = box[sr + dr * i][sc + dc * i]
        info[idx] = 0


def pull():
    tmp = deque()
    for idx in range(1, N * N):  # 맨 좌측 상단은 N*N-1임...
        if info[idx] != 0:
            tmp.append(info[idx])
    for idx in range(1, N * N):
        if tmp:
            info[idx] = tmp.popleft()
        else:
            info[idx] = 0


def explode():
    global ans

    cnt = 0
    found = False
    for idx in range(1, N * N):  # 1번은 항상다름(0번이 상어이므로)
        if info[idx] != info[idx - 1]:  # 다른거 나왔다면,
            # [1] 이전에 쌓였던게 4이상인지 확인하고 맞다면 지워줌
            if cnt >= 4:
                found = True    # 이번에 폭발한게 있음을 확인
                ans += cnt * info[idx - 1] # 점수 추가
                for j in range(cnt):
                    info[idx - 1 - j] = 0
            # [2] cnt = 1로 초기화
            cnt = 1
        else:
            cnt += 1
    return found


def change():
    tmp = deque()
    cnt = 1  # (1번은 이미 세었다고 가정)
    for idx in range(2, N * N):  # 상어는 넣으면 안되므로 2부터 하자...
        if info[idx] != info[idx - 1]:
            tmp.append(cnt)     # 개수를 먼저 넣어주고
            tmp.append(info[idx - 1])   # 그 다음 종류를 넣어주기
            cnt = 1
        else:
            cnt += 1
    for idx in range(1, N * N):  # tmp가 더 긴 경우에도 N*N-1까지만 들어간다...
        if tmp:
            info[idx] = tmp.popleft()
        else:
            info[idx] = 0


def solve():
    # dprint()

    for i in range(K):
        d, s = ops[i]
        # [1] 블리자드 매직 + 당기기
        magic(d, s)
        # dprint()
        pull()
        # dprint()

        # [2] 폭발
        while True:  # 폭발 당김 반복
            if not explode():
                break
            pull()
        # dprint()

        # [3] A, B로 변화
        change()
        # dprint()

    return


info = [0] * (N * N)  # info도 글로벌
box = make_box()
for ZR in range(N):
    for ZC in range(N):
        info[box[ZR][ZC]] = ARR[ZR][ZC]

ans = 0  # 폭발한거만 세자 (not 마법에 의한 파괴

solve()
print(ans)
