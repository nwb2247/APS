"""
플로이드 워셜이 어떻게 임의의 한 정점에서 다른 정점까지의 최단 거리를 보장하는가
플로이드 워셜
for k in range(N):
    for i in range(N): # start
        for j in range(N): # end
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]

d_k [i][j] : 1~k까지의 정점 경유를 허용했을때 i와 j간의 최단 거리
d_0 [i][j]는 중간 정점 경유가 없는 i, j의 최단거리

1. 기저 조건 k=0
d_0 [i][j]는 중간 정점 경유가 없는 i, j의 최단거리, 가중치 없으면 inf
중간 정점 없이 갈 수 있는 최단 거리이므로 성립

2. 귀납 가정
d_k [i][j] : 1~k까지의 정점 경유를 허용했을때 i와 j간의 최단 거리라고 가정하자

3. 귀납 단계 (k->k+1)
d_k+1 [i][j] 는 다음 중 더 작은 값이다.
    1. 1~k 만을 허용한 d_k[i][j]
    2. k+1를 반드시 거치는 d_k[i][k+1] + d_k[k+1][j]
따라서 d_k+1 [i][j] = min(d_k[i][j], d_k[i][k+1] + d_k[k+1][j])
"""

N, M = map(int, input().split())
dist = [[N+1]*(N+1) for _ in range(N+1)] # 유저수보다 거리가 길 순 없으므로 N+1으로 초기화

for i in range(1, N+1):
    dist[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

mn_idx = 0
mn = (N+1)**2
for i in range(1, N+1):
    sm = sum(dist[i][1:])
    if sm < mn:
        mn = sm
        mn_idx = i
        # 여러명일 경우 작은 사람만 출력
        # 그런데 <일때만 갱신하므로 여러명이어도 처음 사람만 기록됨

print(mn_idx)
