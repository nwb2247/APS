"""
1. 문제 꼼꼼히 읽고 손으로 예제 케이스를 확인하면서 규칙 이해하기
    - 이후 문제를 다시 한번 더 찬찬히 읽어보면서 빠뜨린 사항 있는지 확인
2. 입력, 입력의 범위, 개수, 목표, 출력 형태 다시 한번 살피기
3. 엣지 케이스 미리 생각해보고 코드 작성시 주의할 점에 대해 생각해보기
4. 단계별로 어떤 작업을 수행할지 주석으로 간단히 정리하기
5. 코드를 짜면서 왜 이러한 자료구조를 생성했는지 주석 달아두기
    - 다른 기능 보다가 다시 돌아왔을때 왜 이렇게 작성했었는지 헷갈리지 않도록...
"""
from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(sr, sc):

    # BFS 돌리면서 cluster에 정점 좌표 저장
    q = deque()
    visited = [[0] * C for _ in range(R)]
    q.append([sr, sc])
    visited[sr][sc] = 1

    cluster = []

    # 클러스터의 c의 범위 구하고, 각 c마다 최대 r을 저장
    c_mx = 0
    c_mn = C
    r_mxs = [0]*C

    while q:
        cr, cc = q.popleft()
        c_mn = min(c_mn, cc)
        c_mx = max(c_mx, cc)
        r_mxs[cc] = max(r_mxs[cc], cr)
        cluster.append([cr, cc])
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                if cave[nr][nc] == 'x':
                    visited[nr][nc] = 1
                    q.append([nr, nc])

    # 각 c마다 돌면서 클러스터의 가장 아랫부분과 그 아래쪽의 벽 or x 간의 높이차 최소 계산 (즉, 클러스터가 떨어지게 될 거리)
    l_mn = R-1
    for cc in range(c_mn, c_mx+1):
        for cr in range(r_mxs[cc]+1, R):    # 주의 : r_mxs[cc]는 클러스터의 가장 낮은 부분이므로 r_mxs[cc]+1부터 빈칸후보임
            if cave[cr][cc] == 'x':
                l_mn = min(l_mn, cr - r_mxs[cc]-1)
                break
        else:
            l_mn = min(l_mn, R-1-r_mxs[cc])


    # print(c_mn, c_mx)
    # print(r_mxs, r_mns)
    # print(cluster, l_mn)

    # 이제 cluster에 cr,cc에 대해서 먼저 빈칸으로 만들고 이후에 cr+l_mn에 x를 찍음
    # 주의 : 동시에 하면 덧씌워지는 경우 있으므로 X
    for cr, cc in cluster:
        cave[cr][cc] = "."
    for cr, cc in cluster:
        cave[cr+l_mn][cc] = "x"


R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
hs = list(map(int, input().split()))

for i in range(N):
    r = -1      # 막대기 도착한 좌표 찾고, .로 바꿔주기 / i%2에 따라 왼쪽에서 던진건지 오른쪽에서 던진건지 확인
    if i % 2 == 0:
        for c in range(C):
            if cave[R - hs[i]][c] == 'x':
                cave[R - hs[i]][c] = '.'
                r = R - hs[i]
                break
    else:
        for c in range(C - 1, -1, -1):
            if cave[R - hs[i]][c] == 'x':
                cave[R - hs[i]][c] = '.'
                r = R - hs[i]
                break

    for dr, dc in ds:           # 사방으로 BFS돌려서 클러스터 확인
        sr, sc = r + dr, c + dc
        if 0 <= sr < R and 0 <= sc < C:
            if cave[sr][sc] == 'x':
                bfs(sr, sc)
# 결과 출력
for lst in cave:
    print("".join(lst))
