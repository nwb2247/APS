"""
N*N

1. 인접 : 상하좌우

2. 블록 그룹:
    연결된 블록 집합
        (주의)
        일반 블록 1개 이상 필수
        블록의 수는 2개 이상
        (ex) 무지개 하나 X , 일반 + 무지개 O, 무지개 두개 X, 일반 하나 X)

        일반 블록 색은 모두 같아야함
        검은색은 있으면 안됨
        무지개는 얼마든지 있어도 됨
        서로 모두 인접해야함

3. 기준 블록:
    !!! 무지개 블록이 아닌 것만이 기준블록이 됨 (D)
    1. 행 가장 작은
    2. 열 가장 작은
    사전순 정렬

4. 오토플레이 :
    아래 과정이 "블록 그룹"이 존재하는 한 계속반복

    [1] 가장 큰 블록 그룹을 찾는다 (cf) 블록그룹의 크기는 2이상)
    여러개라면
        1. 무지개 블록이 가장 많은
        2. 기준 블록 행 가장 큰
        3. 기준 블록 열 가장 큰

    [2] [1]에서 찾은 가장 큰 블록 그룹의 모든 블록 제거
        블록의 수의 "제곱"을 점수로 획득

    [3] 중력 작용
        (행의 번호가 큰칸으로 이동) -> 제일 아래 방향으로 쌓임
        검은색은 이동하지 않으며, 검은색 위에 있는 것들도 검은색 위로 쌓임
    [4] "반시계" 회전
    [5] 다시 중력

출력:
    "오토 플레이"가 끝났을 때의 점수의 합

[구상]
    무지개 0 검은색 -1, 나머지 1이상의 자연수 (M)

    1. 블록그룹들을 찾는다. (개수 조건 조심)
        블록들 위치정보, 무지개 수, 기준블록
    2. 블록그룹 중 가장 큰 것을 찾는다.
        블록그룹 수 -> 무지개 수 -> 기준 블록 행 내림차순 -> 기준 블록 열 내림차순
    3. 제거 + 점수 산정

    (아래는 위 과정과 독립적으로 진행 가능..)
    4. 중력
    5. 반시계 회전
    6. 중력
"""
from collections import deque

# ---------------- 입력 -----------------

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# ---------------- 함수 -------------------

def dprint(st):
    print(st)
    for l in arr:
        print(l)

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def find_groups():
    """
    (주의)
        일반 블록 1개 이상 필수
        블록의 수는 2개 이상
        (ex) 무지개 하나 X , 일반 무지개 O, 무지개무지개 X, 일반 하나 X)

        일반 블록 색은 모두 같아야함
        검은색은 있으면 안됨
        무지개는 얼마든지 있어도 됨
        서로 모두 인접해야함
    :return: # [0]블록 그룹 수, [1]무지개 수, [2]기준블록 좌표(tuple), [3] 실제 블록들 (list)
    """
    # 일반 블록을 골라서 시작, 시작할때마다 v 초기화 (set으로 쓰자, 매번 N*N 배열 만드는거 부담)
    #   (무지개때문에,,,), 본인 색이거나 무지개일때만 append()
    # 완성되면 무지개 수 세기 (안전하게)
    # 기준 블록 좌표는 정렬하면 시간 오래걸리니까 조건 분기로 하나씩 돌자

    groups = []
    # (I) 한번 그룹에 들어간 유색 (not 무지개색) 다시 볼 필요 없으므로,, v_over_zero를 따로 만들자
    v_over_zero = [[0]*N for _ in range(N)]
    for sr in range(N):
        for sc in range(N):
            # 일반 블록만 골라서 시작
            if arr[sr][sc] <= 0: # 무지개거나 검은색, 빈칸이면 넘어감 (D) 0으로 해야하는데 왜 -2로 함???????
                continue
            if v_over_zero[sr][sc] != 0:    # 이미
                continue
            v_over_zero[sr][sc] = 1
            col = arr[sr][sc]
            v = set()
            q = deque()
            v.add((sr, sc))
            q.append((sr, sc))

            group = []
            while q:
                cr, cc = q.popleft()
                group.append((cr, cc))

                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if oob(nr, nc): # 범위밖이라면
                        continue
                    if arr[nr][nc] < 0: # 빈칸이거나 검은색이면
                        continue
                    if arr[nr][nc] != 0 and arr[nr][nc] != col: # 무지개도 아니고, 시작점과도 같지 않다면 (I) or이 아니라 and 다!!!
                        continue
                    if v_over_zero[nr][nc] != 0:
                        continue
                    if (nr, nc) in v:   # 이미 방문했다면
                        continue
                    if arr[nr][nc] != 0:    # 무지개가 아니라면 v_over_zero에도 넣어줌
                        v_over_zero[nr][nc] = 1
                    v.add((nr, nc))
                    q.append((nr, nc))

            if len(group) >= 2: # 블록 개수가 2개이상인 경우만 groups에 추가
                # 무지개색 세기
                cnt = 0
                br, bc = N+1, N+1
                for cr, cc in group:
                    if arr[cr][cc] == 0:    # 무지개라면
                        cnt += 1
                        continue            # 무지개는 기준 블록이될수 없음
                    # (D) 무지개 블록이 아닌!!! 블록만이 기준 블록이 될 수 있음
                    if br > cr:
                        br = cr
                        bc = cc # (I) bc도 갱신
                    elif br == cr and bc > cc:
                        bc = cc

                # [0]블록 그룹 수, [1]무지개 수, [2]기준블록 좌표(tuple), [3] 실제 블록들 (list)
                groups.append([len(group), cnt, (br, bc), group])

    return groups

