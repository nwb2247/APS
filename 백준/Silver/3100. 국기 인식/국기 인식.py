"""
https://www.acmicpc.net/problem/3100

[조건]
삼"등"분
6*9 = 54
(한 등분 = 18)
가운데 색은 나머지 두줄과 달라야함

[목표]
삼등분된 국기가 되기 위해 바꿔야하는 최소 문자

[접근]
가운데부터 선택해주고
이때 이미 있는 색을 선택하면 안되는 경우까지 고려해서, 세 부분에 대해 26가지를 모두 고려하자
(26**3)
"""

R = 6
C = 9

arr = [list(input()) for _ in range(R)]
arr_T = [list(x) for x in zip(*arr)]
clist = [chr(i) for i in range(ord("A"), ord("Z")+1)]

horizontal = [{} for _ in range(3)]
vertical = [{} for _ in range(3)]

for i, rng in enumerate([[0,2],[2,4],[4,6]]):
    s, e = rng
    for c in clist:
        horizontal[i][c] = 0
        for lst in arr[s:e]:
            horizontal[i][c] += C-lst.count(c)

for i, rng in enumerate([[0,3],[3,6],[6,9]]):
    s, e = rng
    for c in clist:
        vertical[i][c] = 0
        for lst in arr_T[s:e]:
            vertical[i][c] += R-lst.count(c)

mn = float('inf')

for i, c1 in enumerate(clist):
    for c0 in clist[:i] + clist[i+1:]:
        for c2 in clist[:i] + clist[i+1:]:
            mn = min(mn, horizontal[0][c0] + horizontal[1][c1] + horizontal[2][c2])
            mn = min(mn, vertical[0][c0] + vertical[1][c1] + vertical[2][c2])

print(mn)