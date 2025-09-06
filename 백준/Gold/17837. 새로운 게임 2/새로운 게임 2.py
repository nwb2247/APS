ds = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 우0 좌1 상2 하3
rev = [1, 0, 3, 2] # 반대방향
N, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)] # 0, 1, 2 지도

# 말 정보
u = [[[] for _ in range(N)] for _ in range(N)] # 각 위치에 어떤 유닛이 있는지 + 방향
pos = [None] + [(-1, -1) for _ in range(K)] # 각 유닛이 현재 어디에 있는지 (유닛번호는 1부터 K)
dirs = [None] + [0 for _ in range(K)] # 방향 정보 !!!!!! 움직일 때 위의 말들도 같이 움직이므로 같이 pos를 수정해야함

# 좌표 방향 모두 -1 씩 받기
for NUM in range(1, K+1): # 유닛 번호는 헷갈리니까 1부터 받자
    CR, CC, CD = map(lambda x:int(x)-1, input().split())
    u[CR][CC].append(NUM)
    pos[NUM] = (CR, CC)
    dirs[NUM] = CD

# -------------- 함수 ----------------

def oob(r, c):
    return not(0<=r<N and 0<=c<N)

def move_white(num, cr, cc, nr, nc):
    lst = u[cr][cc][u[cr][cc].index(num):]  # num말 포함 위의 모든 말들
    u[cr][cc] = u[cr][cc][:u[cr][cc].index(num)]  # num 아래 말들만 남김
    u[nr][nc] = u[nr][nc] + lst
    for i in lst:
        pos[i] = (nr, nc)
    return len(u[nr][nc])

def move_red(num, cr, cc, nr, nc):
    lst = u[cr][cc][u[cr][cc].index(num):]  # num말 포함 위의 모든 말들
    u[cr][cc] = u[cr][cc][:u[cr][cc].index(num)]  # num 아래 말들만 남김
    lst.reverse()  # INPLACE
    u[nr][nc] = u[nr][nc] + lst
    for i in lst:
        pos[i] = (nr, nc)
    return len(u[nr][nc])

def move(num):
    """
    :param num: 현재 움직일 말 번호
    :return: 4이상 쌓이는 순간 True 반환, 잘 진행되면 False 반환
    """

    # [1] 정보 가져오기
    cr, cc = pos[num]
    cd = dirs[num]

    # [2] 이동하려는 칸 확인
    dr, dc = ds[cd]
    nr, nc = cr+dr, cc+dc
    length = 0
    if oob(nr, nc) or m[nr][nc] == 2:       # 벽이거나 파란 칸
        cd = rev[cd]    # 역방향으로 바꿈
        dirs[num] = cd  # dirs에도 반영
        dr, dc = ds[cd]
        tr, tc = cr+dr, cc+dc
        if oob(tr, tc) or m[tr][tc] == 2: # 반대방향으로 한칸 이동한 것도 벽이거나 2라면
            pass    # 이동하지 않고 가만히 있는다. (방향은 위에서 바꿨음)
        elif m[tr][tc] == 0:
            length = move_white(num, cr, cc, tr, tc)
        elif m[tr][tc] == 1:
            length = move_red(num, cr, cc, tr, tc)

    elif m[nr][nc] == 0:
        length = move_white(num, cr, cc, nr, nc)
    elif m[nr][nc] == 1:
        length = move_red(num, cr, cc, nr, nc)

    if length >= 4:
        return True
    return False

def solve():
    turn = 1
    while turn <= 1000: # 첫 루프 첫번째 턴, 1001번째 턴 되는 순간 종료 (마지막에 turn 더해줌)
        # [1] 순서대로 움직이기
        for num in range(1, K+1):

            res = move(num)
            # print(turn, num)
            # for i in u:
            #     print(i)
            # print(pos)
            # print(dirs)
            # print()
            if res:
                return turn

        # [2] 턴 수 증가
        turn += 1

    return -1   # 1001번째 되면 -1 반환

print(solve())

"""
조건 분기 : 문제에 나오는 그대로 하기

[이해]
N*N (흰, 빨, 피로 칠해져 있음)
말의 개수 K
하나의 말 위에 다른 말을 올릴 수 있음
상하좌우 한칸 이동 (각 말마다 미리 정해져 있음)

턴한번 :
    1번말부터 K번말 "순서대로" 이동
    한 말이 이동하면 "위!!에 올려져 있는" 말도 이동

    A말의 "이동 하려는 칸"이
        흰색 0:
            A말 위 모든 말과 같이
            그 칸의 맨 위로 이동
        빨강 1:
            A말과 모든 말이 같이 뒤집힌 순서로
            그 칸의 맨 위로 이동 (!!! "이동 하려는 칸"의 말들은 그대로)
        파랑 2 or 벽 oob:
            A번말의 이동방향을 반대로 하고 (다른 말은 그대로)
            반대로 바꾼 후 이동하려는 칸도 파랑이라면
                가만히 있음
            아니라면
                한칸 이동

말이 4개 이상 쌓이는 순간 : 게임 종료
값이 1000보다 크거나 종료되지 않는 경우는 -1 출력

[구상]
행열방향 전부 -1해서 받기 (우좌상하)
입력에서는 처음부터 같은것 두개 X
턴 1번부터 시작

solve
    move : 움직임의 결과도 네개 이상이 되었는지 아닌지 반환
        움직일 때 위의 말들도 같이 움직이므로 같이 pos를 수정해야함
"""


