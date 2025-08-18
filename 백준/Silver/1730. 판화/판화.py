"""
수직으로 지나면 | 수평으로지나면 - 수직 수평으로 지나면 +
00부터시작

crcc와 nrnc 모두 그려줘야함
"""

def oob(r, c):
    return not (0<=r<N and 0<=c<N)  #(D) <=N로 적어서 틀림

N = int(input())
OPS = list(input())
ARR = [["." for _ in range(N)] for _ in range(N)]   

DS = {"D":(1,0), "U":(-1,0), "L":(0,-1), "R":(0,1)}

cr, cc = 0, 0
for op in OPS:
    dr, dc = DS[op]
    nr, nc = cr+dr, cc+dc
    if oob(nr, nc):
        continue
    if op in ["D", "U"]:
        if ARR[cr][cc] in ["-", "+"]:
            ARR[cr][cc] = "+"
        else:
            ARR[cr][cc] = "|"

        if ARR[nr][nc] in ["-", "+"]:
            ARR[nr][nc] = "+"
        else:
            ARR[nr][nc] = "|"
    if op in ["L", "R"]:
        if ARR[cr][cc] in ["|", "+"]:
            ARR[cr][cc] = "+"
        else:
            ARR[cr][cc] = "-"

        if ARR[nr][nc] in ["|", "+"]:
            ARR[nr][nc] = "+"
        else:
            ARR[nr][nc] = "-"
    cr, cc = nr, nc
    # print(op)
    # for l in ARR:
    #     print(*l)
    # print()

for l in ARR:
    print("".join(l))   # 출력시 공백 없어야하는데 print(*l)하여 틀림


