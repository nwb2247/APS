"""

초기 : 비활성상태
생명력 수치가 X인 줄기 세포는 X시간동안 비활성 X시간이 지나는 순간 활성상태가 됨

X시간 비활성 -> X시간 활성 살아있음 -> 죽음

죽더라도 소멸하지 않고 죽은 상태도 그리드에 남아있음

이미 줄기 세포가 존재하는 경우 해당 위치에는 번식 X

두개 이상이 하나의 그리드 셀에 동시에! 번식 하려고 하는 경우 생명력 수치가 높은 것이 거기에 번식

    동시에 -> q, nq?
배양용기 매우 큰 것으로 가정

K 300 이하
용기의 크기는 무한 (set사용?)

출력 : 살아있는 세포 + 죽어있는 세포

공간복잡도 대충 650*650? ㄱㄱ
"""
from collections import deque

def init():
    for cr in range(R):
        for cc in range(C):
            if ARR[cr][cc] != 0:
                unact.append((cr, cc, ARR[cr][cc], ARR[cr][cc])) # 활성화까지 남은 시간, X
                v.add((cr, cc))

def activate():
    global unact

    tmp = deque()
    while unact:
        cr, cc, cur, X = unact.popleft()
        if cur-1 == 0:
            act.append((cr, cc, X, X)) # reproduce꺼내마자 1빼므로 +1을 해줘야 맨처음에 X로 시작함
        else:
            tmp.append((cr, cc, cur-1, X))

    unact = tmp
    return

def reproduce():    # 죽은 거 먼저 처리해야함...
    global act

    tmp = deque()
    ndict = dict()
    while act:
        cr, cc, cur, X = act.popleft()

        # 살아있는것만 가지고
        if cur == X-1: # 첫 한시간에만 상하좌우로 번식 (맨처음은 X+1로 시작) (그림상, 활성화 되더라도 바로 번식이 아닌 다음턴)
            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if (nr, nc) in v:
                    continue

                if (nr, nc) not in ndict:
                    ndict[(nr, nc)] = X
                elif ndict[(nr, nc)] < X: # 0의 경우가 있으므로
                    ndict[(nr, nc)] = X

        if cur == 0:    # 이번턴에 죽더라도 번식하고 죽음, 0이 되더라도 번식하고 죽어야함 (1인 경우)
            continue

        tmp.append((cr, cc, cur-1, X))

    # v에 넣는 것은 최종적으로 ndict에 확정된 것만...
    for pos, X in ndict.items():
        nr, nc = pos
        unact.append((nr, nc, X, X))
        v.add((nr, nc))

    act = tmp
    return


def solve():

    # init이 초기 상태, 첫번째 돌면 1시간후
    for t in range(K):
        activate()
        reproduce()
        # print("unact :", unact)
        # print("act :", act)
        # print(f"unact:{len(unact)}, act:{len(act)}")
        # print()

    return


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
TC = int(input())
for tc in range(1, TC+1):
    R, C, K = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(R)]
    unact = deque()
    act = deque()
    v = set()
    init()
    solve()
    print(f"#{tc} {(len(unact) + len(act))}")