"""

"""
A, B = map(int, input().split())
K, X = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    if abs(i - K) <= X:
        cnt += 1
if cnt == 0:
    print("IMPOSSIBLE")
else:
    print(cnt)
