"""
[이해]
파란색 칸에서 이동 시작하면 파란색 화살표를 타야함
이동하는 도중이거나, 파란색이 아닌 칸에서 이동시작하면 빨간색

말이 도착칸에 닿는다면 주사위에 나온수와 관계없이 이동을 마침

말 4개
10턴으로 진행
매번마다 1~5만큼 이동,
도착칸에 있지 않은 말만 움직일 수 있음
이동 마치는 칸에 다른 말이 있는 경우에도 그 말을 고를 수 없음(단, 이동을 마치는 칸이 도착칸이면 고를 수 있음)
도착한 칸의 수가 점수로 추가

[백트래킹]
4**10?
info = 위치, (이미 도착했다면 100) [0]*4
시작은 0으로 하자, 도착은 100로 하자
info 인자로 넘기자
score도 마찬가지

내부는 음수
외부는 양수로 표시
점수는 절대값

파란색이면 -1로가고 (0 or 2칸이면 1)
빨간색이면 0으로 감  (항상 0)
"""
from collections import defaultdict

dice = list(map(int, input().split()))
nxt = defaultdict(list)
for i in range(0, 40, 2):
    nxt[i].append(i+2) # 번호, 점수
nxt[10].append(-13)
nxt[-13].append(-16)
nxt[-16].append(-19)
nxt[-19].append(-25)
nxt[20].append(-22)
nxt[-22].append(-24)
nxt[-24].append(-25)
nxt[30].append(-28)
nxt[-28].append(-27)
nxt[-27].append(-26)
nxt[-26].append(-25)
nxt[-25].append(-30)
nxt[-30].append(-35)
nxt[-35].append(40)
nxt[40].append(100)
blue = {10, 20, 30}

def find_dest(start, l):
    if start in blue:
        cur = start
        for _ in range(l):
            cur = nxt[cur][-1]
            if cur == 100:
                return cur
    else:
        cur = start
        for _ in range(l):
            cur = nxt[cur][0]
            if cur == 100:
                return cur
    return cur

def backtrack(depth, score):
# def backtrack(depth, score, lst):
    """
    :param depth: 몇번째 주사위까지 굴릴 차례인지 (0번째부터 시작 9번째까지 굴림)
    :param score : 점수
    :return:
    """
    global ans
    if depth == 10 or sum(pos) == 100*4: # 10개 다 던졌거나, 모든 말이 도착지에 왔다면 종료
        ans = max(ans, score)
        return

    for i in range(4):  # 굴릴 말 선택
        if pos[i] == 100:     # 목적지에 있는 말은 이동 불가
            continue
        dest = find_dest(pos[i], dice[depth])
        if dest != 100 and dest in pos:     # 도착지에 다른 말이 있는 경우도 이동 불가
            continue
        tmp = pos[i]
        pos[i] = dest
        if dest == 100:
            backtrack(depth + 1, score) # 목적지가 도착지면 점수 없으므로 더하면 안됨
            # backtrack(depth + 1, score, lst + [(i, 0)])
        else:
            backtrack(depth + 1, score + abs(dest))
            # backtrack(depth + 1, score + abs(dest), lst + [(i, dest)])
        pos[i] = tmp    #원 복

ans = 0
pos = [0]*4
backtrack(0, 0)
# backtrack(0, 0, [])
print(ans)



