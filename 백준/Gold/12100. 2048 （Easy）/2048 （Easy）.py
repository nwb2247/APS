"""
[반드시 다시 풀기]

[요약평]
구상이 미흡하다....
구상이 미흡한데, 바로 구현하려 하면 시간이 더 오래걸림

=> 구상의 완성도를 높이기 위해선 그림으로도 정리해야함!!!
    말로만 정리해두면, 다시 읽으면서 썼던 것을 오해할 수 있음
    또한 그림으로 대충이라도 그려봐야 놓친 부분을 찾기 수월함


한 방법이 떠올랐다고 해서 바로 구현으로 넘어가지 말고,
1. 미흡한 부분, 잘못된 부분 없는지 (!!! 특히 내가 생각한 방식이 구현이 너무 복잡하다면..)
2. 더 쉬운 방법은 없는지
더 깊게 생각하고 넘어가야함
(잘못된 방법으로 구현했다가 나중에 뜯어 고치는게 훨씬 오래걸림)

[타임라인]
이해 및 구상 : 15분
구현 및 디버깅 : 88분
- 디버깅 요소
    move()에서 move_each() 분리하고 처음 구현하고 제대로 작동하는지 확인 (19분)
    떨어져 있는 경우를 처리 하지 않고 바로 인접한 것끼리만 확인한 문제 발견 및 수정 (15분)

[이해 및 구상]
-) 내부가 꽉 차있다는 가정에서만 구상함
    구상, 구현, 디버깅 과정에서 모든 입력 상황을 고려해야하자
-) 오픈 테케 + 그림을 제대로 확인하고 이해했어야함... => 손구상에도 그려놔야할듯...

[구현]
+) 우선 한 방향에 대해서만 구현해보되, 이를 나중에 함수화(move_each) 좋도록 일반화된 방법으로 코드를 작성함

[시간복잡도]
4**5 * N**2

"""

# [손구상 내용]
# 한 이동에서 합쳐졌던 건 다시 합쳐질 수 없음
# 동일한 수 3개 -> 이동하려는 칸이 먼저 합쳐짐
#
# 백트래킹.. 복원 어떻게? 돌릴때 arr 만들자
#
# 이동방향의 반대 방향으로 증가 시키면서 => (D) 떨어져 있는 것을 고려하지 못함....
# while oob
#     이전 것과 같으면 합치고 인덱스 +2 해줌
#     다르면 아무것도 하지 않고 인덱스 +1 해줌




from itertools import permutations

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 0상 1하 2좌 3우
rev = [1, 0, 3, 2]


def oob(r, c):
    return not (0 <= r < Z and 0 <= c < Z)


Z = int(input())
arr = [list(map(int, input().split())) for _ in range(Z)]


def move_each(sr, sc, cd, arr):

    dr, dc = ds[rev[cd]]  # 반대방향, 이동방향의 반대 방향으로 덩어리를 찾자

    # [1] 담기
    cr, cc = sr, sc
    blocks = []
    while not oob(cr, cc):      # 끝에 도달할때까지 0이 아닌 것들을 blocks에 넣어주기 (떨어진것들을 일단 붙여놓음)
        nr, nc = cr + dr, cc + dc
        if arr[cr][cc] != 0:
            blocks.append(arr[cr][cc])
        cr, cc = nr, nc

    new_blocks = []     # (D) 떨어져 있는 것들 고려하지 않고 인접한 것이랑만 같은지를 확인했음
    ci = 0      # blocks 내의 인덱스를 의미
    while ci < len(blocks):                 # 0이 아닌 것들을 하나씩 꺼내서
        if ci+1 == len(blocks):             # 다음이 없다면, 현재만 넣어주고 break
            new_blocks.append(blocks[ci])
            break
        if blocks[ci+1] == blocks[ci]:      # 다음 것과 같다면 넣어주고 += 2
            new_blocks.append(blocks[ci]*2) # 합쳐진것을 new에 넣기
            ci += 2
        else:                               # 다르다면 넣어주고 += 1
            new_blocks.append(blocks[ci])   # 본인만 넣고
            ci += 1

    # [2] 채우기
    cr, cc = sr, sc
    idx = 0
    while not oob(cr, cc):
        if idx < len(new_blocks):   # new_blocks에 해당하는만큼 붙여서 채워주고
            arr[cr][cc] = new_blocks[idx]
        else:
            arr[cr][cc] = 0         # 나머지는 0으로 채우기
        idx += 1
        cr, cc = cr + dr, cc + dc


