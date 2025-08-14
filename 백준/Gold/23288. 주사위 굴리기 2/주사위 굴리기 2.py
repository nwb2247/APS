"""
주사위 아랫면과 도착 면 비교해서 방향 결정
=> 이동방향에 칸이 없다면 (맵밖) 이동 방향을 반대로 한 다음 한 칸 굴러감

처음 방향 동쪽
처음 좌표 0,0


이동 횟수 K동안 얻는 점수의 합

"""
from collections import deque


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)

def bfs(r, c, num):
    q = deque()
    visited = [[0]*M for _ in range(N)]

    visited[r][c] = 1
    q.append((r,c))
    score = 0

    while q:
        cr, cc = q.popleft()
        score += 1

        for dk in ds:
            dr, dc = ds[dk]
            # print(dk)
            nr, nc = cr+dr, cc+dc
            if not oob(nr, nc) and arr[nr][nc] == num and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    # for lst in visited:
    #     print(lst)

    return score

def roll(d):
    global dice

    sky, ground, east, west, south, north = dice
    new_sky, new_ground, new_east, new_west, new_south, new_north = dice

    if d == "N":
        new_north = sky
        new_sky = south
        new_south = ground
        new_ground = north
    elif d == "S":
        new_north = ground
        new_sky = north
        new_south = sky
        new_ground = south
    elif d == "W":
        new_west = sky
        new_sky = east
        new_east = ground
        new_ground = west
    elif d == "E":
        new_west = ground
        new_sky = west
        new_east = sky
        new_ground = east
    else:
        print("!!!!!!!!!")

    dice = [new_sky, new_ground, new_east, new_west, new_south, new_north]


N, M, K = map(int, input().split())

dice = [1, 6, 3, 4, 5, 2]  # 하늘, 땅, 동, 서, 남, 북
curd = "E"
cr, cc = 0, 0

arr = [list(map(int, input().split())) for _ in range(N)]

ds = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
revd = {"N": "S", "S": "N", "E": "W", "W": "E"}
clock = {"N":"E", "E":"S", "S":"W", "W":"N"}
rev_clock = {"E":"N", "S":"E", "W":"S", "N":"W"}

sm = 0
cnt = 0
while cnt < K:

    # print(cr, cc, sm)
    dr, dc = ds[curd]
    nr, nc = cr + dr, cc + dc
    if oob(nr, nc):
        curd = revd[curd]
        dr, dc = ds[curd]
        nr, nc = cr + dr, cc + dc

    roll(curd)
    cr, cc = nr, nc

    A = dice[1]       # ground 1번 (주사위 밑 바닥을 의미)
    B = arr[cr][cc]         # 지도 상 번호를 의미
    C = bfs(cr, cc, B)
    sm += B*C

    if A > B:
        curd = clock[curd]
    elif A < B:
        curd = rev_clock[curd]

    cnt += 1

print(sm)
