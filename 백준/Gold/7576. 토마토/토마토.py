from collections import deque

ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # visited와 겸용

q = deque()
cnt = 0
wall_num = 0 # M*N-wall_num : 전체 토마토의 개수
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append([r, c, 0])
            # 주의 : pop할 때 cnt += 1 할 것이므로 여기서는 X
        elif arr[r][c] == -1:
            wall_num += 1

ans = 0
while q:
    cr, cc, day = q.popleft()
    cnt += 1
    ans = max(ans, day)
    for dr, dc in ds:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < M:     # 범위 내에 있고
            if arr[nr][nc] == 0:            # 방문하지 않았다면
                arr[nr][nc] = 1
                q.append([nr, nc, day+1])   # 날짜 1일 추가
if cnt != M*N-wall_num:
    day = -1
print(day)
