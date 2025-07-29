N = None
M = None


def dfs(pos, arr, visited):  # stk과 loop를 이용한 dfs
    cr, cc = pos
    stk = []
    while True:
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and not visited[nr][nc]:
                    stk.append((cr, cc))
                    visited[nr][nc] = True
                    cr, cc = nr, nc
                    break
        else:
            if len(stk) == 0:
                break
            else:
                cr, cc = stk.pop()

def solve():
    global N, M
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for i in range(N):  # 3개의 rgb값을 더함
        lst = list(map(int, input().split()))
        for j in range(M):
            arr[i][j] = lst[3 * j] + lst[3 * j + 1] + lst[3 * j + 2]

    T = int(input())  # rgb 값
    for r in range(N):
        for c in range(M):
            if arr[r][c] >= 3 * T:  # 3*T보다 크거나 같다면 1로 바꾸고
                arr[r][c] = 1
            else:  # 작다면 0으로 바꿈
                arr[r][c] = 0

    visited = [[False] * M for _ in range(N)]

    cnt = 0
    for sr in range(N):
        for sc in range(M):
            if arr[sr][sc] == 1 and not visited[sr][sc]:
                dfs((sr, sc), arr, visited)
                cnt += 1

    print(cnt)


solve()
