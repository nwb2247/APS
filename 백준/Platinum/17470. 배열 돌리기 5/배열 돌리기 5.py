"""

01
23

(번호, 상하, 좌우, 회전수 오른쪽)

"""
import sys
input = sys.stdin.readline

UD = False
LR = False
ROT = 0
s = [[0, 1], [2, 3]]


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
p = [None]*4
p[0] = [lst[:C//2] for lst in arr[:R//2]]
p[1] = [lst[C//2:] for lst in arr[:R//2]]
p[2] = [lst[:C//2] for lst in arr[R//2:]]
p[3] = [lst[C//2:] for lst in arr[R//2:]]

p.append([lst[C//2] for lst in arr[:R//2]])
ops = list(map(int, input().split()))
for op in ops:
    if op == 1:
        s = [[s[1][0], s[1][1]], [s[0][0], s[0][1]]]
        if ROT % 2 == 0:
            UD = not UD
        else:
            LR = not LR
    elif op == 2:
        s = [[s[0][1], s[0][0]], [s[1][1], s[1][0]]]
        if ROT % 2 == 0:
            LR = not LR
        else:
            UD = not UD
    elif op == 3:
        ROT = (ROT + 1)%4
        s = [[s[1][0], s[0][0]], [s[1][1], s[0][1]]]
    elif op == 4:
        ROT = (ROT - 1)%4
        s = [[s[0][1], s[1][1]], [s[0][0], s[1][0]]]
    elif op == 5:
        s = [[s[1][0], s[0][0]], [s[1][1], s[0][1]]]
    elif op == 6:
        s = [[s[0][1], s[1][1]], [s[0][0], s[1][0]]]

# print(UD, LR, ROT)
# for l in s:
#     print(l)

np = [None]*4
for i in range(4):
    row, col = i//2, i%2
    a = p[s[row][col]]

    # 뒤집기 부터 먼저 수행
    if UD:
        at = [list(lst) for lst in zip(*a)]
        at = [lst[::-1] for lst in at]
        a = [list(lst) for lst in zip(*at)]
    if LR:
        a = [lst[::-1] for lst in a]

    for _ in range(ROT):
        at = [list(lst) for lst in zip(*a)]
        a = [lst[::-1] for lst in at]

    np[i] = a

res = []
for i in range(len(np[0])):
    res.append(np[0][i] + np[1][i])
for i in range(len(np[0])):
    res.append(np[2][i] + np[3][i])

for l in res:
    print(*l)

