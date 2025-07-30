# 7:49 ~

L = 100

arr = [[False] * (L + 2) for _ in range(L + 2)]
N = int(input())
for _ in range(N):
    sr, sc = map(int, input().split())
    for r in range(sr + 1, sr + 11):
        for c in range(sc + 1, sc + 11):
            arr[r][c] = True
cnt = 0
for r in range(L + 1):
    for c in range(L + 2):
        if arr[r][c] != arr[r + 1][c]:
            cnt += 1
for c in range(L + 1):
    for r in range(L + 2):
        if arr[r][c] != arr[r][c + 1]:
            cnt += 1
print(cnt)
