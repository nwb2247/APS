"""
조건을 하나라도 빼먹으면 안됨,
    => 하나가 성립하면 반드시 이것도 만족된다 -> 엄밀하게 확인하기 어렵다면 무조건 나와 있는 그대로 처리해주자

print 했을 때 눈에 잘 보이는 방식으로 찍고, 꼼꼼히 보자...
    - rjust 이용
    - 숫자가 한번에 안보이면 문자나 특수기호로 바꿔서 보기...
"""

"""
선거구
    한 구역 이상 포함
    모든 구역 연결
    중간에 통하는 인접한 같은 선거구에 속하는 구역이 0개 이상
    
기준점, d1, d2 조건 확인 (부등호)
"""
from collections import deque

# -------------- 입력, 전처리 --------------

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())  # N*N
population = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in
                                range(N)]  # 조건이 다 1,1시작 기준으로 나와있으므로 헷갈리지 않게 패딩하자 (인구는 1이상이므로 0으로 패딩)


# ------------------ 함수 --------------------

def oob(r, c):
    return not (1 <= r <= N and 1 <= c <= N)


# def dprint(m):
#     rep = [")", "!", "@", "#", "$", "5"]
#     for l in m:
#         print(*map(lambda x: rep[x].rjust(3), l))

def cond1(r, c, x, y, d1, d2):
    return 1 <= r < x + d1 and 1 <= c <= y

def cond2(r, c, x, y, d1, d2):
    return 1 <= r <= x + d2 and y < c <= N

def cond3(r, c, x, y, d1, d2):
    return x + d1 <= r <= N and 1 <= c < y - d1 + d2

def cond4(r, c, x, y, d1, d2):
    return x + d2 < r <= N and y - d1 + d2 <= c <= N


def bfs(num, m, start, check, x, y, d1, d2):
    sr, sc = start
    v = [[0] * (N + 1) for _ in range(N + 1)]
    q = deque()
    v[sr][sc] = 1
    q.append((sr, sc))
    while q:
        cr, cc = q.popleft()
        m[cr][cc] = num

        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if not check(nr, nc, x, y, d1, d2):
                continue
            if m[nr][nc] != 0:
                continue
            if v[nr][nc] != 0:
                continue
            # 경계 내에 있고, 부등호 조건 만족하고(check), 방문하지 않았다면
            # ("1번 오른쪽 위" 조건은 시작점에 의해 보장, 부등호 조건 만족한다면 5번 구역 넘어가지 못함)
            v[nr][nc] = 1
            q.append((nr, nc))


def make_groups(x, y, d1, d2):
    """
    선거구 획정하고 유효한 선거구 획정이라면 ans를 갱신
    """
    global ans
    m = [[0] * (N + 1) for _ in range(N + 1)]

    # [1] 경계선 그리기
    cr, cc = x, y  # 1번
    for l in range(d1 + 1):  # x+d1, y-d1까지 그어야함 즉 (d1 포함)
        m[cr + l][cc - l] = 5

    cr, cc = x, y  # 2번
    for l in range(d2 + 1):
        m[cr + l][cc + l] = 5

    cr, cc = x + d1, y - d1  # 3번
    for l in range(d2 + 1):
        m[cr + l][cc + l] = 5

    cr, cc = x + d2, y + d2  # 4번
    for l in range(d1 + 1):
        m[cr + l][cc - l] = 5

    # [2] 경계선 내부를 5로 채우기
    for cr in range(x + 1, x + d1 + d2):  # (x와 x+d1+d2는 한점이므로 포함하면 안됨, d1, d2 1보다 크므로 1 더해도 OK)
        f = False  # False로 시작해서 첫 5만나면 True, 두번째 5만나면 False로 바꿔줌
        for cc in range(y - d1, y + d2 + 1):  # 각각 왼쪽 꼭지점, 오른쪽 꼭지점의 열좌표
            if m[cr][cc] == 5:
                f = not f
            if f:
                m[cr][cc] = 5

    # [3] 1, 2, 3, 4 채우기
    # (D) 1번 선거구, 1<r<x+d1 and 1<c<y and 경계선의 왼쪽 위
    #   => 5가 아니고 부등호조건을 만족한다고 해서 "경계선 왼쪽 위를 만족하는 것이 아님
    #   (5번이 길쭉한 우하향 모양인 경우, 오른쪽 위에도 그려짐,,,)
    # 선거구는 모두 연결되어있어야하므로 안전하게 bfs를 쓰자

    # 1, 2, 3, 4번 선거구 획정
    starts = [None, (1, 1), (1, N), (N, 1), (N, N)]  # 1번 : 왼쪽 위에 있도록 하기 위해 1, 1부터 시작
    checks = [None, cond1, cond2, cond3, cond4]  # 부등호 조건
    for num in range(1, 4 + 1):
        bfs(num, m, starts[num], checks[num], x, y, d1, d2)

    sm = [None, 0, 0, 0, 0, 0]
    for cr in range(1, N + 1):
        for cc in range(1, N + 1):
            sm[m[cr][cc]] += population[cr][cc]

    # 선거구 획정 유효성
    if 0 in sm:  # 구역이 0개인 선거구가 있다면 X(0개라면 인구 더해지지 않아서 0임 (각 구역 인구는 1이상)
        return
    for lst in m[1:]:  # 선거구 배정 안받은 구역이 있다면 X
        if 0 in lst[1:]:
            return

    ans = min(ans, max(sm[1:]) - min(sm[1:]))

    return


def solve():
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for d1 in range(1, N + 1):  # d1, d2도 아래 조건에 의해 N보다 큰 경우는 볼 필요가 없음
                for d2 in range(1, N + 1):
                    if not (1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N):
                        continue
                    make_groups(x, y, d1, d2)
    return


# ------------------ 실행 -------------------
ans = N * N * 101
solve()
print(ans)

# dprint(make_groups(2, 4, 2, 2))
# print()
# dprint(make_groups(1, 2, 1, 5))
# print()
# dprint(make_groups(1, 9, 8, 1)) # N = 10
