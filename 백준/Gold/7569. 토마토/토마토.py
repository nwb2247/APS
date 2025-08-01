# bfs 사용, 모두 익는 최소 일수
# 토마토의 개수 NMH 아닐 수 있음 (-1개수를 세서 빼기, 큐에서 꺼낼때 세자)

from collections import deque

ds = [[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]] # [위아래, 세로, 가로]

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

cnt = M*N*H
for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1: # 네번째는 day
                q.append((h,r,c,0)) # 개수세는건 확인을 꺼낼 때 cnt -=1 해서 0이 되면 전부 익은 것
                visited[h][r][c] = 1
            elif box[h][r][c] == -1:
                cnt -= 1          # -1 제외하고
# 익은 것 전부 넣고 하나씩 꺼내기, 익은 날짜도 함께,,

ans = -1
while q:
    ch, cr, cc, day = q.popleft()
    cnt -= 1 # 꺼냈으면 cnt 하나 줄임 0 되면 모두 익은 것..
    ans = max(ans, day)
    for dh, dr, dc in ds:
        nh, nr, nc = ch+dh, cr+dr, cc+dc
        if 0<=nh<H and 0<=nr<N and 0<=nc<M:
            if box[nh][nr][nc] == 0 and visited[nh][nr][nc] == 0:
                visited[nh][nr][nc] = 1
                q.append((nh, nr, nc, day+1))

if cnt == 0:
    print(ans)
else:
    print(-1)


