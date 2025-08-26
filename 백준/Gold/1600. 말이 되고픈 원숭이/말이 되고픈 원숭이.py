"""
(테스트 : H-1, W-1 만나도 break안하고 갱신만 하면 터짐?)
3차원, 이동횟수는 q로 관리, v는 방문여부만 (방문했다는 것은 이미 최소거리로 도달했다는 뜻)
+
같은 k에서만 비교 (뭐가 더 빠를지?)
+
H-1, W-1 도달했다면 break
=> (1000ms로 단축)

=> 그냥 최소로 방문한 k를 넣어버리자
(k번만 사용하고도 최소비용으로 여기에 올 수 있다는 뜻이므로)
단, 같은 dist인데 k가 더 작다면 같은 k로 갱신
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
dist = [[float('inf')] * W for _ in range(H)]

q = deque()
v[0][0] = 0
q.append((0, 0, 0, 0))  # cr, cc, k, sec

ans = float('inf')
while q:
    cr, cc, ck, sec = q.popleft()

    if (cr, cc) == (H - 1, W - 1):
        ans = min(ans, sec)
        # break

    if ck < K:
        for dr, dc in horse:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc) or arr[nr][nc] == 1:
                continue

            if v[nr][nc] == -1 or v[nr][nc] > ck+1:
                v[nr][nc] = ck+1
                q.append((nr, nc, ck + 1, sec + 1))

    for dr, dc in monkey:
        nr, nc = cr + dr, cc + dc
        if oob(nr, nc) or arr[nr][nc] == 1:
            continue

        if v[nr][nc] == -1 or v[nr][nc] > ck:
            v[nr][nc] = ck
            q.append((nr, nc, ck, sec + 1))

if ans == float("inf"):
    print(-1)
else:
    print(ans)

# """
# 3차원, 이동횟수는 q로 관리, v는 방문여부만 (방문했다는 것은 이미 최소거리로 도달했다는 뜻)
# +
# 같은 k에서만 비교 (뭐가 더 빠를지?)
# => (1000ms로 단축)
# """
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

# """
# 3차원, 이동횟수는 q로 관리, v는 방문여부만 (방문했다는 것은 이미 최소거리로 도달했다는 뜻)
# (3000ms)
# """
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
# v = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
# dist = [[float('inf')]*W for _ in range(H)]
#
# q = deque()
# v[0][0][0] = 1
# q.append((0, 0, 0, 0)) # cr, cc, k, sec
#
#
# ans = float('inf')
# while q:
#     cr, cc, ck, sec = q.popleft()
#
#     if (cr, cc) == (H-1, W-1):
#         ans = min(ans, sec)
#         break
#
#     if ck < K:
#         for dr, dc in horse:
#             nr, nc = cr+dr, cc+dc
#             if oob(nr, nc) or arr[nr][nc] == 1:
#                 continue
#
#             for i in range(ck+2):
#                 if v[nr][nc][i] != 0:
#                     break
#             else:
#                 v[nr][nc][ck+1] = 1
#                 q.append((nr, nc, ck+1, sec + 1))
#
#     for dr, dc in monkey:
#         nr, nc = cr+dr, cc+dc
#         if oob(nr, nc) or arr[nr][nc] == 1:
#             continue
#
#         for i in range(ck+1):
#             if v[nr][nc][i] != 0:
#                 break
#         else:
#             v[nr][nc][ck] = 1
#             q.append((nr, nc, ck, sec + 1))
#
# # for l in v:
# #     print(v)
#
# # for l in v:
# #     print(l)
#
# if ans == float("inf"):
#     print(-1)
# else:
#     print(ans)


# """
# 3차원 visited (3000ms)
# """
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
