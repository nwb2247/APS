"""
(4차시도)
BFS 응용
원래 BFS는 각 정점 한번씩만 방문하지만,
적은 말이동 횟수로 다시 도착한 경우에는 이미 방문했더라도 한번 더 넣어주자

BFS이므로 짧은 거리에서 긴 거리로 순차적으로 진행된다.
따라서 r, c에 이미 방문했는데, 이 곳에 다시 도달한다는 것은 이전에 왔던 거리보다 작지 않다는 것을 의미한다.
따라서 r, c에 말이동 횟수 k를 써서 온것이 최소였다면, k보다 크거나 같은 경우로 온경우는 결코 목적지까지 더 이전의 방법보다 짧아질 수 없다.
그러나 k보다 작은 횟수로 온 경우에는 말이동횟수가 적어도 하나 이상 더 있는 상태이므로, 목적지까지 더 짧게 도달가능한 경우가 존재할 수 있다.
따라서 k보다 작은 횟수로 온 경우에는 append하고 계속 진행해야한다.

(참고)
위 방법은 400ms
v[r][c][몇번의 횟수로 방문왔었는지] 는 3000ms


"""
from collections import deque

monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
horse = [(-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2)]


def oob(r, c):
    return not (0 <= r < H and 0 <= c < W)


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(H)]

v = [[-1 for _ in range(W)] for _ in range(H)]

q = deque()
v[0][0] = 0 # 말이동 횟수 0번으로 도달가능
q.append((0, 0, 0, 0))  # cr, cc, k, sec (횟수)

ans = -1
while q:
    cr, cc, ck, sec = q.popleft()

    if (cr, cc) == (H - 1, W - 1):
        ans = sec
        break

    if ck < K:  # 말 이동횟수가 남아있다면 말이동 시도해봄
        for dr, dc in horse:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or arr[nr][nc] == 1: # 범위밖이거나 장애물이면 패스
                continue

            if v[nr][nc] == -1 or v[nr][nc] > ck+1: # 방문하지 않았거나, 더 적은 말이동횟수로 도달가능한 경우라면
                v[nr][nc] = ck+1
                q.append((nr, nc, ck + 1, sec + 1))

    for dr, dc in monkey: # 원숭이 이동은 항상 시도
        nr, nc = cr + dr, cc + dc
        if oob(nr, nc) or arr[nr][nc] == 1:
            continue

        if v[nr][nc] == -1 or v[nr][nc] > ck:
            v[nr][nc] = ck
            q.append((nr, nc, ck, sec + 1))

print(ans)


"""
(1차시도) 실패
백트래킹 -> 시간 초과

(2차 시도) 3000ms
3차원 visited, 지금까지의 말이동 수 k보다 작은 값으로 + 같거나 짧은 거리로 왔다면 패스

(3차 시도) 3000ms
3차원, 이동횟수는 q로 관리, v는 방문여부만 (방문했다는 것은 이미 최소거리로 도달했다는 뜻)
+
같은 k에서만 비교 (뭐가 더 빠를지?)
+
H-1, W-1 도달했다면 break
=> (1000ms로 단축)
"""

#########################################################

"""
3차 시도 (3000ms)
3차원, 이동횟수는 q로 관리, v는 방문여부만 (방문했다는 것은 이미 최소거리로 도달했다는 뜻)
+
같은 k에서만 비교
H-1, W-1 도달했다면 break
=> (1000ms로 단축)
"""
# from collections import deque
#
# monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# horse = [(-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2)]
#
#
# def oob(r, c):
#     return not (0 <= r < H and 0 <= c < W)
#
#
# K = int(input())
# W, H = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(H)]
#
# v = [[[0 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]
# dist = [[float('inf')] * W for _ in range(H)]
#
# q = deque()
# v[0][0][0] = 1
# q.append((0, 0, 0, 0))  # cr, cc, k, sec
#
# ans = float('inf')
# while q:
#     cr, cc, ck, sec = q.popleft()
#
#     if (cr, cc) == (H - 1, W - 1):
#         ans = min(ans, sec)
#         break
#
#     if ck < K:
#         for dr, dc in horse:
#             nr, nc = cr + dr, cc + dc
#             if oob(nr, nc) or arr[nr][nc] == 1:
#                 continue
#
#             if v[nr][nc][ck + 1] == 0:
#                 v[nr][nc][ck + 1] = 1
#                 q.append((nr, nc, ck + 1, sec + 1))
#
#     for dr, dc in monkey:
#         nr, nc = cr + dr, cc + dc
#         if oob(nr, nc) or arr[nr][nc] == 1:
#             continue
#
#         for i in range(ck + 1):
#             if v[nr][nc][i] != 0:
#                 break
#         if v[nr][nc][ck] == 0:
#             v[nr][nc][ck] = 1
#             q.append((nr, nc, ck, sec + 1))

