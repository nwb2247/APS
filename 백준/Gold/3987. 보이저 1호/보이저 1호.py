"""
주의할 실수 : visited 초기화 위치 => 방향마다 필요;;

블랙홀 C
빈칸 .
행성 \/       => 어떤 모양을 어느방향에서 만나는지에 따라 다음 방향 달라짐
PR, PC로 주어짐 초기위치
가장 오랜 시간 머무는 방향과 시간
여러개라면 URDL 순서 중에 앞서는 것
무한하다면 Voyager

리팩토링 : 어차피 방향 4개인데 set 쓸필요 없음

"""
N, M = map(int, input().split())
ARR = [list(input()) for _ in range(N)]
sr, sc = map(int, input().split())

DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # URDL
to_char = ["U", "R", "D", "L"]
ND = {"/": {0: 1, 1: 0, 2: 3, 3: 2}, "\\": {0: 3, 3: 0, 1: 2, 2: 1}}


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)

# visited = [[set() for _ in range(M)] for _ in range(N)] 여기서 초기화하면 안됨;;;;;;;;;;;;

ans = 0  # 무한 -1 voyager
ans_d = ""
for sd in range(4):
    cr, cc, cd = sr - 1, sc - 1, sd  # 그림 상 좌표를 1, 1부터 시작하게 주고 있음
    visited = [[[0]*4 for _ in range(M)] for _ in range(N)] # (D) visited 초기화 위치 생각하자 제발
    visited[cr][cc][cd] = 1
    sec = 0
    while True:  # 나가거나, 왔던 위치에 동일한 방향이면 종료
        # print(cr, cc, cd)
        sec += 1
        dr, dc = DS[cd]
        nr, nc = cr + dr, cc + dc
        if oob(nr, nc) or ARR[nr][nc] == "C":
            if ans != -1 and sec > ans:  # 벽밖으로 나가면 sec으로 갱신하고 루프 종료
                ans = sec
                ans_d = to_char[sd]  # cd 아님 주의
            break
        if ARR[nr][nc] in ["/", "\\"]:
            cd = ND[ARR[nr][nc]][cd]
        cr, cc = nr, nc
        if visited[cr][cc][cd] == 1:  # 해당위치에 같은 방향으로 다시 왔다면 무한으로 voyager
            ans = -1
            ans_d = to_char[sd]
            break
        visited[cr][cc][cd] = 1

    if ans == -1:  # 무한이면 나머지는 볼 필요도 없음
        break

if ans == -1:
    print(ans_d)
    print("Voyager")
else:
    print(ans_d)
    print(ans)
