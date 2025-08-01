"""
[조건]
N, M <= 100
입력에서 가장자리에 치즈가 있는 경우는 없다

[목표]
치즈가 모두 없어지는 시간 구하기

[접근]
매번 arr 전체를 도는 대신에 큐를 돌면서
없어질 좌표를 다른 큐에 넣어두고 arr에 반영해준다.
유지할 큐도 남겨둔다.
-> 찾는 동시에 없애면, 지금 없어지면 안되는 치즈도 없어지기 때문
이후 그 큐를 다음 시간에 사용한다.

[주의]
1. 큐에서 뺄 때 arr에도 바로 반영하면
지금 없어지면 안되는 치즈도 없어지기 때문에 따로 관리
2. 벽에 붙어있는 경우 -> 공기와 접촉한 것이 아니므로 카운트 X
따라서 치즈를 세지 말고 공기(0)을 세자
!!! 3. 치즈에 둘러싸인 공기는 외부공기 X
그런데 내부공기를 체크하는 것보다 외부공기를 체크하는 것이 더 쉽다 BFS (입력에서 가장자리에 치즈가 있는 경우는 없다 했으므로,,)
-> -1 등으로 채워두고 check()실행, 큐 완료한 뒤엔 -1을 다시 0으로 바꿔줌

[생각해본 edge case]
2 2
1 1
1 1
---
1

2 2
0 0
0 0
---
0

8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
-----
2가 아닌 3 (내부 공기)


"""
from collections import deque

ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def check(cr, cc):
    cnt = 0
    for dr, dc in ds:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == -1:
            cnt += 1
    return cnt

def outer_air(): # 외부공기를 -1로 채우고, 내부 공기를 0으로 유지
    # 가장자리에 치즈가 있는 경우는 없으므로 0,0부터 시작
    # visited 대신 arr를 -1로 채우는 것으로 대체
    outq = deque() # q 대신 outq 써야하는 것 주의
    outq.append((0,0))
    arr[0][0] = -1

    while outq:
        cr, cc = outq.popleft()
        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                outq.append((nr, nc))

def rollback():
    for r in range(N):
        for c in range(M):
            if arr[r][c] == -1:
                arr[r][c] = 0

q = deque()  # 처음 큐를 초기화, 이후 시간을 하나씩 늘릴 때마다 큐를 대체
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r, c))
sec = 0
while q:  # q = nq 식으로 대체한 큐가 비어있게 된다면
    sec += 1
    newq = deque()
    delq = deque()

    outer_air()

    while q:  # q에 하나씩 꺼내서 nq에 넣을지 여부 결정
        cr, cc = q.popleft()
        if check(cr, cc) >= 2:  # 빈칸이 2개 이상 있다면
            delq.append((cr, cc))
        else:
            newq.append((cr, cc))

    # 분류 완료했으면 delq에 있는 거 arr에 반영
    while delq:
        cr, cc = delq.popleft()  # delq를 pop해야함
        arr[cr][cc] = 0

    q = newq

    rollback()

    # print(sec)
    # for lst in arr:
    #     print(lst)
print(sec)

# def check(cr, cc):
#     cnt = 0
#     for dr, dc in ds:
#         nr, nc = cr + dr, cc + dc
#         if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
#             cnt += 1
#     return cnt