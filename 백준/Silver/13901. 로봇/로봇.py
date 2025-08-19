"""
벽, 방문지, 장애물 만나면 방향전환
다음 방향 없다면 맨 처음방향으로 돌아감

움직일 수 없으면 멈춤

멈추는 위치 출력
00 - R-1C-1
"""
R, C = map(int, input().split())
K = int(input())
ARR = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(K):
    zr, zc = map(int, input().split())
    ARR[zr][zc] = 1  # 벽 or 방문지
sr, sc = map(int, input().split())
DIRS = list(map(int, input().split()))
# print(sr, sc)
# print(DIRS)

DS = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 1위 2아래 3왼 4오른

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

cr, cc, cd = sr, sc, 0 # cd 관리 주의!!!! DIR 사용해야함
ARR[sr][sc] = 1
ar, ac = -1, -1
cnt = 0
while True:
    dr, dc = DS[DIRS[cd]]
    nr, nc = cr+dr, cc+dc
    if oob(nr, nc) or ARR[nr][nc]:
        cd = (cd+1)%len(DIRS)
        cnt += 1
        if cnt == 4:
            ar, ac = cr, cc
            break
        continue
    cnt = 0
    cr, cc = nr, nc
    ARR[cr][cc] = 1
print(ar, ac)
