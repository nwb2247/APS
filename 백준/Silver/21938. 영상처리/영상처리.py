N = None
M = None

# 메모리 초과, 재귀 깊이 초과로 인해 stk을 이용한 dfs로 풀었음

def dfs(pos, arr, visited):  # stk과 loop를 이용한 dfs
    cr, cc = pos
    stk = []        # 더 이상 방문하지 않은 정점이 없을 때 돌아갈 직전 분기
    while True:
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:       # 인접한 칸에 대해
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and not visited[nr][nc]:    # 1이고 방문한 적 없다면
                    stk.append((cr, cc))                        # 원래 것을 스택에 넣고
                    visited[nr][nc] = True                      # nr, nc를 방문처리하고 cr, cc에 대입
                    cr, cc = nr, nc
                    break
        else:                                                   # 모든 인접 정점을 방문한 상태라면
            if len(stk) == 0:                                   # 스택이 비어 있다면 dfs 완료된 것이므로 while문 탈출
                break
            else:
                cr, cc = stk.pop()                              # 스택에 남아있는 것이 있다면 tos를 cr, cc로

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
                dfs((sr, sc), arr, visited)       # dfs를 이용해 같은 객체인지 확인
                cnt += 1

    print(cnt)


solve()
