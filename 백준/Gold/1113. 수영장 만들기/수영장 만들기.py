"""
sr, sc로
처음높이 + 1에서 시작해서 여기에 얼마높이의 물을 댈수 있는지 확인

시간복잡도
N*M * N*M * 10 => 62500000

"""
from collections import deque


def oob(r, c):      # 물밖으로 흐르는지 확인
    return not (0 <= r < N and 0 <= c < M)


def check():        # 현재 높이 h에서 안넘치게 채울 수 있는 좌표를 반환
    VISITED = [[0] * M for _ in range(N)]
    q = deque()

    pos = []

    VISITED[sr][sc] = 1
    q.append((sr, sc))
    while q:
        cr, cc = q.popleft()
        pos.append((cr, cc))

        for dr, dc in DS:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):             # 범위밖으로 넘쳐 흐르면 빈리스트 반환
                return []

            if ARR[nr][nc] < h and VISITED[nr][nc] == 0:    # h보다 작은 경우만 넣어야 경계가 h일때 흐르지 않음
                VISITED[nr][nc] = 1
                q.append((nr, nc))

    return pos



DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
ARR = [list(map(int, input())) for _ in range(N)]   # 입력
RES = [[-1]*M for _ in range(N)]                    # 각 좌표에서 가능한 최대 높이

for sr in range(N):
    for sc in range(M):
        if RES[sr][sc] != -1:      # 다른 곳에 이미 채워졌다면 continue
            continue
        RES[sr][sc] = ARR[sr][sc]   # 아니라면 일단 내 높이로 넣고 시작 (물을 안채운 상태)
        for h in range(ARR[sr][sc] + 1, 10):    # 각 높이마다 가능 여부를 확인 (높이 + 1 ~ 9)
            pos = check()
            if pos:                 # 빈리스트가 아니고 h로 채울 수 있는 곳이 있다면 넣음
                for zr, zc in pos:
                    RES[zr][zc] = h
            else:
                break               # 없다면 그 위 높이는 확인필요없으므로 break

cnt = 0
for r in range(N):
    # print(RES[r])
    for c in range(M):
        cnt += RES[r][c] - ARR[r][c]        # 채워진 높이와 입력 높이 (바닥) 의 차이 더해줌
print(cnt)


