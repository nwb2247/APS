"""
DP :
바텀업 (루프)    : 미리 필요한 값들을 만들어두고 사용 (타뷸레이션)
탑다운 (재귀)    : 값이 필요하다면 만들어 가면서 사용 (메모이제이션)
"""

N = int(input())

DP = [N]*(N+1)
DP[1] = 0
# 바텀업
for i in range(2, N+1):
    if i%3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)
    if i%2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    DP[i] = min(DP[i], DP[i-1] + 1)

print(DP[N])