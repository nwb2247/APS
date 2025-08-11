N = int(input())
lst = list(map(int, input().split()))

# DP 초기화
DP = [0]*N
DP[0] = lst[0]

ans = lst[0]
for i in range(1, N):
    if DP[i-1] <= 0: # 0보다 작거나 같으면 더해줘봤자 더 작거나 같으므로 새롭게 시작
        DP[i] = lst[i]
    else:
        DP[i] = DP[i-1]+lst[i]  # 0보다 크면 무조건 커지므로 계속 더해줌
    ans = max(ans, DP[i])
print(ans)