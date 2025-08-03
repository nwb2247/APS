"""
[조건]
N 사람수 , M 파티수 진실을 아는 사람수 각 파티오는 사람 수 모두 50 이하

[목표]
거짓말쟁이로 알려지지 않으면서 많은 파티를 참석하는 법

[접근]
거짓말쟁이로 알려지면 안되기 때문에 일단, 진실아는 파티에서는 진실 얘기해야함
한편 진실을 모르는 사람이라하더라도, 두 파티에서 서로 다른 말을 들으면 거짓말임을 알게 됨
즉 진실을 아는 사람이 참석한 파티 뿐만 아니라, 그 파티 참석한 사람들의 다른 파티, 또 다른 파티.... 에서도 거짓을 얘기하면 안됨
BFS로 이들을 연결하되, 파티의 인덱스를 N+1 ~ N+M로 연결 / visited_p 등에서 방문되지 않은 파티를 세기

[주의사항]
사람들의 번호는 1~N

"""
from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))

visited = [0]*(N+M+1)
adj = [[] for _ in range(N+M+1)]
q = deque()

for v in lst[1:]: # 사람들의 번호만 q에 저장 lst = [0]이어도 [1:]처럼 슬라이싱으로 가져오는 것은 인덱스에러 발생 X
    q.append(v)
    visited[v] = 1

for p in range(N+1, N+M+1): # 파티넘버는 N+1부터 시작 (N+1 ~ N+M)
    lst = list(map(int, input().split()))
    for v in lst[1:]:
        adj[p].append(v)
        adj[v].append(p)

while q:
    cur = q.popleft()

    for nxt in adj[cur]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            q.append(nxt)

print(visited[N+1:].count(0))   
# 파티 중에서 (N+1 ~ ) 방문되지 않은 것 갯수 세기