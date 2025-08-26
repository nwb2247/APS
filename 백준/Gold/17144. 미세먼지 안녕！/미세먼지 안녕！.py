"""
[요약평]
1. 배열 돌리기 같은 문제 연습,, (회전용 배열 만드는 전처리가 너무 오래걸림)
 => 돌리기 문제는 종이에 한번 그려보자 (돌리기 + 처리 로직 둘다)
2. 중간에 구상의 변화가 생겼을때 어떻게 다른 로직을 같이 잘 수정할 수 있을지 고민

[타임라인]
이해 및 구상 : 9분
구현 및 디버깅 : 37분 (20분 이상을 돌리기에서 사용...)

[이해 및 구상]
-) 회전용 좌표 리스트를 출력으로만 보려다보니 확신이 안서서 오래 들여다봄
    종이에 그려보는게 단축에 더 좋았을 듯
+) 회전용 좌표 리스트를 만드는 아이디어 자체는 좋았음

[구현]
-) 구상했던 구현 방식에 수정이 생기면서 수정할 것은 없는지 확인하느라 시간이 오래걸림
-) new_top.reverse()이게 굳이 필요했나 싶음 (어차피 new_top, top 둘다 만들건데)
+) 방향 배열 하나 만들어서 위아래 같이 사용하기 위해 [0, 1, 2, 3] [0, 3, 2, 1]로 사용
+) top = new_top[1:] + [new_top[0]] 로 빠르게 작성 (for문대신)

[디버깅]
-) 에러 떴다면 몇번째 라인에서 뜬건지를 확인하자...
    cr, cc = bottom[i]              # (D) top
    여기서도 시간 한참 사용
+) 문제 특성상 arr을 출력하면 쉽게 디버깅은 가능했음

[시간 복잡도]
N**2*T = 2500000

안퍼지는 조건을 좀더 신경썼으면 좋았을 듯
if arr[cr][cc] == 0:         # (D) <5로하면 빠를듯
    continue


-----
총 46분

"""

"""
구상 과정
확산 규칙 이해
공기청정기는 움직이지 않음
청정기 위치 m으로 받아오자
회전은 회전이 이뤄지는 좌표들로 관리 (계속사용되므로)
(마지막에 공기청정기 위치 더해주면 안됨)
    => 0으로 바꾸는 것으로 수정했음

50*50*1000 가능할듯
"""

def oob(r, c):
    return not (0<=r<R and 0<=c<C) # (D) c를 R로 씀 (빠르게 찾음)

def spread():
    plus = [[0]*C for _ in range(R)]
    for cr in range(R):
        for cc in range(C):
            if arr[cr][cc] < 5: # 시간 비교용 제출
            # if arr[cr][cc] == 0:         # (D) <5로하면 빠를듯
                continue
            a = arr[cr][cc] // 5
            for dr, dc in ds:
                nr, nc =  cr+dr, cc+dc
                if oob(nr, nc) or ((nr, nc) in [(m[0], 0), (m[1], 0)]):
                    continue
                arr[cr][cc] -= a
                plus[nr][nc] += a
    for cr in range(R):
        for cc in range(C):
            arr[cr][cc] += plus[cr][cc]

def rotate():
    for i in range(len(new_top)):
        nr, nc = new_top[i]
        cr, cc = top[i]
        arr[nr][nc] = arr[cr][cc]

    arr[m[0]][0] = 0
    arr[m[0]][1] = 0                    # (D) 새바람도 0
    for i in range(len(new_bottom)):
        nr, nc = new_bottom[i]
        cr, cc = bottom[i]              # (D) top
        arr[nr][nc] = arr[cr][cc]
    arr[m[1]][0] = 0
    arr[m[1]][1] = 0                    # (D) 새바람도 0


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# ---------- 전처리 -----------
m = []  # 청정기 좌표
for zr in range(R):
    if arr[zr][0] == -1:
        m.append(zr)
        arr[zr][0] = 0

ds = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 동북서남

new_top = []
cr, cc = m[0], 0
for zd in [0, 1, 2, 3]:
    while True:
        dr, dc = ds[zd]
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc) or nr>m[0]:
            break
        new_top.append((nr, nc))
        cr, cc = nr, nc
new_top.reverse()
top = new_top[1:] + [new_top[0]]

new_bottom = []
cr, cc = m[1], 0
for zd in [0, 3, 2, 1]:
    while True:
        dr, dc = ds[zd]
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc) or nr<m[1]:
            break
        new_bottom.append((nr, nc))
        cr, cc = nr, nc

new_bottom.reverse()
bottom = new_bottom[1:] + [new_bottom[0]]

for i in range(T):
    spread()
    rotate()
    # for l in arr:
    #     print(l)
    # print()

print(sum(map(sum, arr)))