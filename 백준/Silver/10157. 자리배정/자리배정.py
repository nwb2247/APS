C, R = map(int, input().split())
ds = [[1,0],[0,1],[-1,0],[0,-1]]
K = int(input())

visited = [[0]*(C+2) for _ in range(R+2)]
for cr in range(R+2):
    visited[cr][0] = 1
    visited[cr][C+1] = 1
for cc in range(C+2):
    visited[0][cc] = 1
    visited[R+1][cc] = 1

di = 0
cr, cc = 1, 1
visited[cr][cc] = 1

if K<=R*C:
    for i in range(2, K+1):
        dr, dc = ds[di]
        nr, nc = cr+dr, cc+dc
        if visited[nr][nc] == 1:
            di = (di+1)%4
            dr, dc = ds[di]
            nr, nc = cr + dr, cc + dc
        cr, cc = nr, nc
        visited[cr][cc] = 1
    print(cc, cr)
else:
    print(0)



