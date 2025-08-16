"""
DP
"""

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
# for lst in W:
#     print(lst)
# print()

dp = [[dict() for _ in range(N)] for _ in range(N)]
for e in range(N):
    for s in range(N):
        if W[s][e] == 0:
            continue
        else:
            dp[s][e][(1<<s) | (1<<e)] = W[s][e]

# for i in range(N):
#     print(dp[i])
# print()

for _ in range(N-2):
    new_dp = [[dict() for _ in range(N)] for _ in range(N)]
    for s in range(N):
        for e in range(N):
            for ne in range(N):
                if s == ne or W[e][ne] == 0:
                    continue
                for k in dp[s][e]:
                    if (k & (1<<ne)) != 0:      # 이미 경유가 된 곳은 패스 (D) == 1로 하면 안됨
                        continue
                    if k | (1<<ne) in new_dp[s][ne]:
                        new_dp[s][ne][k | (1 << ne)] = min(new_dp[s][ne][k | (1 << ne)], dp[s][e][k] + W[e][ne])
                    else:
                        new_dp[s][ne][k | (1 << ne)] = dp[s][e][k] + W[e][ne]
    dp = new_dp
    # for i in range(N):
    #     print(dp[i])
    # print()

mn = float('inf')

for s in range(N):
    for e in range(N):
        for k in dp[s][e]:
            if k == ((1<<N) - 1) and W[e][s] != 0:
                # print(dp[s][e][((1<<N) - 1)] + W[e][s])
                mn = min(mn, dp[s][e][((1<<N) - 1)] + W[e][s])

print(mn)