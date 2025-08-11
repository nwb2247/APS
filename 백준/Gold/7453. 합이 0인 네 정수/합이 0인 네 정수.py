"""
a, b 묶어서 합 경우의 수 만들고
c, d 묶어서 합 경우의 수 만들고
-(a+b)가 (c+d) 있는지 확인
"""

N = int(input())
A, B, C, D = [0]*N, [0]*N, [0]*N, [0]*N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

cnt = dict()
for a in A:
    for b in B:
        if a+b in cnt:
            cnt[a+b] += 1
        else:
            cnt[a+b] = 1

ans = 0
for c in C:
    for d in D:
        if -(c+d) in cnt:
            ans += cnt[-(c+d)]

print(ans)
