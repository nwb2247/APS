"""
[2차 풀이]
사다리 표현 방식을 벽 표현처럼 바꿈 (양옆으로 갈 수 있는지 없는지)
최소 추가 횟수를 구하는 것이므로 bfs 쓸까하다가 구상이 잘안되서 백트래킹으로 감
depth >= ans 가지치기는 꼭 기억하자

----------------------------------------------------


3개 보다 큰 값이거나 버그를 고치는 것이 불가능하다면 -1를 출력

종료조건 depth == 3 + 이미 3개의 유실선 추가했는데 해결안되면 -1, 해결되면 3?

고객번호, 취약지점 모두 1부터 시작 -> -1씩 빼주자


H, N = > R, C

입력에서는 겹치는 선은 주어지지 않음

wire : R*C*2 삼차원 => 양옆고객과 이어지는지...

"""


def check():
    for sc in range(C):
        cc = sc
        for cr in range(R):
            if wire[cr][cc][0] == 1:  # 왼쪽으로 가는 선이 있다면 왼쪽으로 가고
                cc -= 1
            elif wire[cr][cc][1] == 1:  # 오른쪽으로 가는 선이 있다면 오른쪽으로 감
                cc += 1
        if cc != sc:
            return False

    return True  # 모든 열이 시작과 끝이 동일한 경우에만 True 반환


def backtrack(depth, start):
    global ans

    if depth >= ans:  # 가지치기 : 이미 depth가 ans보다 크거나 동일하다면 종료
        return

    if check():  # 일단 확인, 여기서 성공하면 더 추가할일 없으므로 return, 0개인 경우도 가능...
        ans = min(ans, depth)
        return

    if depth == 3:  # 이미 3개 추가했는데도, 성공못했으면 return
        return

    for i in range(start, len(pos)):
        zr, zc = pos[i]
        if wire[zr][zc][0] == 0 and wire[zr][zc][1] == 0 and wire[zr][zc + 1][0] == 0 and wire[zr][zc + 1][1] == 0:
            # 넣을때도 한번더 확인해야함 (이전에 넣은거때문에 불가능해졌을 수 있으므로)
            wire[zr][zc][1] = 1
            wire[zr][zc + 1][0] = 1

            backtrack(depth + 1, i + 1)

            wire[zr][zc][1] = 0  # 원복
            wire[zr][zc + 1][0] = 0

    return


def solve():
    backtrack(0, 0)
    return


def init():
    for cr in range(R):
        for cc in range(C - 1):  # cc와 cc+1를 이으므로 C-2까지만 확인
            if wire[cr][cc][0] == 0 and wire[cr][cc][1] == 0 and wire[cr][cc + 1][0] == 0 and wire[cr][cc + 1][1] == 0:  # 본인, 양쪽에 1이 없어야함
                pos.append((cr, cc))  # cr에서 cc와 cc+1를 이음


C, M, R = map(int, input().split())
wire = [[[0, 0] for _ in range(C)] for _ in range(R)]  # 0왼쪽으로 가는 선 여부, 1오른쪽으로 가는 선 여부
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())  # a행에서 b와 b+1를 이음
    wire[a][b][1] = 1
    wire[a][b + 1][0] = 1
pos = []  # r, c : r지점에서 c와 c+1를 잇는 것
init()

ans = 4
solve()

if ans == 4:
    print(-1)
else:
    print(ans)


