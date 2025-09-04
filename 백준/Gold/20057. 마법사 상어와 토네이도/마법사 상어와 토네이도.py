"""
sr, sc nr, nc, cr, cc 등 쓰는거는 함수화
전처리 등에는 zr,zc 사용

엣지 :
3 (마지막)
100 0 0
0 0 0
0 0 0
-----
90

3
0 0 0
0 100 0
0 0 0
------
가운데에만 있는 경우는 흩날릴 일이 없음

"""

ds = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 좌하우상

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0 # 밖으로 나간 것들

# 흩날림 양 전처리
ms = []
apos = []   # 알파 위치

# 좌이동 기준
m0 = [(-2, 0, 2),
     (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
     (0, -2, 5),
     (1, -1, 10), (1, 0, 7), (1, 1, 1),
     (2, 0, 2)]
apos0 = (0, -1)
ms.append(m0)
apos.append(apos0)

# 나머지 방향으로도 만들어줌
for _ in range(3):

    ml = ms[-1]
    nm = []
    for zr, zc, zm in ml:
        nm.append((-zc, zr, zm))
    ms.append(nm)

    zr, zc = apos[-1]
    apos.append((-zc, zr))

# for i in range(4):
#     print(apos[i])
#     print(ms[i])

def spread(sr, sc, cd):
    global ans

    val = arr[sr][sc]
    a = val - ((val*2//100)*2 + (val*10//100)*2 + (val*7//100)*2 + (val*1//100)*2 + (val*5//100))
    # print([apos[cd] + (a, )] + ms[cd])
    for dr, dc, dm in ms[cd]: # 알파 외에
        nr, nc = sr+dr, sc+dc
        if oob(nr, nc):
            ans += (val*dm//100)      # (D) 사실 원래 있던 것합 - 마지막 있던 것들 합 으로 해도 될듯...
            continue
        arr[nr][nc] += (val*dm//100)
    # 알파 (a를 구했으므로 //해주면 안됨)
    dr, dc = apos[cd]
    nr, nc = sr+dr, sc+dc
    if oob(nr, nc):
        ans += a
    else:
        arr[nr][nc] += a
    
    # 비워줌
    arr[sr][sc] = 0


# [1] 토데이도 이동
def solve():
    cr, cc, cd = N // 2, N // 2, 0  # 가운데, 좌방향이동부터 시작
    length = 1
    cnt = 0
    while True:  # 0 , 0 의 왼쪽에서 끝남 항상
        dr, dc = ds[cd]
        nr, nc = cr + dr, cc + dc
        # 여기서 처리
        spread(nr, nc, cd) # 도착한 좌표랑 당시의 방향

        # print(nr, nc, cd)
        # for l in arr:
        #     print(l)
        # print(ans)
        # print()

        # 종료
        if (nr, nc) == (0, 0):
            break
        cr, cc = nr, nc
        cnt += 1
        if cnt == length:       # 가야하는 만큼 왔으면 회전
            cd = (cd + 1) % 4
            cnt = 0
            if cd % 2 == 0:     # 좌, 우 방향이면 하나씩 길이 늘려줌
                length += 1

solve()
print(ans)