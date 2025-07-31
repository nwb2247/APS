N = int(input())
DP_max = [0, 0, 0]
DP_min = [0, 0, 0]
for _ in range(N):
    lst = list(map(int, input().split()))

    temp_max = [0, 0, 0]
    temp_max[0] = max(DP_max[:2]) + lst[0]
    temp_max[1] = max(DP_max) + lst[1]
    temp_max[2] = max(DP_max[1:]) + lst[2]
    DP_max = temp_max

    temp_min = [0, 0, 0]
    temp_min[0] = min(DP_min[:2]) + lst[0]
    temp_min[1] = min(DP_min) + lst[1]
    temp_min[2] = min(DP_min[1:]) + lst[2]
    DP_min = temp_min
print(max(DP_max), min(DP_min))
