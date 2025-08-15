N = int(input())

DP = [0]*1001
DP[1] = 1       # 시작하는 사람(상근)이 이기면 1, 지면 -1
DP[2] = -1
DP[3] = 1
DP[4] = 1
for i in range(5, N+1):
    for j in [i-1, i-3, i-4]:   # 돌을 1, 3, 4 빼는 경우에 (상근)
        if DP[j] == -1:         # 성영이가 지는 경우가 있다면
            DP[i] = 1           # 상근 이김
            break
    else:                       # 성영을 지게 하는 수가 없다면
        DP[i] = -1              # 성영이김

if DP[N] == 1:
    print("SK")
else:
    print("CY")