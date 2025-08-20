"""
상하좌우에서 하나 선물 잡아 포장 가능
벨트위에 더 오래 올려져 있던 선물을 집어다가 포장 (즉, 다음 선물이 지나갈 수 잇음)
포장되지 않은 선물은 폐기됨

(모서리 직원은 인접 두개 이므로 주의)

B = 100 100*100
M 선물 개수 100 이므로 1초씩 늘리면서하자..

폐기 되는 선물 개수 세서 M에서 빼주자
폐기 -> 끝지점이 지나면!! 폐기

선물도 1초에 한번씩 올라옴
"""
def oob(r, c):
    return not (0 <= r < B and 0 <= c < B)

# ---------------------- 전처리 --------------------------
DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 선물 방향 : 우하좌 -> 폐기
B, N, M = map(int, input().split())
ARR = [[0]*B for _ in range(B)]

path = []
cr, cc, cd = 0, 0, 0
path.append((cr, cc))
while cd<3:     # 상 방향은 안씀
    dr, dc = DS[cd]
    nr, nc = cr+dr, cc+dc
    if oob(nr, nc):
        cd += 1
        continue
    cr, cc = nr, nc
    path.append((cr, cc))

path_rev = path[::-1]
# print(path_rev[1:])

workers = [[] for _ in range(N)]
for i in range(N):
    wr, wc, t = map(int, input().split())
    workers[i] = [wr, wc, t, 0] # 0 포장 가능상태, 0초과 포장중상태
    # ARR[wr][wc] = str(0)

# ---------------------- 시작 --------------------------

sec = 0
discard = 0
success = 0
present_num = M

while sec <= (M + B*3): # sec < M + B*3 - 1 가 맞을거 같긴한데, 넉넉하게 잡아도 상관없을듯
    sec += 1
    
    # [1] 선물 한칸씩 이동 (이동 추가)

    for i in range(1, len(path_rev)): # enumerate 함부로 쓰면 2개씩 뜀;
        cr, cc = path_rev[i]
        if ARR[cr][cc] != 0:
            nr, nc = path_rev[i-1]
            ARR[nr][nc] = ARR[cr][cc]
            ARR[cr][cc] = 0

    if present_num > 0:           # 주의 M 직접 줄이면 sec <= (M + B*3)에서 사고남
        nr, nc = path_rev[-1]
        ARR[nr][nc] = sec
        present_num -= 1
        
    # [2] 선물 처리
    for i in range(N-1, -1, -1):
        wr, wc, t, state = workers[i]
        if state > 0:       # 포장 중이라면
            workers[i][3] -= 1 # state 감소
            # ARR[wr][wc] = str(workers[i][3])

        if workers[i][3] == 0:                  
            # (D) else로 하면 큰일남 그림 5초에서 포장 끝난 상태면 바로 다음 선물 집어야댐
            # (D) 늦게온 선물 부터 집어야함 선물에 sec을 넣자
            gr, gc, gsec = -1, -1, (M + B*3) + 10000    # 집을 선물 좌표, 초
            for dr, dc in DS:
                nr, nc = wr+dr, wc+dc
                if oob(nr, nc): continue
                if ARR[nr][nc] > 0 and ARR[nr][nc] < gsec: # (D) oob 처리 해야함
                    gsec = ARR[nr][nc]
                    gr, gc = nr, nc

            if (gr, gc) != (-1, -1):
                ARR[gr][gc] = 0
                workers[i][3] = t
                # ARR[wr][wc] = str(workers[i][3])
                success += 1

    # [3] 폐기
    # print(ARR[path_rev[0][0]][path_rev[0][1]])
    if ARR[path_rev[0][0]][path_rev[0][1]] > 0: # 폐기 # (D) 1로잡음
        discard += 1
        ARR[path_rev[0][0]][path_rev[0][1]] = 0 # 폐기 처리 필수

    # print(sec)
    # for l in ARR:
    #     print(l)
    # print(discard)
    # print(workers)
    # print()

print(M-discard)