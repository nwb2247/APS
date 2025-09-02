"""
한번의 공격에서 같은걸 여러번 때릴 순 없음
-> 즉 각각 한번만 때릴 수 있음

때렸을때 모두 0 되면 종료 BFS
"""

from collections import deque

def backtrack(depth):
    if depth == 3:
        ways.append(wlst[:])
        return

    for i in range(3):
        if v[i] == 0:
            v[i] = 1
            wlst[depth] = i
            backtrack(depth + 1)
            v[i] = 0

ways = []
v = [0]*3
wlst = [0]*3
backtrack(0)

N = int(input())
state = tuple(map(int, input().split())) + (0, )*(3-N)

q = deque()
q.append((state, 0))
v = set()
v.add(state)
while q:
    state, cnt = q.popleft()

    if state.count(0) == 3:
        print(cnt)
        break

    for w in ways:
        tmp = [0]*3
        for i in range(3):
            tmp[w[i]] = max(state[w[i]] - 3**i, 0)
        nstate = tuple(tmp)
        if nstate in v:
            continue
        v.add(nstate)
        q.append((nstate, cnt + 1))

# print(v)