# ----------------------------------------------------------------------------------------
# """
# [반드시 다시 풀기]
# 
# [1차 풀이]
# 
# [요약평]
# 1. 백트래킹은 그냥 무조건 재귀 쓰자 (깊이가 작더라도 코드 실수를 방지하기 위해서)
# 2. 문제의 상황을 리스트 또는 다른 자료형을 이용해 어떻게 표현할것인지 확실하게 정해두고 가야함
#     ex) 사다리를 어떻게 표현할 것인가?
# 
# [타임라인]
# 이해 및 구상 18분
# 구현 + 사다리 검증 등 37분
# 총 55분
# 
# [이해 및 구상]
# -) 0번 추가 해도 정답인 경우가 다행히 테케에 있어 고려할 수 있었지만,
#     없을 경우에도 이를 생각해내는 연습이 필요
# +) 사다리를 어떻게 리스트로 표현해낼 것인가가 관건이었는데, 애매하게 넘기지 않고 확실하게 정리하고 간 것이 시간 단축, 실수 방지에 좋았음
# +) 주어진 테케를 가지고 check() 함수의 검증에도 사용 (추가 전후 사다리를 넣고 False, True가 잘 나오는지,,,)
# 
# [시간복잡도]
# N(세로선 개수 C) * H(가로선 개수 H) P 3 * N*H
# 300 * 299 * 298 * 300 ?
# 
# ---------------------------------------------------------
# 
# [손구상 내용]
# 
# 두 가로선이 연속하거나 접하면 안됨
# i시작은 i의 결과 나와야함
# 정답이 3보다 커도 -1 => 3개까지만 확인하면됨 -> 재귀말고 루프로 가보자 (Review) 재귀가 더 깔끔할 듯..
# 
# arr[x][y] :
#     => y번째 행에  x과 x+1를 잇는 가로선
#         즉 x를 타고 내려가면 양옆 가로선 정보는 [x-1] (x-1, x를 잇는)와
#         [x] (x, x+1를 잇는)를 참조해야함
#         즉, x타고 오다가 타고 내려오다가 x-1에 1있으면 x-1을 타고가고
#         x에 1 있으면 x+1을 타고감
#     x == 0, C+1은 dummy padding, 절대 1이 들어가면 안됨
#     y는 0부터 시작으로 조정, x는 그대로
# 
# 300에서 3, 2, 1개... 일단 해보기? (Review) 0개도 고려해야함
# 
# """
# 
# # def check():  # 테스트 완료
# #     res = []
# #     for i in range(1, C + 1):  # i : 시작점
# #         cr, cnum = 0, i  # 현재 몇행인지, cnum 몇열을 타고 내려가는지
# #         while cr < R:
# #             # 디버깅 위해서 4개 다 확인
# #             if arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 0:
# #                 pass  # cr += 1 도 처리 되어야하므로 pass로....
# #             elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 0:
# #                 cnum -= 1
# #             elif arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 1:
# #                 cnum += 1
# #             elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 1:
# #                 print("error!!!!!")
# #
# #             # 전부 내려가긴 해야함 (수정시 주의)
# #             cr += 1
# #
# #         # print(i, cnum)
# #         if i != cnum:  # 타고 내려오다가 다른게 있으면 바로 False 반환
# #             return False
# #     return True
# #
# #
# # def solve():  # 조합 만들어서 확인
# #     global ans
# #
# #     # 아무것도 추가안해도 가능이면? 0 만들고 바로 return
# #     if check():
# #         ans = 0
# #         return
# #
# #     # 1개
# #     for cr, cc in pos:
# #         arr[cr][cc] = 1
# #         if check():
# #             ans = 1
# #             return
# #         arr[cr][cc] = 0  # 원복
# #
# #     # 2개
# #     for i in range(L):
# #         cri, cci = pos[i]
# #         arr[cri][cci] = 1
# #         for j in range(i + 1, L):
# #             crj, ccj = pos[j]
# #             if arr[crj][ccj - 1] != 0 or arr[crj][ccj + 1] != 0:
# #                 continue
# #             arr[crj][ccj] = 1
# #             if check():
# #                 ans = 2
# #                 return
# #             arr[crj][ccj] = 0
# #         arr[cri][cci] = 0  # 원복
# #
# #     # 3개
# #     for i in range(L):
# #         cri, cci = pos[i]
# #         arr[cri][cci] = 1
# #         for j in range(i + 1, L):
# #             crj, ccj = pos[j]
# #             if arr[crj][ccj - 1] != 0 or arr[crj][ccj + 1] != 0:
# #                 continue
# #             arr[crj][ccj] = 1
# #             for k in range(j + 1, L):
# #                 crk, cck = pos[k]
# #                 if arr[crk][cck - 1] != 0 or arr[crk][cck + 1] != 0:
# #                     continue
# #                 arr[crk][cck] = 1
# #                 if check():
# #                     ans = 3
# #                     return
# #                 arr[crk][cck] = 0
# #             arr[crj][ccj] = 0
# #         arr[cri][cci] = 0  # 원복
# #
# #
# # # 실수 적은 방식으로 변수명 변경 (단, 문제의 M등이 겹칠 때 주의)
# # C, K, R = map(int, input().split())
# #
# # # [0] 사다리 표현
# # arr = [[0] * (C + 1) for _ in range(R)]
# #
# # for _ in range(K):
# #     a, b = map(int, input().split())
# #     arr[a - 1][b] = 1
# #
# # # for l in arr:
# # #     print(l)
# #
# # # [1] pos 일단 가능한 점들 넣음
# # pos = []
# # for zr in range(R):
# #     for zc in range(1, C):  # 양끝은 포함하면 안됨
# #         # 내가 0이고 양옆도 비어있을때만 추가
# #         if arr[zr][zc] == 0 and arr[zr][zc - 1] == 0 and arr[zr][zc + 1] == 0:
# #             pos.append((zr, zc))
# # L = len(pos)  # pos의 크기
# #
# # ans = -1  # 로 두고 0개 1개 2개 3개 를 차례로 확인해봄 solve() return 이용해 빠른 탈출
# # solve()
# # print(ans)
# 
# # 리팩토링 - 재귀이용 백트래킹
# def check():  # 테스트 완료
#     res = []
#     for i in range(1, C + 1):  # i : 시작점
#         cr, cnum = 0, i  # 현재 몇행인지, cnum 몇열을 타고 내려가는지
#         while cr < R:
#             # # 디버깅 위해서 4개 다 확인
#             # if arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 0:
#             #     pass  # cr += 1 도 처리 되어야하므로 pass로....
#             # elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 0:
#             #     cnum -= 1
#             # elif arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 1:
#             #     cnum += 1
#             # elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 1:
#             #     print("error!!!!!")
#             if arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 0:       # 조건 확인 시간 단축 위해 단순화
#                 cnum -= 1
#             elif arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 1:
#                 cnum += 1
# 
#             # 전부 내려가긴 해야함 (수정시 주의)
#             cr += 1
# 
#         # print(i, cnum)
#         if i != cnum:  # 타고 내려오다가 다른게 있으면 바로 False 반환
#             return False
#     return True
# 
# def backtrack(depth, start, num): # 조합 생성 / 지금까지 넣은 개수, 몇번부터 넣을건지, 총 넣을 갯수
#     global ans
# 
#     if depth == num:
#         if check():
#             ans = num
#         return
# 
#     for i in range(start, L):
#         cr, cc = pos[i]
#         if arr[cr][cc-1] != 0 or arr[cr][cc+1] != 0:
#             continue
#         arr[cr][cc] = 1
#         backtrack(depth+1, i+1, num)
#         if ans != -1:   # 찾았으면 바로 return
#             return
#         arr[cr][cc] = 0
# 
# 
# def solve():  # 조합 만들어서 확인
#     global ans
# 
#     # 아무것도 추가안해도 가능이면? 0 만들고 바로 return
#     if check():
#         ans = 0
#         return
# 
#     lst = [] # 지금까지 넣은 거
# 
#     # 1개
#     backtrack(0, 0, 1)
#     if ans != -1:
#         return
# 
#     # 2개
#     backtrack(0, 0, 2)
#     if ans != -1:
#         return
# 
#     # 3개
#     backtrack(0, 0, 3)
#     if ans != -1:
#         return
# 
# 
# # 실수 적은 방식으로 변수명 변경 (단, 문제의 M등이 겹칠 때 주의)
# C, K, R = map(int, input().split())
# 
# # [0] 사다리 표현
# arr = [[0] * (C + 1) for _ in range(R)]
# 
# for _ in range(K):
#     a, b = map(int, input().split())
#     arr[a - 1][b] = 1
# 
# # for l in arr:
# #     print(l)
# 
# # [1] pos 일단 가능한 점들 넣음 (시간 단축을 위함...)
# pos = []
# for zr in range(R):
#     for zc in range(1, C):  # 양끝은 포함하면 안됨
#         # 내가 0이고 양옆도 비어있을때만 추가
#         if arr[zr][zc] == 0 and arr[zr][zc - 1] == 0 and arr[zr][zc + 1] == 0:
#             pos.append((zr, zc))
# L = len(pos)  # pos의 크기
# 
# ans = -1  # 로 두고 0개 1개 2개 3개 를 차례로 확인해봄 solve() return 이용해 빠른 탈출
# solve()
# print(ans)
