"""
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

=> 규칙을 지키기 위해
첫 색칠이 무엇이었는지 기억하면서 올라가기
DP[몇번째 칠하는지][칠할색][첫색]

편의상 0번부터 시작으로 바꾸기
"""
INF = 1000*1000+1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[[INF for k in range(3)] for j in range(3)] for i in range(N)] # 012 RGB
for i in range(3):
        DP[0][i][i] = arr[0][i]

for i in range(1, N):
    for cur in range(3):
        for prev in range(3):
            if cur == prev:
                continue
            for first in range(3):
                DP[i][cur][first] = min(DP[i][cur][first], DP[i-1][prev][first]+arr[i][cur])

ans = INF
#
# for l in DP:
#     print(l)

for cur in range(3):
    for first in range(3):
        if cur == first:
            continue
        ans = min(ans, DP[N-1][cur][first])

print(ans)
