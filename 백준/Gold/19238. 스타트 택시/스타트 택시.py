"""
[이해]
빈칸 or 벽
특정 위치로 이동시 최단 경로로만 이동
승객을 태어 목적지로 이동
승객 고를때
최단거리 -> 행, 열
승객 태우러 감 (이거리 기준으로 선정)
태워서 목적지로 이동 (이거리의 두배로 충전이 됨)
두 경우 모두 한칸 마다 연료가 소모됨

출력 : 모든 손님을 이동시키고 남은 연료량
[1] 연료가 바닥나거나
[2] 모든 손님을 이동시킬 수 없을때
는 -1 출력

20 400
N*N, M명

(다 -1해서 받아야함)
운전 시작 칸
승객 출발지, 목적지

[구상]
매번 한명씩 태우고 정렬

(400log400 + 400*5(BFS) )*400 => 가능

도착지 dest : 2차원 배열로 생성

승객 -> arr에 기록 (돌 수 있는 만큼 다돎) ## (+ 나중에 남은 승객수 다 돌았으면 가치지기)
info 에 append하고 정렬 기준에 따라 정렬
info[0] 이 남은 연료량보다 크면 -1

arr에 승객 위치를 0으로 만들고 (태웠으므로)
dest에서 도착지 가져와서 거리를 BFS로 다시 계산
남은 연료량보다 멀면 -1

다돌고 남은거 출력

중간에 -1 줘야하므로 solve 사용

"""
from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def find(tr, tc):
    """
    :param tr:
    :param tc:
    :return:
        dist, nr, nc 반환
        태울 승객이 없다면 0, -1, -1 반환하게 해야함
    """

    v = [[-1] * N for _ in range(N)]
    q = deque()

    v[tr][tc] = 0
    q.append((tr, tc))

    info = []  # 출발지

    # 벽이 아닌 경우에만 append()
    while q:
        cr, cc = q.popleft()
        if arr[cr][cc] == 2:
            info.append((v[cr][cc], cr, cc))

        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] == 1:
                continue
            if v[nr][nc] != -1:
                continue
            v[nr][nc] = v[cr][cc] + 1
            q.append((nr, nc))

    if len(info) == 0:  # 태울 승객 없다면
        return 0, -1, -1

    info.sort(key=lambda x: (x[0], x[1], x[2]))
    # print(info)
    return info[0]


def to_dest(tr, tc):
    """
    :param tr: 택시 위치이자, 승객 위치
    :param tc:
    :return: dest[tr][tc]까지의 거리

    """
    er, ec = dest[tr][tc]

    v = [[-1] * N for _ in range(N)]
    q = deque()

    v[tr][tc] = 0
    q.append((tr, tc))
    while q:
        cr, cc = q.popleft()

        if (cr, cc) == (er, ec):
            return v[er][ec], er, ec  # dist, r, c 반환

        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] == 1:
                continue
            if v[nr][nc] != -1:
                continue
            v[nr][nc] = v[cr][cc] + 1
            q.append((nr, nc))

    # er, ec를 못찾았으면 0, -1, -1 반환
    return 0, -1, -1


def solve():
    cnt = 0  # 목적지 까지 성공적으로 도착한 승객 수 (연료가 바닥나든, 이동이 불가하든, M 못채우면 실패)
    fuel = K  # 남은 연료량
    tr, tc = TR, TC

    while True:
        # [1] 태울 승객 위치 찾기
        dist0, nr, nc, = find(tr, tc)
        # print(nr, nc)
        if (nr, nc) == (-1, -1):  # 더 이상 태울 승객이 없다면
            break
        if fuel < dist0:
            break
        fuel -= dist0  # 거리만큼 연료깎고
        tr, tc = nr, nc
        # (I) 승객 태웠으므로 0으로 만들어줘야함
        arr[tr][tc] = 0

        # [2] 목적지까지 데려다 주기 (목적지는 반드시 있음)
        dist1, nr, nc = to_dest(tr, tc)  # 현재 택시 위치 == 손님 위치
        if (nr, nc) == (-1, -1):  # (I) 도달할 수 없다면
            break
        if fuel < dist1:
            break
        fuel -= dist1
        tr, tc = nr, nc

        # [3] 성공적으로 목적지까지 도달해야 cnt올라감
        cnt += 1
        fuel += dist1 * 2  # 승객의 출발지 -> 목적지의 거리 dist*2를 해줌

        # print(fuel)
        # for l in arr:
        #     print(l)
        # print()

    # while 문 끝났다면 cnt가 손님수 M 가 일치하면 fuel 반환 그렇지 않으면 -1 반환
    if cnt == M:
        return fuel
    else:
        return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
TR, TC = map(lambda x: int(x) - 1, input().split())  # 택시 좌표 (1씩빼서 받기)
dest = [[(-1, -1) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    SR, SC, ER, EC = map(int, input().split())
    arr[SR - 1][SC - 1] = 2  # 맵에 바로 표시 : 모든 승객의 출발지가 다르므로!!!! 가능한 방법 (아니라면 불가능)
    dest[SR - 1][SC - 1] = (ER - 1, EC - 1)

print(solve())