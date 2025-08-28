"""
[요약평]
BFS 뺄때 처리하는 것은 넣을때는 처리하면 안됨
중복 로직은 모듈화
주어진 테케 한번 풀어보기
진입 가능 조건이 까다로운 문제
while q:
    while q:
    
    [경우에 따라 q에 새로운 것을 추가] (ex) 이전에 못들어갔던 곳 들어가려면,,]

"""

"""
벽 *
문서 $
열쇠 소문자
문 대문자
가지고 있지 않으면 0

엣지
1
2 2
$$
$$
b
-----
4이 나와야하는데 8가 나옴



"""
import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w", encoding="UTF-8")

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def is_key(r, c):
    return "a" <= arr[r][c] <= "z"


def is_door(r, c):
    return "A" <= arr[r][c] <= "Z"


def can_go(r, c):
    return chr(ord(arr[r][c]) - ord("A") + ord("a")) in keys


def bfs():
    not_opened = deque()
    cnt = 0

    v = [[0] * C for _ in range(R)]  # (D) R, C 거꾸로 씀
    q = deque()

    for tr in range(R):
        for tc in range(C):
            if tr in [0, R - 1] or tc in [0, C - 1]:
                if arr[tr][tc] == "*":
                    continue
                elif is_door(tr, tc):
                    if can_go(tr, tc):
                        v[tr][tc] = 1
                        q.append((tr, tc))
                    else:
                        not_opened.append((tr, tc))
                elif is_key(tr, tc) or arr[tr][tc] in ["$", "."]:
                    v[tr][tc] = 1           # (D) 갯수를 세거나 열쇠 추가는 꺼내면서 할일!!!!!!
                    q.append((tr, tc))
                # elif is_key(tr, tc):
                #     keys.add(arr[tr][tc])
                #     v[tr][tc] = 1
                #     q.append((tr, tc))
                # elif arr[tr][tc] == "$":
                #     v[tr][tc] = 1
                #     cnt += 1                # (D) 갯수를 세거나 열쇠 추가는 꺼내면서 할일!!!!!!
                #     q.append((tr, tc))
                # elif arr[tr][tc] == ".":
                #     v[tr][tc] = 1
                #     q.append((tr, tc))


    while q:
        while q:
            # 열쇠 문서 등은 제약없이 갈 수 있으므로 꺼내면서
            # 문 벽은 제약 있으므로 넣으면서 확인
            cr, cc = q.popleft()
            if is_key(cr, cc):
                keys.add(arr[cr][cc])
            elif arr[cr][cc] == "$":
                cnt += 1

            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc):
                    continue
                if v[nr][nc] == 1:
                    continue
                if arr[nr][nc] == "*":
                    continue
                if is_door(nr, nc):
                    if can_go(nr, nc):
                        v[nr][nc] = 1
                        q.append((nr, nc))
                    else:
                        not_opened.append((nr, nc))
                else:
                    v[nr][nc] = 1
                    q.append((nr, nc))

        tmpq = deque()
        while not_opened:
            nr, nc = not_opened.popleft()
            if can_go(nr, nc):
                q.append((nr, nc))
            else:
                tmpq.append((nr, nc))
        not_opened = tmpq

    # for l in v:
    #     print(l)
    print(cnt)


TC = int(input())
for _ in range(TC):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    kst = input()
    keys = set()
    if kst != "0":
        keys = set(list(kst))
    bfs()

# 1차 시도 (미제출, 기록용)
# from collections import deque
#
# DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#
# def key(r, c):
#     # print(arr[r][c], chr(ord(arr[r][c]) - ord("A") + ord("a")))
#     return chr(ord(arr[r][c]) - ord("A") + ord("a"))
#
#
# def oob(r, c):
#     return not (0<=r<H and 0<=c<W)
#
#
# def bfs(sr, sc):
#     # 처음이 문서거나 열쇠인 경우도 확인해줘야함
#     # 근데 어차피 q에 append하고 바로 pop할거니까 거기서 해주자
#     v = [[0]*W for _ in range(H)]
#     q = deque()
#     q.append((sr, sc))
#     v[sr][sc] = 1
#     sset = set() # 문서 먹은 개수
#     keys = keys_fisrt.copy()
#     no_opened = deque()
#     while q:
#         # print(q, keys)
#         while q:
#             cr, cc = q.popleft()
#
#             if arr[cr][cc] == "$":
#                 sset.add((cr, cc))
#             elif "a" <= arr[cr][cc] <= "z":
#                 keys.add(arr[cr][cc])
#
#             for dr, dc in DS:
#                 nr, nc = cr+dr, cc+dc
#                 if oob(nr, nc) or v[nr][nc] == 1 or arr[nr][nc] == "*":
#                     continue
#                 # print("A" <= arr[nr][nc] <= "Z", arr[nr][nc])
#                 if "A" <= arr[nr][nc] <= "Z":
#                     if key(nr, nc) not in keys:
#                         no_opened.append((nr, nc))
#                         continue
#                 v[nr][nc] = 1
#                 q.append((nr, nc))
#                 # print(q)
#         # print(no_opened)
#         new_no_opened = deque()
#         while no_opened:
#             nr, nc = no_opened.popleft()
#             if key(nr, nc) in keys:
#                 q.append((nr, nc))
#             else:
#                 new_no_opened.append((nr, nc))
#         no_opened = new_no_opened
#         # print(no_opened)
#
#     print(sr, sc)
#     for l in v:
#         print(l)
#     print(sset, keys)
#
#     return len(sset)
#
#
#
# TC = int(input())
# for _ in range(TC):
#     H, W = map(int, input().split())
#     arr = [list(input()) for _ in range(H)]
#     keys_fisrt = set(list(input()))
#
#     ans = 0
#     # (0, 0) 등이 겹치긴 하지만 4번 뿐이므로 그냥하자
#     # 벽 또는 문이면 진행 안됨
#     for zr in range(H):
#         if arr[zr][0] != "*" and not ("A" <= arr[zr][0] <= "Z" and key(zr, 0) not in keys_fisrt):
#             print("A" <= arr[zr][0] <= "Z", key(zr, 0) in keys_fisrt)
#             ans = max(ans, bfs(zr, 0))
#         if arr[zr][W-1] != "*" and not ("A" <= arr[zr][W-1] <= "Z" and key(zr, W-1) not in keys_fisrt):
#             ans = max(ans, bfs(zr, W-1))
#
#     for zc in range(W):
#         if arr[0][zc] != "*" and not ("A" <= arr[0][zc] <= "Z" and key(0, zc) not in keys_fisrt):
#             ans = max(ans, bfs(0, zc))
#         if arr[H-1][zc] != "*" and not ("A" <= arr[H-1][zc] <= "Z" and key(H-1, zc) not in keys_fisrt):
#             ans = max(ans, bfs(H-1, zc))
#
#     print(ans)
#
#
#
#
