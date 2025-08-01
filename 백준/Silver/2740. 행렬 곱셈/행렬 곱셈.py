N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = [[0]*K for _ in range(N)]
for r in range(N):
    for c in range(K):
        for m in range(M):
            ans[r][c] += A[r][m]*B[m][c]
for lst in ans:
    print(*lst)