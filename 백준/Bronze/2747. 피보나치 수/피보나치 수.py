"""
DP :
바텀업 (루프)    : 미리 필요한 값들을 만들어두고 사용 (타뷸레이션)
탑다운 (재귀)    : 값이 필요하다면 만들어 가면서 사용 (메모이제이션)
"""

N = int(input())
DP = [-1]*(N+1)
DP[0] = 0
DP[1] = 1

# 바텀업
for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N])

# 탑다운
# def fibo(i):
#     if DP[i] == -1:
#         DP[i] = fibo(i-1)+fibo(i-2)
#     return DP[i]
# print(fibo(N))