def move(cd, arr):                  # 각 점에 대해서 순회 시작할 첫점을 찍어주고 move_each에 넘김
    if cd == 0:  # 상 이동
        for sc in range(Z):
            sr = 0
            move_each(sr, sc, cd, arr)
    elif cd == 1:  # 하 이동
        for sc in range(Z):
            sr = Z - 1
            move_each(sr, sc, cd, arr)
    elif cd == 2:  # 좌 이동
        for sr in range(Z):
            sc = 0
            move_each(sr, sc, cd, arr)
    elif cd == 3:  # 우 이동
        for sr in range(Z):
            sc = Z - 1
            move_each(sr, sc, cd, arr)


# 최대! 5번 but 움직여서 더 작아지는 경우는 없으므로 5번 움직여보자
K = 5
way = [-1]*K
ans = 0
def backtrack(depth):
    global ans

    if depth == K:          # 5개 다 골랐으면
        narr = [lst[:] for lst in arr]
        for i in way:
            move(i, narr)
        ans = max(ans, max(map(max, narr))) # 가장 큰 블록
        return

    for i in range(4):
        way[depth] = i
        backtrack(depth+1)

backtrack(0)
print(ans)

# 1차 시도 (오답) / 같은 크기의 것이 바로 붙어있지 않은 경우를 고려하지 못함
# from itertools import permutations
#
# ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 0상 1하 2좌 3우
# rev = [1, 0, 3, 2]
#
#
# def oob(r, c):
#     return not (0 <= r < Z and 0 <= c < Z)
#
#
# Z = int(input())
# arr = [list(map(int, input().split())) for _ in range(Z)]
#
#
# def move_each(sr, sc, er, ec, cd, arr):
#     # [1] 담기
#     cr, cc = sr, sc
#     dr, dc = ds[rev[cd]]  # 반대방향
#     pos = []
#     while not oob(cr, cc):
#         nr, nc = cr + dr, cc + dc
#         if arr[cr][cc] == 0:
#             cr, cc = nr, nc
#             continue
#
#         if oob(nr, nc):
#             pos.append(arr[cr][cc])
#             break
#
#         elif arr[nr][nc] == arr[cr][cc]:
#             pos.append(arr[cr][cc] * 2)
#             cr, cc = nr + dr, nc + dc
#         else:
#             pos.append(arr[cr][cc])
#             cr, cc = nr, nc
#
#     # print(sr, sc, pos)
#
#     # [2] 채우기
#     cr, cc = sr, sc
#     dr, dc = ds[rev[cd]]  # 역방향
#     idx = 0
#     while not oob(cr, cc):
#         if idx < len(pos):
#             arr[cr][cc] = pos[idx]
#         else:
#             arr[cr][cc] = 0
#         idx += 1
#         cr, cc = cr + dr, cc + dc
#
#
# def move(cd, arr):
#     if cd == 0:  # 상 이동
#         for sc in range(Z):
#             sr = 0
#             ec = sc
#             er = Z - 1
#             move_each(sr, sc, er, ec, cd, arr)
#     elif cd == 1:  # 하 이동
#         for sc in range(Z):
#             sr = Z - 1
#             ec = sc
#             er = 0
#             move_each(sr, sc, er, ec, cd, arr)
#     elif cd == 2:  # 좌 이동
#         for sr in range(Z):
#             sc = 0
#             er = sr
#             ec = Z - 1
#             move_each(sr, sc, er, ec, cd, arr)
#     elif cd == 3:  # 우 이동
#         for sr in range(Z):
#             sc = Z - 1
#             er = sr
#             ec = 0
#             move_each(sr, sc, er, ec, cd, arr)
#
# # 최대! 5번 but 움직여서 더 작아지는 경우는 없으므로 5번 움직여보자
# K = 5
# way = [-1]*K
# ans = 0
# def backtrack(depth):
#     global ans
#
#     if depth == K:
#         narr = [lst[:] for lst in arr]
#         for i in way:
#             move(i, narr)
#         ans = max(ans, max(map(max, narr)))
#         return
#
#     for i in range(4):
#         way[depth] = i
#         backtrack(depth+1)
#
# backtrack(0)
# print(ans)
#
