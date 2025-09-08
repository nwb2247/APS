"""
[반드시 다시 풀기]

[요약평]
중력은 무조건 스택 쓰자... 다른 방법은 머리아프다... (시간복잡도도 다르지 않음)
엣지는 코드 창 내리고 생각하기

[타임라인]
이해 및 구상 26분
구현 47분
디버깅 42분
----------------------
총 115분

[구현]
-) 중력을 원래 방식 (for으로 올라가면서 빈칸 있는지 확인하고 그때마다 내리기)으로 구현하면 끝까지 안내려오는 경우가 생김
+) 내리는 로직은 꽉찬건, 연한색 지우고 마지막에 하는게 아니라, 지울때마다 해줘야하는 것을 문제에서 캐치

[디버깅]
-) 엣지케이스 만들기 충분히 하고 제출해야함
-) 문제 찾았지만 급한 마음에 제대로 해결하지 못하고 재제출, 심지어 오픈테케에서 틀림
    수정한 부분의 로직 철저히 검증하자
+) 문제 - 이해 - 구상 - 구현 순으로 잘못된 부분 있는지부터 확인하고 그 다음에 엣지케이스를 확인하려 했음

[엣지케이스]
7
2 2 2
2 2 2
2 2 2
2 2 2
3 1 1
3 1 1
3 0 0
---------
2
13
(한번에 두행 삭제)
"""

"""
xy->rc와 동일 x행y열
빨파초

빨강에서 선택하면 초록, 파랑으로 이동하는데, 다른 블록을 만나거나, 경계를 만날때까지 이어짐

초록색 어떤 행이 가득차면  제거되고 위에 있던 블록이 사라진 행의 수만큼 이동
파란색 어떤 열이 가득차면 제거되고 왼쪽에 있던 블록이 사라진 열의 수만큼 이동
사라진 행 또는 사라진 열의 수만큼 점수를 얻음 (행 , 열 당 1점)

연한색 칸
연한 초록(01)에는 블록이 있으면
블록이 있는 행의 수만큼 아래 행 타일이, 사라짐 사라진 행 수만큼 이동
연한 파랑(01)도
블록이 있는 열의 수만큼 오른쪽열의 타일이 사라짐, 사라진 열 수 만큼 이동
    => 이때는 점수를 안얻음....?

(주의!)
행이나 열로 가득찬 경우 + 연한칸 색 이 모두 발생하면
=> 행열 가득찬 경우 없을때 까지 모두 진행 => 그다음 연한칸 블록을 처리해야함

블록은 보드에 넣인 이후 다른 블록과 합쳐지지 않는다,,,,?

출력 : 얻은 점수 + 초록 보드, 파란 보드에 타일이 있는 칸의 개수 세기 (어차피 연한 블록에는 블록이 안남음)

10000번 이동에 추가 시간 없음, 보드 크기 작으니까 OK

[구상]
1*1 1*2 2*1

헷갈리니까 초록도 세로로 세우고, 파랑도 초록처럼 세로로 세우자
이때 빨강에서 놓는 것이 파랑은 행<->열 바꿔서 넣어야함
파랑을 출력시에 열 뒤집어서..

2짜리 블록은 한칸씩 처리하면안되고, 두개가 한번에 움직여야함. (가로로 떨어가는 경우)
"""
K = int(input())
ops = [tuple(map(int, input().split())) for _ in range(K)]
R, C = 6, 4
green = [[0 for _ in range(C)] for _ in range(R)]
blue = [[0 for _ in range(C)] for _ in range(R)]


# -------------- 함수 ----------------
def dprint_green():
    print("green")
    for l in green:
        print(*l)
    print()


def dprint_blue():
    print("blue")
    for l in blue:
        print(*l[::-1])
    print()


def oob(r):
    return not (0 <= r < R)


def put(arr, t, c):  # 주의 위에서 떨어지면서 바닥을 만날때까지 확인해야함 (아래부터 확인하면 사고) + 직전에다가 쌓아줌 r-1
    if t == 1:  # 1*1
        for r in range(R + 1):  # 바닥 처리를 위해 R+1
            if oob(r) or arr[r][c] == 1:
                arr[r - 1][c] = 1
                return
    elif t == 2:  # 1*2 (가로)
        for r in range(R + 1):
            if oob(r) or arr[r][c] == 1 or arr[r][c + 1] == 1:  # 다 or로 처리
                arr[r - 1][c] = 1
                arr[r - 1][c + 1] = 1
                return
    elif t == 3:  # 2*1 (세로)
        for r in range(R + 1):
            if oob(r) or arr[r][c] == 1:
                arr[r - 1][c] = 1
                arr[r - 2][c] = 1
                return


def full(arr):
    global score

    # [1] 꽉찬 행 먼저 삭제 (D) 꽉 찬 행 2개인 경우 처리 못해줌 (먼저 다 지워주고 지워진 만큼 이동해야함)
    cnt = 0
    for cr in range(R - 1, -1, -1):  # 아래부터 꽉찬 줄 있는지 확인하고 있다면 비워줌
        if arr[cr] == [1, 1, 1, 1]:
            arr[cr] = [0, 0, 0, 0]
            cnt += 1
            score += 1

    tmp = []
    for cr in range(R):
        if arr[cr] != [0, 0, 0, 0]:
            tmp.append(arr[cr])
    for cr in range(R-1, -1, -1):
        if tmp:
            arr[cr] = tmp.pop()
        else:
            arr[cr] = [0, 0, 0, 0]
    return


def light(arr):
    # [2] 연한 색 처리
    cnt = 0
    for lst in arr[:2]:  # 0, 1행 확인
        if 1 in lst:
            cnt += 1
    for i in range(1, cnt + 1):
        arr[-i] = [0, 0, 0, 0]

    tmp = []
    for cr in range(R):
        if arr[cr] != [0, 0, 0, 0]:
            tmp.append(arr[cr])
    for cr in range(R-1, -1, -1):
        if tmp:
            arr[cr] = tmp.pop()
        else:
            arr[cr] = [0, 0, 0, 0]

    return


def solve():  # 주의 : 중력 처리는  full, light 각각에서 미리 해줘야함 (문제 설명)
    for k in range(K):
        t, x, y = ops[k]
        if t == 1:
            put(green, 1, y)
            put(blue, 1, x)
        if t == 2: # 초록 기준 가로 2칸
            put(green, 2, y)
            put(blue, 3, x)
        if t == 3: # 초록 기준 세로 2칸
            put(green, 3, y)
            put(blue, 2, x)

        full(green)
        full(blue)
        light(green)
        light(blue)
        #
        # print("turn", k)
        # dprint_green()
        # dprint_blue()


# ----------- 실행 -----------

score = 0
solve()
print(score)
print(sum(map(lambda x: sum(green[x]) + sum(blue[x]), range(R))))
