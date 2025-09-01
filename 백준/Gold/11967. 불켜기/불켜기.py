"""
이동 가능한 방이 아닌, 불이 켜진 방....

문제에서 요구하는게 뭔지 정확히 파악하자
"""


from collections import deque

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
R, C = N, N
info = [[[] for _ in range(C)] for _ in range(R)]   # 각 방에서 켤 수 있는 방
for _ in range(M):
    x, y, a, b = map(int, input().split())      # x,y 에서 a,b를 켤 수 있음
    info[x-1][y-1].append((a-1, b-1))

s = set() # 불이 켜진 방

v = [[0]*C for _ in range(R)]
q = deque()

v[0][0] = 1         # 0 미방문, 1미방문이나 불켜짐 2불켜져있고 방문
s.add((0, 0))       # 첫번째는 불이켜져 있음
q.append((0, 0))

w = set()           # 방문하지 못한 공간

# 스위치를 먼저 접할지, 미방문 공간을 먼저 접할지 모르므로 둘다 확인

while q:
    while q:
        cr, cc = q.popleft()

        for zr, zc in info[cr][cc]: # 각 방에서 켤 수 있는 것들을
            s.add((zr, zc))         # 켜진 방에 추가

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc       # 각 방향에 대해서
            if oob(nr, nc):
                continue
            if v[nr][nc] == 1:
                continue
            if (nr, nc) not in s:
                w.add((nr, nc))
                continue
            v[nr][nc] = 1
            q.append((nr, nc))

    get_lighted = []        # w 중에 켜진 것들을 저장
    for nr, nc in w:        # 아직 불이 꺼져 방문하지 못한 곳들 중에
        if (nr, nc) in s:   # 새롭게 켜진 방이 있다면
            v[nr][nc] = 1
            q.append((nr, nc))
            get_lighted.append((nr, nc))

    for nr, nc in get_lighted:  # 켜진 방들은 제거
        w.remove((nr, nc))

# for l in v:
#     print(l)
# print(sum(map(lambda x:x.count(1), v)))

print(len(s))       # 켜진 방의 수 세기



