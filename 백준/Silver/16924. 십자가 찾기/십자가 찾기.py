"""
십자가 끼리는 겹쳐도 됨
N*M 개 이하로만 사용
(무한히 겹치지 않는 이상은 상관없을듯?)

십자가의 크기는 1이상 (3x3)

(접근)
각 *모양에 대해서 그것을 중심으로 하는 십자가 형상인 최대 크기를 확인하고 배열에 넣어줌
그리고 새도화지에 하나씩 꺼내면서 십자가를 그리고 원본과 일치하는지 확인
일치하면 넣어주고 일치하지 않으면 -1 출력
(최소 갯수가 아니므로 상관 X)

"""
def oob(r, c):
    return not (0<=r<N and 0<=c<M)

def cross_size(sr, sc):
    lng = 1
    while True:
        for dr, dc in DS:
            nr, nc = sr+dr*lng, sc+dc*lng
            if oob(nr, nc) or ARR[nr][nc] != "*":
                return lng-1
        lng += 1
    return -1


N, M = map(int, input().split())
ARR = [list(input()) for _ in range(N)]
DS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
crosses = []

for r in range(N):
    for c in range(M):
        if ARR[r][c] == "*":
            size = cross_size(r, c)
            if size >= 1:
                crosses.append((r, c, size))

NEW_ARR = [["."]*M for _ in range(N)]
for r, c, size in crosses:
    for l in range(size+1):
        for dr, dc in DS:
            nr, nc = r+dr*l, c+dc*l
            NEW_ARR[nr][nc] = "*"

is_same = True
for r in range(N):
    for c in range(M):
        if ARR[r][c] != NEW_ARR[r][c]:
            is_same = False
            break
    if not is_same:
        break

if is_same:
    print(len(crosses))
    for r, c, size in crosses:
        print(r+1, c+1, size)
else:
    print(-1)


