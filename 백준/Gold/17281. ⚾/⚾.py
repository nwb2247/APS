"""
stage를 리스트로 관리하는 과정에서 시간이 많이 소요됨
비트마스킹으로 비벼보자
"""

from itertools import permutations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sms = list(map(lambda x:sum(x)*3, arr))
# print(sms)

def simul():
    global ans


    score = 0
    cbat = 0
    for ci in range(N):

        if score + (N-ci)*24 <= ans:
            break

        b1, b2, b3 = 0, 0, 0
        out = 0
        while out < 3:
            val = arr[ci][order[cbat]]
            if val == 0:
                out += 1
            elif val == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif val == 2:
                score += (b3 + b2)
                b3, b2, b1 = b1, 1, 0
            elif val == 3:
                score += (b3 + b2 + b1)
                b3, b2, b1 = 1, 0, 0
            else:
                score += (b3 + b2 + b1 + 1)
                b3, b2, b1 = 0, 0, 0
            cbat = (cbat+1)%9


    ans = max(ans, score)

ans = 0
for p in permutations(list(range(1, 9))):
    order = p[:3] + (0, ) + p[3:]
    simul()

print(ans)