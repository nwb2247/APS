"""
[반드시 다시 풀기]

- 배열조작
- R, C 자주 바뀌는 경우 len사용하는 것이 안전할수도
- 어렵게 생각하려고 하지말고 그냥 시키는대로 만들자..
    중간에 더 좋은 아이디어가 떠오르더라도 원래 생각했던게 확실히 구현 가능하다면 밀고 가자 (막상 새로운 아이디어가 더 복잡할 수도 있음)
    시간초과가 걱정된다면 일단 만들고 최적화 가능한 방법을 생각

[타임라인]

이해 및 구상 24분
    달팽이 규칙성 찾으려다가 포기 그냥 시키는대로 구현
    잦은 배열 복사로 시간 초과가 걱정되었음
    +
    배열의 크기가 R*C가 아니라 행마다 가변이라면 어떻게 처리해야하는지 고민

구현 및 디버깅 84분 (달팽이 만드는거 53분)
    달팽이 만드는 로직 구현하는데 매우 오래걸림
    처음에 생각했던 방법 그대로 했어야 했는데, 자꾸 다른 생각함
------
총 108분

[시간복잡도]
???

"""

"""
어항 정리
    달팽이 공중부양
    조정
    일렬 (왼쪽 아래부터 위방향으로)

    왼쪽 180도 공중 부양 -> 2번 진행 (바닥 길이 N//4가 됨)
    조정
    일렬

이렇게 몇번 해야 maxmin차이가 K이하가 되는지? (0번도 가능)
어항의 수가 바뀌지는 않는다., N은 4의 배수
달팽이? 공중 부양이 어렵다..
"""


def rotate(arr):        # 시계방향 90도회전
    return [list(lst[::-1]) for lst in zip(*arr)]


def make_snail():
    lst = list(range(N))

    rolled = [[lst[0]]]     # 굴려진 부분
    bottom = lst[1:]        # 바닥 부분

    while True:
        added = bottom[:len(rolled[0])]     # 바닥부분을 굴려진것의 열길이 만큼 자름
        if len(bottom[len(added):]) < len(rolled) + 1:  # 그게 rolled보다 짧다면 굴리면 안됨. break
            break
        rolled.append(added)            # 자른거 붙이고
        rolled = rotate(rolled)         # 한번더 굴림
        bottom = bottom[len(added):]    # 잘린거 빼고 갱신

    rolled.append(bottom)               # 굴린거에 남은 바닥 붙여줌

    return rolled


# ----------------------------

N, K = map(int, input().split())
LST = list(map(int, input().split()))
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
SNAIL = make_snail()        # 달팽이로 굴렸을 때, LST의 각 인덱스가 어디에 위치해야하는지


def oob(r, c, arr): # 입력된 arr 기준으로 oob 검사
    return not (0 <= r < len(arr) and 0 <= c < len(arr[r]))


def add_one():      # 가장 작은 것들 1씩 검사
    mn = min(LST)
    for i in range(N):
        if LST[i] == mn:
            LST[i] += 1


def roll():     # 달팽이 형태로 굴리기
    snail = [list(lst[:]) for lst in SNAIL]
    for cr in range(len(snail)):
        for cc in range(len(snail[cr])):
            snail[cr][cc] = LST[snail[cr][cc]]
    return snail


def adjust(arr):    # 인구수 조정
    narr = [[0 for _ in range(len(lst))] for lst in arr]

    for cr in range(len(arr)):
        for cc in range(len(arr[cr])):
            val = arr[cr][cc]       # 원래 값 기억
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc, arr) or arr[cr][cc] <= arr[nr][nc]:
                    continue
                d = (arr[cr][cc] - arr[nr][nc]) // 5    # arr[cr][cc]가 더 큰 경우만 확인
                if d > 0:
                    narr[nr][nc] += d
                    val -= d
            narr[cr][cc] += val

    return narr


def flatten(arr):   # 1자로 만들어주기
    cnt = 0
    for cc in range(len(arr[-1])):
        for cr in range(len(arr) - 1, -1, -1):
            if oob(cr, cc, arr):    # cc에 대해서는 배열의 세로길이 확인하기 어려우므로 oob사용
                break
            LST[cnt] = arr[cr][cc]
            cnt += 1

    return


def stand():    # 네개로 잘라서 세우기
    A, B, C, D = LST[:N // 4], LST[N // 4:(N // 4) * 2], LST[(N // 4) * 2:(N // 4) * 3], LST[(N // 4) * 3:]
    C.reverse()
    A.reverse()
    res = [C] + [B] + [A] + [D]
    return res

def solve():

    turn = 0
    if max(LST) - min(LST) <= K:
        return turn

    while True:
        turn += 1
        # [1] 1씩 추가
        add_one()
        
        # [2] 달팽이, 조정, 일자 
        snail = roll()
        snail = adjust(snail)
        flatten(snail)
        
        # [3] 세우고, 조정, 일자
        arr = stand()
        arr = adjust(arr)
        flatten(arr)
        
        # 확인
        if max(LST) - min(LST) <= K:
            return turn


print(solve())
