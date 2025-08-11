"""
N, M <= 1000
(r+1, c), (r, c+1), (r+1, c+1) 방향으로만 이동가능, N-1, N-1으로 이동할때 최대 사탕 개수

즉
DP[r][c]는 max(DP[r-1][c], DP[r][c-1], DP[r-1][c-1])+arr[r][c]
왼쪽에서 오른쪽, 위에서 아래방향으로 채우면, 최대값 구할 수 있음

"""
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [[0]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if r-1>=0:
            DP[r][c] = max(DP[r][c], DP[r-1][c])
        if c-1>=0:
            DP[r][c] = max(DP[r][c], DP[r][c-1])
        if r-1>=0 and c-1>=0:
            DP[r][c] = max(DP[r][c], DP[r-1][c-1])

        DP[r][c] += arr[r][c]

print(DP[N-1][M-1])