"""
----------------------------------------------
확실하게 설계하지 못할 것 같으면 다른 방법 찾기!!!!!!!!!
왠지 맞을 거 같다고 시작해버리면 시간 허비 가능성 커짐
----------------------------------------------

아이디어 (3차) :
6*5 / 2 = 15경기
승무패 3^15 시간 상 터짐
가지치기 필수
(A, B) (A, C), ..... (A, F), (B, C) , ... (E, F) 15개를 하나씩 확정지으면서
ARR에 값을 추가해주고 경기 결과(RES)를 비교
경기 결과보다 커지면 무얼 추가해주더라도 RES 못만듦 -> 가지치기
완성 되면 원래 결과랑 비교해주기 같으면 found = True 처리

=> 리팩토링 (4차)
ARR를 따로 두는 대신 RES를 직접 줄이기 (어차피 원상복구 확실하게 되므로)
확인 부분 함수화


---------------------

(1차 구상)
15 경기에 대한 모든 결과를 만들면서 그 결과가 4개 TC와 일치하는지 확인
-> 시간 터짐

(2차 구상)
백트래킹으로 앞 팀의 승무패를 하나씩 까면서 다음 것을 확인
A팀 승 -> A팀 무 -> A팀 패 -> B팀 승....
시간 오래걸림 + 틀림
=> 복원 등이 너무 까다롭고 설계가 엄밀하지 않음...


"""


# 리팩토링
def check():
    global found
    for r in range(6):
        for c in range(3):
            if RES[r][c] != 0:
                return              # (B) break 쓰면 대형사고

    found = True
    return


def backtrack(depth):

    # for l in RES:
    #     print(l)
    # print()

    if depth == L:  # 다 완성됐다면 일치하는지 확인
        check()
        return

    x, y = VS[depth]

    for i in range(3):
        RES[x][i] -= 1
        RES[y][2 - i] -= 1
        if RES[x][i] >= 0 and RES[y][2 - i] >= 0:
            backtrack(depth + 1)
            if found:  # 찾았으면 가지치기
                return
        RES[x][i] += 1
        RES[y][2 - i] += 1


VS = []
for i in range(6):
    for j in range(i + 1, 6):
        VS.append((i, j))
L = len(VS)

ans = []
for tc in range(4):
    lst = list(map(int, input().split()))
    RES = [[0 for _ in range(3)] for _ in range(6)]
    for i in range(6):
        for j in range(3):
            RES[i][j] = lst[3 * i + j]
    found = False
    backtrack(0)
    if found:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)

# ------------------ 3차 풀이 (정답) -----------
# def backtrack(depth):
#
#     global found
#
#     if depth == L: # 다 완성됐다면 일치하는지 확인
#         bad = False
#         for r in range(6):
#             for c in range(3):
#                 if ARR[r][c] != RES[r][c]:
#                     bad = True
#                     break
#             if bad:
#                 break
#         else:
#             found = True
#         return
#
#     x, y = VS[depth]
#
#     for i in range(3):
#         ARR[x][i] += 1
#         ARR[y][2-i] += 1
#         if ARR[x][i] <= RES[x][i] and ARR[y][2-i] <= RES[y][2-i]:
#             backtrack(depth + 1)
#             if found:           # 찾았으면 가지치기
#                 return
#         ARR[x][i] -= 1
#         ARR[y][2-i] -= 1
#
# VS = []
# for i in range(6):
#     for j in range(i+1, 6):
#         VS.append((i, j))
# L = len(VS)
#
# ans = []
# for tc in range(4):
#     lst = list(map(int, input().split()))
#     RES = [[0 for _ in range(3)] for _ in range(6)]
#     for i in range(6):
#         for j in range(3):
#             RES[i][j] = lst[3*i + j]
#     ARR = [[0 for _ in range(3)] for _ in range(6)]
#     found = False
#     backtrack(0)
#     if found:
#         ans.append(1)
#     else:
#         ans.append(0)
# print(*ans)

# -------------------- 2차 구상 (오답) ---------------------
# def backtrack(r, c):
#     global found
#     # print(f"info : {tc, r, c}")
#     # for l in RES:
#     #     print(*l)
#     # print()
#
#     if RES[r][c] > sum(map(lambda x:x[2-c], RES[r+1:])):
#         return
#
#     if (r, c) == (5, 2) and RES[r][c] == 0:
#         found = True
#         # print(tc, found)
#         return
#
#     if RES[r][c] > 0:
#         RES[r][c] -= 1
#         for nr in range(r+1, 6):
#             if RES[nr][2-c] > 0:
#                 RES[nr][2-c] -= 1
#                 backtrack(r, c)
#                 if found:
#                     return
#                 RES[nr][2-c] += 1
#         RES[r][c] += 1
#
#     else:
#         if c == 2:
#             backtrack(r+1, 0)
#         else:
#             backtrack(r, c+1)
#
#
# ans = []
# for tc in range(4):
#     LST = list(map(int, input().split()))
#     RES = [[] for _ in range(6)]
#     for i in range(6):
#         wl = [0]*3
#         for j in range(3):
#             wl[j] = LST[3*i+j]
#         RES[i] = wl
#     # print(RES)
#     found = False
#     backtrack(0, 0)
#     if found:
#         ans.append(1)
#     else:
#         ans.append(0)
# print(*ans)
#
