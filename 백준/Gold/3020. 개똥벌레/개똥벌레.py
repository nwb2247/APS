"""
[조건]
N 길이 <= 200_000
H 높이 <= 500_500
장애물크기는 1~H-1

[목표]
파괴해야하는 장애물의 최소값과 그러한 구간이 총 몇개 있는지

[접근]
"""

N, H = map(int, input().split())

lst = [int(input()) for _ in range(N)]

cnt = [0]*(H+1)

for i in range(0, N, 2):
    cnt[lst[i]] += 1

for h in range(H-1, 0, -1):
    cnt[h] += cnt[h+1]

cnt1 = [0]*(H+1)

for i in range(1, N, 2):
    cnt1[H-lst[i]+1] += 1

for h in range(1, H+1):
    cnt1[h] += cnt1[h-1]

for h in range(1, H+1):
    cnt[h] += cnt1[h]

mn = min(cnt[1:])
print(mn, cnt[1:].count(mn))