# for l in v:
#     print(v)

# for l in v:
#     print(l)

"""
2차시도
3차원 visited (3000ms)
"""
# from collections import deque
#
#
# monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# horse = [(-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2)]
#
#
# def oob(r, c):
#     return not (0 <= r < H and 0 <= c < W)
#
#
# K = int(input())
# W, H = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(H)]
#
# v = [[[-1 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
#
# q = deque()
# v[0][0][0] = 0
# q.append((0, 0, 0))
#
# while q:
#     cr, cc, ck = q.popleft()
#
#     if ck < K:
#         for dr, dc in horse:
#             nr, nc = cr+dr, cc+dc
#             if oob(nr, nc) or arr[nr][nc] == 1:
#                 continue
#
#             for i in range(ck+2):
#                 if v[nr][nc][i] != -1 and v[nr][nc][i] <= v[cr][cc][ck] + 1:
#                     break
#             else:
#                 v[nr][nc][ck+1] = v[cr][cc][ck] + 1
#                 q.append((nr, nc, ck+1))
#
#     for dr, dc in monkey:
#         nr, nc = cr+dr, cc+dc
#         if oob(nr, nc) or arr[nr][nc] == 1:
#             continue
#
#         for i in range(ck+1):
#             if v[nr][nc][i] != -1 and v[nr][nc][i] <= v[cr][cc][ck] + 1:
#                 break
#         else:
#             v[nr][nc][ck] = v[cr][cc][ck] + 1 # (D) v[nr][nc][ck]를 v[nr][nc] 로 씀;;
#             q.append((nr, nc, ck))
#
# # for l in v:
# #     print(v)
#
# ans = float('inf')
# for i in range(K+1):
#     if v[H-1][W-1][i] != -1 and ans >= v[H-1][W-1][i]:
#         ans = v[H-1][W-1][i]
#
# if ans == float("inf"):
#     print(-1)
# else:
#     print(ans)
#

"""
1차 시도
백트래킹 시간초과
"""

# monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# horse = [(-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2)]
#
#
# def oob(r, c):
#     return not (0 <= r < H and 0 <= c < W)
#
#
# def backtrack(cr, cc, sec, k):
#     global ans
#     if sec >= ans:  # 가지치기
#         return
#
#     if (cr, cc) == (H-1, W-1):
#         ans = min(ans, sec)
#         return
#
#     for dr, dc in monkey:
#         nr, nc = cr + dr, cc + dc
#         if oob(nr, nc):
#             continue
#         if v[nr][nc] == 0 and arr[nr][nc] != 1:
#             v[nr][nc] = 1
#             backtrack(nr, nc, sec + 1, k)
#             v[nr][nc] = 0
#
#     if k > 0:
#         for dr, dc in horse:
#             nr, nc = cr + dr, cc + dc
#             if oob(nr, nc):
#                 continue
#             if v[nr][nc] == 0 and arr[nr][nc] != 1:
#                 v[nr][nc] = 1
#                 backtrack(nr, nc, sec + 1, k-1)
#                 v[nr][nc] = 0
#
#
# K = int(input())
# W, H = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(H)]
#
# v = [[0] * W for _ in range(H)]
#
# ans = float('inf')
# v[0][0] = 1
# backtrack(0, 0, 0, K)
#
# if ans == float('inf'):
#     print(-1)
# else:
#     print(ans)

