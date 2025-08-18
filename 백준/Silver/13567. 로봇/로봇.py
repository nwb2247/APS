"""

로봇 초기
0, 0 동쪽 방향

TURN 0 : 왼쪽 회전
TURN 1 : 오른쪽 회전
MOVE d : d만큼 이동 (양수)

단 로봇이 "경계" 또는 내부에 있는 경우만 유효 (경계를 위해 M+1 필요)

명령어 열이 모두 유효해야만 유요한 명령어열

"""

def oob(x, y):
    return not (0<=x<M+1 and 0<=y<M+1) # M:한변 길이 (경계에 있는것은 OK이므로 +1해줘야함

M, N = map(int, input().split())  # N개 명령어 (M, N 주의)
DS = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 우상좌하 (TURN 0기준으로)


def solve():
    cx, cy, cd = 0, 0, 0
    for _ in range(N):
        # print(cx, cy, cd)
        st = input().split()
        op = st[0]
        num = int(st[1])
        if op == "TURN":
            if num == 0:
                cd = (cd + 1)%4
            else:
                cd = (cd + 4 - 1)%4
        else:   # MOVE
            dx, dy = DS[cd]
            nx, ny = cx+dx*num, cy+dy*num
            if oob(nx, ny):
                return nx, ny
            else:
                cx, cy = nx, ny
    return cx, cy
x, y = solve()
if oob(x, y):
    print(-1)
else:
    print(x, y)
