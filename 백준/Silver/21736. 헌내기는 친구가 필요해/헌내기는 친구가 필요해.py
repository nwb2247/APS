from collections import deque

N, M = map(int, input().split())

arr = [input().rstrip() for _ in range(N)]
start = None
found_I = False
for r in range(N) :
    for c in range(M) :
        if arr[r][c] == 'I' :
            start = r, c
            found_I = True
            break
    if found_I :
        break

visited = [[False]*M for _ in range(N)]
ds = [[1,0],[0,1],[0,-1],[-1,0]]

q = deque()
q.append(start)
cnt = 0
while not len(q) == 0 :
    cr, cc = q.popleft()
    if visited[cr][cc] :
        continue
    visited[cr][cc] = True
    if arr[cr][cc] == 'P':
        cnt += 1
    for d in ds :
        nr, nc = cr+d[0], cc+d[1]
        if (0<=nr<N and 0<=nc<M and
                arr[nr][nc] != 'X' and
                not visited[nr][nc]) :
            q.append([nr, nc])
if cnt != 0 :
    print(cnt)
else :
    print("TT")