import sys
sys.setrecursionlimit(11000)

def recurF(cur):    # 첫번째 수를 가지고 모든 조상을 구함
    if cur == -1:
        return
    visited[cur] = 1
    recurF(parent[cur])

def recurS(cur):    # 두번째 수에 대해 조상을 찾으면서 첫번째 조상과 겹치는 경우 ans에 저장하고 종료
    global ans
    if cur == -1:
        return
    if visited[cur] == 1:
        ans = cur
        return
    recurS(parent[cur])


TC = int(input())
for _ in range(TC):
    N = int(input())
    parent = [-1]*(N+1)
    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[c] = p
    F, S = map(int, input().split())
    visited = [0]*(N+1)
    ans = -1
    recurF(F)
    recurS(S)
    print(ans)