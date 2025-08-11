"""
1,2 칸씩 올라올수 있으나, 연속된 세계단은 불가

[0] : 1칸 밟고 올라온
[1] : 2칸 밟고 올라온

꼭 마지막 계단 밟아야 하므로 max(DP[N-1])

"""

N = int(input())
offset = 2  # # 계단 한개인 경우도 일반화 위해 offset 사용
lst = [int(input()) for _ in range(N)]

DP = [[0] * 2 for _ in range(N + offset)]

for i in range(N):
    DP[i + offset][0] = DP[i + offset - 1][1] + lst[i]
    DP[i + offset][1] = max(DP[i + offset - 2]) + lst[i]

# for i in range(N):
#     print(lst[i], DP[i + offset])

print(max(DP[N-1+offset]))
