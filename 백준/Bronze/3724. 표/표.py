import math

TC = int(input())
for _ in range(TC):
    M, N = map(int, input().split()) # N이 행의 수 M이 열의 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for lst in arr:
    #     print(lst)
    A = [0]*M
    for c in range(M):
        mul = 1
        for r in range(N):
            mul *= arr[r][c]
        A[c] = mul

    ans = -1
    mx = -math.inf
    for c in range(M):
        if A[c]>=mx:
            mx=A[c]
            ans = c+1
    print(ans)


