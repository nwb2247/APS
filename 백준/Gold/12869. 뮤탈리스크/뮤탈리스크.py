"""
한번의 공격에서 같은걸 여러번 때릴 순 없음
-> 즉 각각 한번만 때릴 수 있음
때릴 수 있는 방법 백트래킹으로 만듦 3! (사실 6개.....)

때렸을때 모두 0 이하가 되면 종료 BFS
"""

from collections import deque

def backtrack(depth, lst):
    if depth == 3:
        ways.append(lst)
        return

    for i in range(3):
        if v[i] == 0:       # 지금까지 안넣은 것만 넣어줌
            v[i] = 1        # 방문처리
            backtrack(depth + 1, lst+[i])
            v[i] = 0        # 원상복구

ways = []
v = [0]*3
backtrack(0, [])

N = int(input())
state = tuple(map(int, input().split())) + (0, )*(3-N) # 3되도록 0으로 채워줌

# BFS를 이용해 최단 공격 횟수를 찾자...
q = deque()
q.append((state, 0))    # 현재 상태, 지금까지의 공격횟수
v = set()               # v에 상태를 넣어서 방문 표시
# (이전에 존재했던 상태인지... 존재한다면 그 상태에 도달되는 더 작은 공격횟수의 방법이 있다는 것이므로 넘어감)
v.add(state)
while q:
    state, cnt = q.popleft()    # 상태, 공격횟수

    if state.count(0) == 3: # 모두 -이라면...
        print(cnt)
        break

    for w in ways:  # w : [1, 2, 0] 1번 인덱스는 1,  2번인덱스는 3, 0번 인덱스는 9를 빼주겠다.. 
        tmp = [0]*3
        for i in range(3):
            tmp[w[i]] = max(state[w[i]] - 3**i, 0)  # 3**i를 뺀수 (1, 3, 9)로 채워줌 (음수라면 0)
        nstate = tuple(tmp)     # 방문여부 확인위해 tmp에 넣어줌
        if nstate in v:         # 이미 있었던 상태라면 continue
            continue
        v.add(nstate)           # 처음 보는 상태라면 넣어주고 +1 함
        q.append((nstate, cnt + 1))

# print(v)


