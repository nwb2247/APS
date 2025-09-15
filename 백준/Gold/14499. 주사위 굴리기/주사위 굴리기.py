"""
N, M

주사위를 굴렸을때
바닥이 0이면 바닥에 복사
바닥이 0이 아니면 주사위에 복사, 바닥은 0됨
굴릴때마다 주사위 상단에 쓰여있는값

주사위 면정보에 대한 리스트 작성
"""

def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)

def roll(op):
    global dice, cr, cc
    ground, north, east, west, south, sky = dice
    new_ground, new_north, new_east, new_west, new_south, new_sky = dice

    dr, dc = ds[op]
    nr, nc = cr + dr, cc + dc
    if oob(nr, nc):
        return

    # 범위 내에 있어서 이동할 수 있다면
    if op == 1:  # 동
        new_ground = east
        new_west = ground
        new_sky = west
        new_east = sky
    elif op == 2:  # 서
        new_ground = west
        new_east = ground
        new_sky = east
        new_west = sky
    elif op == 3:  # 북
        new_ground = north
        new_south = ground
        new_sky = south
        new_north = sky
    elif op == 4:  # 남
        new_ground = south
        new_north = ground
        new_sky = north
        new_south = sky

    if arr[nr][nc] == 0:
        arr[nr][nc] = new_ground
    else:
        new_ground = arr[nr][nc]
        arr[nr][nc] = 0

    dice = [new_ground, new_north, new_east, new_west, new_south, new_sky]
    print(new_sky)

    cr, cc = nr, nc

N, M, sr, sc, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ops = list(map(int, input().split()))
cr, cc = sr, sc

ds = [(0,0)] + [(0,1), (0,-1), (-1,0), (1,0)] # 1:동, 2:서 3:북 4:남
dice = [0, 0, 0, 0, 0, 0] # 땅, 북, 동, 서, 남, 하늘

for op in ops:
    roll(op)



