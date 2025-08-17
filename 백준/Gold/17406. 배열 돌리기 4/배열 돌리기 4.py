"""
K<=6 각 회전 연산을 모두 한번씩 사용한 결과에서 배열 A의 값 (행의 수 합 중 최소)의 최소 구하기
회전 + 백트래킹

r-s r+s 등이 항상 범위 내에 있도록 제공됨
"""


def rotate(R, C, S, arr):
    new_arr = [[x for x in LST] for LST in arr]
    for s in range(1, S + 1):
        cr, cc = R - s, C - s
        for i in range(4 * (2 * s)): # (D) 2**s가 아닌 2*s (그림으로 그려보고 시작하기)
            dr, dc = DS[i // (2 * s)]
            nr, nc = cr + dr, cc + dc
            new_arr[nr][nc] = arr[cr][cc]
            cr, cc = nr, nc
    return new_arr


def backtrack(depth):
    global ans
    if depth == K:
        arr = [[x for x in LST] for LST in ARR]
        for r, c, s in ORDER:
            arr = rotate(r, c, s, arr)
        mn = INF
        for lst in arr[1:]:
            mn = min(mn, sum(lst))
        ans = min(ans, mn)
        return

    for k in range(K):
        if VISITED[k] == 0:
            VISITED[k] = 1
            ORDER[depth] = COMS[k]
            backtrack(depth + 1)
            VISITED[k] = 0


N, M, K = map(int, input().split())
ARR = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
COMS = [tuple(map(int, input().split())) for _ in range(K)]
VISITED = [0] * K

DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
ORDER = [()] * K

INF = 100 * M
ans = INF

# ---------
backtrack(0)
print(ans)
# ----------
# for r, c, s in COMS:
#     arr = rotate(r, c, s, ARR)
#     ARR = arr
#     print(r,c,s)
#     for l in arr:
#         print(l)
#     print()

