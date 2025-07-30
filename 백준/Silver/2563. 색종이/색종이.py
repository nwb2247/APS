# 7:42~7:45
# 구현

arr = [[False]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    sr, sc = map(int, input().split())
    for r in range(sr, sr+10):
        for c in range(sc, sc+10):
            arr[r][c] = True
cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] : cnt += 1
print(cnt)
