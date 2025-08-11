"""
i번째를 포함하는 최장 증가 부분 수열 길이
DP[i] = max({DP[k] + 1 | 0<=k<i and lst[k] < lst[i]})
즉, 0~i-1에서 작은 수를 찾고 그것의 가장 긴 증가하는 부분 수열 길이 + 1

N<=1000이므로 N^2 ok
"""

N = int(input())
lst = list(map(int, input().split()))

DP = [1]*N # 항상 자기 자신의 길이가 있으므로 1로 초기화

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))
# (D) : DP(N-1)은 N-1번째를 포함하는 최장증가부분수열 길이이므로
# 가장 긴 것을 구하려면 max(DP)가 맞음