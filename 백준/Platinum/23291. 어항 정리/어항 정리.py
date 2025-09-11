"""
어항 정리
    달팽이 공주부양

    조정

    일렬 (왼쪽 아래부터 위방향으로)

    왼쪽 180도 공중 부양 -> 2번 진행 (바닥 길이 N//4가 됨)

    조정

    일렬

이렇게 몇번 해야 maxmin차이가 K이하가 되는지? (0번도 가능)

어항의 수가 바뀌지는 않는다., N은 4의 배수

달팽이? 공중 부양이 어렵다..

"""


def rotate(arr):
    return [list(lst[::-1]) for lst in zip(*arr)]


def roll():
    lst = list(range(N))

    rolled = [[lst[0]]]
    bottom = lst[1:]

    while True:
        added = bottom[:len(rolled[0])]
        if len(bottom[len(added):]) < len(rolled) + 1:
            break
        rolled.append(added)
        rolled = rotate(rolled)
        bottom = bottom[len(added):]

    rolled.append(bottom)

    return rolled


# ----------------------------

N, K = map(int, input().split())
LST = list(map(int, input().split()))
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
SNAIL = roll()


def oob(r, c, arr):
    return not (0 <= r < len(arr) and 0 <= c < len(arr[r]))


def add_one():
    mn = min(LST)
    for i in range(N):
        if LST[i] == mn:
            LST[i] += 1


def do_snail():
    snail = [list(lst[:]) for lst in SNAIL]
    for cr in range(len(snail)):
        for cc in range(len(snail[cr])):
            snail[cr][cc] = LST[snail[cr][cc]]
    return snail


def adjust(arr):
    narr = [[0 for _ in range(len(lst))] for lst in arr]
    # for l in narr:
    #     print(l)

    for cr in range(len(arr)):
        for cc in range(len(arr[cr])):
            val = arr[cr][cc]
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc, arr) or arr[cr][cc] <= arr[nr][nc]:
                    continue
                d = (arr[cr][cc] - arr[nr][nc]) // 5
                if d > 0:
                    narr[nr][nc] += d
                    val -= d
            narr[cr][cc] += val

    # for l in narr:
    #     print(l)

    return narr


def flatten(arr):
    cnt = 0
    for cc in range(len(arr[-1])):
        for cr in range(len(arr) - 1, -1, -1):
            if oob(cr, cc, arr):
                continue
            LST[cnt] = arr[cr][cc]
            cnt += 1

    return


def stand():
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
        add_one()

        snail = do_snail()
        snail = adjust(snail)
        flatten(snail)

        arr = stand()
        arr = adjust(arr)
        flatten(arr)

        if max(LST) - min(LST) <= K:
            return turn


print(solve())
