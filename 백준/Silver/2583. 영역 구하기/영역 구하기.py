import sys

sys.setrecursionlimit(10000)

M = -1  # height
N = -1  # width

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 방향 리스트


def dfs(pos, arr, visited):
    cr, cc = pos
    visited[cr][cc] = True
    
    # 연결된 요소의 개수
    cnt = 1

    for dr, dc in ds:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < M and 0 <= nc < N:
            # 새로운 좌표가 0이고 방문하지 않았다면 재귀 호출하고 cnt에 값 추가
            if arr[nr][nc] == 0 and not visited[nr][nc]:
                cnt += dfs((nr, nc), arr, visited)

    return cnt


def solve():
    global M, N
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    # 주의 : M이 height N이 width
    for _ in range(K):  # 영역 칠하기
        sc, sr, ec, er = map(int, input().split())
        # 주의 : arr[er][ec]는 칠해지지 않음, 즉 range(sr, er+1)이 아닌 range(sr, er)까지 돌아야 함
        for r in range(sr, er):
            for c in range(sc, ec):
                arr[r][c] = 1
    visited = [[False] * N for _ in range(M)]
    
    # 연결 요소의 갯수 추가
    cons = []
    for sr in range(M):
        for sc in range(N):
            if arr[sr][sc] == 0 and not visited[sr][sc]:
                cons.append(dfs((sr, sc), arr, visited))
    cons.sort()
    print(len(cons))
    print(*cons)

solve()
