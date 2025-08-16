"""
DP + 비트 마스킹
시도 1.
DP[s][e][mask] : 시작, 마지막 방문, 지금까지 방문한 곳
O(N^3 * 2*N)

시도 2.
DP[e][mask] : 0으로 시작점 고정 (어차피 사이클이기 때문에 어딜 먼저 시작지로 잡아도 0을 무조건 거쳐야함)
O(N^2 * 2*N)
"""

# 시도 1 (s차원이용안하고 시작점 0으로 고정
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [dict() for _ in range(N)]
for e in range(1, N):
    if W[0][e] != 0:
        dp[e][(1<<0) | (1<<e)] = W[0][e]

# for i in range(N):
#     print(dp[i])
# print()

for _ in range(N-2):
    new_dp = [dict()for _ in range(N)]
    for e in range(N):        # 마지막에 방문한 곳
        for ne in range(N):   # 새로운 방문지
            if W[e][ne] == 0:      # e에서 ne로 갈 수 없으면 넘어감
                continue
            for k in dp[e]:
                if (k & (1<<ne)) != 0:        # 이미 경유가 된 곳은 패스 (D) == 1로 하면 안됨
                    continue
                if k | (1<<ne) in new_dp[ne]:
                    new_dp[ne][k | (1 << ne)] = min(new_dp[ne][k | (1 << ne)], dp[e][k] + W[e][ne])
                else:
                    new_dp[ne][k | (1 << ne)] = dp[e][k] + W[e][ne]
    dp = new_dp
    # for i in range(N):
    #     print(dp[i])
    # print()

mn = float('inf')

for e in range(N):
    for k in dp[e]:
        if k == ((1<<N) - 1) and W[e][0] != 0:
            mn = min(mn, dp[e][((1<<N) - 1)] + W[e][0])

print(mn)


# # 시도 1 (s차원이용)
# N = int(input())
# W = [list(map(int, input().split())) for _ in range(N)]
# # for lst in W:
# #     print(lst)
# # print()
#
# dp = [[dict() for _ in range(N)] for _ in range(N)]
# for e in range(N):
#     for s in range(N):
#         if W[s][e] == 0:
#             continue
#         else:
#             dp[s][e][(1<<s) | (1<<e)] = W[s][e]
#
# # for i in range(N):
# #     print(dp[i])
# # print()
#
# for _ in range(N-2):
#     new_dp = [[dict() for _ in range(N)] for _ in range(N)]
#     for s in range(N):            # 시작지
#         for e in range(N):        # 마지막에 방문한 곳
#             for ne in range(N):   # 새로운 방문지
#                 if s == ne or W[e][ne] == 0:      # 시작지와 도착지가 같거나, e에서 ne로 갈 수 없으면 넘어감
#                     continue
#                 for k in dp[s][e]:
#                     if (k & (1<<ne)) != 0:        # 이미 경유가 된 곳은 패스 (D) == 1로 하면 안됨
#                         continue
#                     if k | (1<<ne) in new_dp[s][ne]:
#                         new_dp[s][ne][k | (1 << ne)] = min(new_dp[s][ne][k | (1 << ne)], dp[s][e][k] + W[e][ne])
#                     else:
#                         new_dp[s][ne][k | (1 << ne)] = dp[s][e][k] + W[e][ne]
#     dp = new_dp
#     # for i in range(N):
#     #     print(dp[i])
#     # print()
#
# mn = float('inf')
#
# for s in range(N):
#     for e in range(N):
#         for k in dp[s][e]:
#             if k == ((1<<N) - 1) and W[e][s] != 0:
#                 # print(dp[s][e][((1<<N) - 1)] + W[e][s])
#                 mn = min(mn, dp[s][e][((1<<N) - 1)] + W[e][s])
#
# print(mn)