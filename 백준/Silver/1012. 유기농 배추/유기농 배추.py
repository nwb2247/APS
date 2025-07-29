import sys
sys.setrecursionlimit(10000)

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 방향 리스트
M = -1  # M, N : dfs() 내에서도 사용하므로 전역 범위에서 쓰고 매 tc마다 입력받아 할당
N = -1


def dfs(pos, visited, arr):
    cr, cc, = pos  # 현재 위치
    visited[cr][cc] = True  # 방문 처리
    for dr, dc in ds:  # 네 방향에 대해서
        nr, nc = cr + dr, cc + dc
        # 새로운 좌표가 정상 범위 내에 있고 방문하지 않았고 1값을 갖는다면 재귀호출
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 1:
            dfs((nr, nc), visited, arr)


def solve(tc):
    global M, N  # M, N : dfs() 내에서도 사용하므로 전역 범위에서 쓰고 매 tc마다 입력받아 할당
    M, N, K = map(int, input().split())
    # 입력 받음
    arr = [[0] * M for r in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    # 방문 여부 관리
    visited = [[False] * M for r in range(N)]
    ans = 0  # 연결된 정점 덩어리 갯수
    for sr in range(N):
        for sc in range(M):
            if arr[sr][sc] != 1 or visited[sr][sc]:  # 1이 아니거나, 앞에서 이미 방문한 정점이면 넘어감
                continue
            dfs((sr, sc), visited, arr)
            ans += 1
    print(ans)


def main():
    TC = int(input())
    for tc in range(1, TC + 1):
        solve(tc)


main()