def delete(group):
    for cr, cc in group:
        arr[cr][cc] = -2 # 주의 빈칸은 -2 다...

def gravity():
    # 주의 빈칸은 -2 다...
    for sc in range(N): # 열 먼저 순회
        # 검은색 (-1)의 위치를 잡고
        blacks = [N]      # 검은색들의 행 좌표 (그 위부터 다음검은색의 아래까지 넣어야함) N, -1도 넣어줌
        for zr in range(N-1, -1, -1):
            if arr[zr][sc] == -1:
                blacks.append(zr)
        blacks.append(-1)

        # print(sc, blacks)
        for i in range(len(blacks)-1):
            sr, er = blacks[i]-1, blacks[i+1]
            # sr <= tr < er의 좌표들을 모아둠
            # 그리고 sr부터 하나씩 쌓아줌
            # print(sr, er)
            tmp = []
            for tr in range(sr, er, -1):
                if arr[tr][sc] != -2:
                    tmp.append(arr[tr][sc])
            for j in range(len(tmp)):
                arr[sr-j][sc] = tmp[j]
            for tr in range(sr-len(tmp), er, -1):
                arr[tr][sc] = -2

    return

def rotate(): # 쉽게 zip 쓰자
    global arr
    arr_rev = [lst[::-1] for lst in arr]
    arr = [list(lst) for lst in zip(*arr_rev)]


def solve():

    score = 0

    # 블록 그룹이 존재할때까지!!!
    while True:
        # [1] 블록 그룹들 찾기
        groups_info = find_groups() # [0]블록 그룹 수, [1]무지개 수, [2]기준블록 좌표(tuple), [3] 실제 블록들 (list)
        if not groups_info:
            break

        # [2] 가장 큰 것 찾기
        groups_info.sort(key = lambda x: (-x[0], -x[1], -x[2][0], -x[2][1]))
        # (I) 주의 : 기준블록행 중 가장 큰것, 기준블록열 중 가장 큰것, 죄다 오름차순.,,
        biggest = groups_info[0]

        # [3] 제거 + 점수산정
        delete(biggest[3]) # 제거
        score += biggest[0]**2
        # dprint("제거")

        gravity()
        # dprint("중력")

        rotate()
        # dprint("돌리고")

        gravity()
        # dprint("중력2")

        # print(score)
        # print()

    return score

print(solve())
