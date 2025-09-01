from collections import deque

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
R, C = N, N
info = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    info[x-1][y-1].append((a-1, b-1))

s = set() # 누른 스위치

v = [[0]*C for _ in range(R)]
q = deque()

v[0][0] = 1 # 0 미방문, 1미방문이나 불켜짐 2불켜져있고 방문
q.append((0, 0))

w = set() # 미방문 공간

# 스위치를 먼저 접할지, 미방문 공간을 먼저 접할지 모르므로 둘다 확인

while q:
    while q:
        cr, cc = q.popleft()

        for zr, zc in info[cr][cc]:
            s.add((zr, zc)) # 일단 누른 스위치에 추가

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if v[nr][nc] == 1:
                continue
            if (nr, nc) not in s:
                w.add((nr, nc))
                continue
            v[nr][nc] = 1
            q.append((nr, nc))

    get_lighted = []
    for nr, nc in w:
        if (nr, nc) in s:
            v[nr][nc] = 1
            q.append((nr, nc))
            get_lighted.append((nr, nc))

    for nr, nc in get_lighted:
        w.remove((nr, nc))

# for l in v:
#     print(l)
# print(sum(map(lambda x:x.count(1), v)))

s.add((0, 0))

print(len(s))



