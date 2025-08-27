from collections import deque

DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def bfs():
    global sr, sc, size, to_eat, sec

    q = deque()
    v = [[-1]*N for _ in range(N)]

    q.append((sr, sc))
    v[sr][sc] = 0

    edible = []
    dist = -1
    while q:
        cr, cc = q.popleft()

        if dist != -1 and dist < v[cr][cc]:
            break

        if arr[cr][cc] != 0 and arr[cr][cc] < size and (dist == -1 or dist == v[cr][cc]):
            dist = v[cr][cc]
            edible.append((cr, cc))

        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] <= size and v[nr][nc] == -1:
                v[nr][nc] = v[cr][cc] + 1
                q.append((nr, nc))

    # print(edible)
    # for l in v:
    #     print(l)

    if dist == -1:
        return False

    edible.sort(key=lambda x:(x[0], x[1]))
    cr, cc = edible[0]
    arr[cr][cc] = 0
    to_eat -= 1
    sec += dist
    sr, sc = cr, cc
    if to_eat == 0:
        size += 1
        to_eat = size

    return True

    # for l in v:
    #     print(l)
    # print()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


sr, sc = -1, -1
for zr in range(N):
    for zc in range(N):
        if arr[zr][zc] == 9:
            sr, sc = zr, zc
            arr[sr][sc] = 0

sec = 0
size = 2
to_eat = 2
while True:
    if not bfs():
        break
print(sec)


