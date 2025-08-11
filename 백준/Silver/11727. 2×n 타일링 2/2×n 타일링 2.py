"""
DP[1] = 1
DP[2] = 3
DP[3] = DP[2] + DP[1]*2
DP[4] = DP[3] + DP[2]*2
....

DP[K] = DP[K-1] + DP[K-2]*2 => K-1에다가 세로 작대기 하나 붙인 것 + k-2에다가 = ㅁ 붙인것

"""

N = int(input())
DP = [0]*(N+1)
DP[0] = 1
DP[1] = 1

Z = 10007

for i in range(2, N+1):
    DP[i] = (DP[i-1] + DP[i-2]*2)%Z

print(DP[N])
