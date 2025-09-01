from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

N, Q = map(int, input().split())
R, C = 2**N, 2**N
arr = [list(map(int, input().split())) for _ in range(R)]
ops = list(map(int, input().split()))

# 0<=L<N
starts = [[] for _ in range(N+1)]

for l in range(N+1):
    for sr in range(0, R, 2**l):
        for sc in range(0, C, 2**l):
            starts[l].append((sr, sc))

def rotate(l):
    narr = [[0]*C for _ in range(R)]
    for sr, sc in starts[l]:
        br, bc = sr-1, sc-1
        offset_c = 2**l+1
        for cr in range(sr, sr+2**l):
            for cc in range(sc, sc+2**l):
                dr, dc = cr-br, cc-bc
                nr, nc = br+dc, bc-dr+offset_c
                narr[nr][nc] = arr[cr][cc]

    return narr

def melt():
    narr = [[0]*C for _ in range(R)]
    for cr in range(R):
        for cc in range(C):
            if arr[cr][cc] == 0:
                continue
            cnt = 0
            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if oob(nr, nc):
                    continue
                if arr[nr][nc] > 0:
                    cnt += 1
            if cnt >= 3:
                narr[cr][cc] = arr[cr][cc]
            else:
                narr[cr][cc] = arr[cr][cc] - 1

    return narr

def bfs():
    v = [[0]*C for _ in range(R)]
    mx = 0
    for sr in range(R):
        for sc in range(C):
            if arr[sr][sc] == 0:
                continue
            if v[sr][sc] != 0:
                continue
            q = deque()
            q.append((sr, sc))
            v[sr][sc] = 1
            cnt = 0

            while q:
                cr, cc = q.popleft()
                cnt += 1

                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if oob(nr, nc):
                        continue
                    if arr[nr][nc] == 0:
                        continue
                    if v[nr][nc] != 0:
                        continue
                    v[nr][nc] = 1
                    q.append((nr, nc))
            # print((sr, sc, cnt))
            mx = max(mx, cnt)

    return mx

for l in ops:
    arr = rotate(l)
    arr = melt()
    # print(l)
    # for l in arr:
    #     print(l)

print(sum(map(sum, arr)))
print(bfs())
