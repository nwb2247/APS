"""

"""
def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def init_tops():
    global tops
    mx = -1
    for cr in range(N):
        for cc in range(N):
            if mmap[cr][cc] == mx:
                tops.append((cr, cc))
            elif mmap[cr][cc] > mx:
                tops = [(cr, cc)]
                mx = mmap[cr][cc]

def backtrack(pr, pc, v, cnt): # 마지막 위치, 지금까지 뭐넣었는지, 지금까지의 길이
    global ans
    ans = max(ans, cnt)
    # print(v)

    # 종료조건, 4방에 더 갈 곳이 없다면...
    for cd in range(4):
        dr, dc = ds[cd]
        nr, nc = pr+dr, pc+dc
        if oob(nr, nc) or mmap[nr][nc] >= mmap[pr][pc] or (nr, nc) in v:
            continue
        # 갈수 있다면
        v[nr][nc] = 1
        backtrack(nr, nc, v, cnt+1)
        v[nr][nc] = 0 # 원상 복구

    return

def check(v):

    for sr, sc in tops:
        v[sr][sc] = 1
        backtrack(sr, sc, v, 1) # 마지막 위치, 지금까지 뭐 넣었는지, 지금까지 넣은 것의 개수
        v[sr][sc] = 0


    return


def solve():

    v = [[0 for _ in range(N)] for _ in range(N)]

    # 아무것도 안깎는거 한번 수행
    check(v) # (D) 주석처리하고 까먹고 안해제함

    for cr in range(N):
        for cc in range(N):
            origin = mmap[cr][cc]
            # for new in range(max(0, origin - K), origin):  # 최대로 많이 깎는거부터, 최소(1)로 깎는거
            for new in range(max(0, origin - K), origin):  # 최대로 많이 깎는거부터, 최소(1)로 깎는거
                mmap[cr][cc] = new
                check(v)

                # for l in mmap:
                #     print(l)
                # print()
                # print(ans)

            mmap[cr][cc] = origin  # 원복
    return

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(N)]
    tops = []
    init_tops() # 가장 높은 봉우리를 깎더라도, 그 점에서 시작할 수 있다... (문제 설명이 모호함)

    ans = 0
    solve()
    print(f"#{tc} {ans}")
