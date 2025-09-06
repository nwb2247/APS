"""
4*4
물고기는 번호와 방향
한칸에는 한마리씩 존재
1~16
상하좌우 대각선

상어방향은 0,0 물고기를 먹고 0,0에 들어감 방향과 같아짐
그 이후 물고기 이동

물고기는 작은 순서대로 이동
    물고기는 한칸이동
    이동 가능 : 빈칸, 다른 물고기
    불가능 : 경계,  상어 있는 곳
    (이동 가능칸을 향할때까지 45도반시계 회전)
    이동할칸 없으면 이동하지 않음 (8방향 다보고도)
    for brealk

    물고기가 다른 물고기가 있는 곳으로 갈땐 서로의 위치를 바꿈

그 다음 상어 이동
    한번에 여러개의 칸을 이동가능 (그 방향으로 쭉 선택가능)
    물고기 있는 칸으로 이동했다면
        물고기 먹으면 그 물고기의 방향을 가짐
        이동중에 지나치는 물고기 먹지 않음
    물고기가 없는 칸으로 이동했다면
        방향 유지
    이동할 수 있는 칸이 없다면 종료

위 과정을 반복
"""
ds = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}

M = [[0] * 4 for _ in range(4)]

FINFO = [None] + [()] * 16
for ZR in range(4):
    inp = list(map(int, input().split()))
    for ZC in range(4):
        NUM, D = inp[2 * ZC], inp[2 * ZC + 1]
        M[ZR][ZC] = NUM
        FINFO[NUM] = (ZR, ZC, D)  # 0 1위치, 2 방향

# SR, SC = 0, 0
# 상어의 번호는 -1으로 표시..
# 빈칸은 0으로 표시
SR, SC = 0, 0
first = M[SR][SC]
SD = FINFO[first][2]
M[SR][SC] = -1
FINFO[first] = None


def oob(r, c):
    return not (0 <= r < 4 and 0 <= c < 4)


def fish(m, finfo):
    nm = [lst[:] for lst in m]
    nfinfo = finfo[:]

    for num in range(1, 16 + 1):  # (I) 16
        if nfinfo[num] is None:  # 죽었으면
            continue

        cr, cc, cd = nfinfo[num]
        for nd in list(range(cd, 9)) + list(range(1, cd)):
            dr, dc = ds[nd]
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or nm[nr][nc] == -1:
                continue  # 이동 못하면 반시계 45도 회전
            else:
                break
        else:  # 이동 가능 칸이 없다면 아무것도 안함
            continue
        # [이동]
        if nm[nr][nc] == 0:
            nm[nr][nc] = num

            nfinfo[num] = (nr, nc, nd)
            nm[cr][cc] = 0
        elif 1 <= nm[nr][nc] <= 16:  # 물고기 칸
            other = nm[nr][nc]
            nfinfo[other] = (cr, cc, nfinfo[other][2])
            nfinfo[num] = (nr, nc, nd)
            nm[nr][nc], nm[cr][cc] = num, other

    return nm, nfinfo

def shark(sr, sc, sd, m, finfo): # (D) 물고기가 없는 칸은 이동못함
    dr, dc = ds[sd]
    tmp = []
    nr, nc = sr + dr, sc + dc
    while not oob(nr, nc):
        if m[nr][nc] != 0:
            tmp.append((nr, nc))
        nr += dr
        nc += dc
    return tmp


def backtrack(score, m, finfo, sr, sc, sd):
    global ans

    nm, nfinfo = fish(m, finfo)

    lst = shark(sr, sc, sd, nm, nfinfo)

    if len(lst) == 0:
        ans = max(ans, score)
        return

    for nsr, nsc in lst:
        if nm[nsr][nsc] == 0:  # 빈칸이라면
            nm[nsr][nsc], nm[sr][sc] = -1, 0
            backtrack(score, nm, nfinfo, nsr, nsc, sd)
            nm[nsr][nsc], nm[sr][sc] = 0, -1  # 원복
        else:  # 물고기가 있다면
            num = nm[nsr][nsc]
            num_info = nfinfo[num]

            nm[nsr][nsc], nm[sr][sc] = -1, 0
            nfinfo[num] = None

            backtrack(score + num, nm, nfinfo, nsr, nsc, num_info[2])

            nm[nsr][nsc], nm[sr][sc] = num, -1  # 원복
            nfinfo[num] = num_info


ans = first
backtrack(first, M, FINFO, SR, SC, SD)
print(ans)
