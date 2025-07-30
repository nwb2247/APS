ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def solve():
    visited = [[False] * N for _ in range(N)]
    ans = []
    for sr in range(N):
        for sc in range(N):
            if arr[sr][sc] == 1 and not visited[sr][sc]:    # 단지 시작점이 될 수 있는지 확인
                q = [(sr, sc)]                              # 시작점 큐에 넣고 방문 처리
                visited[sr][sc] = True
                cnt = 0
                while q:
                    cr, cc = q.pop(0)
                    cnt += 1
                    for dr, dc in ds:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr <N and 0 <= nc < N:      # 범위확인하고 단지 여부, 미방문 확인 후 방문처리하고 큐에 넣음
                        # 주의 : 범위확인 까먹지 말기 (심지어 빠져도 index error 안생길수도 있음)
                            if arr[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                ans.append(cnt)
    ans.sort()
    print(len(ans))
    print(*ans, sep="\n")


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
solve()
