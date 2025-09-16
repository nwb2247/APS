"""
[2차 풀이]

- 거의 동일하게 풀었음
- turn 에 대해서 for로 쓰는게 안전할지 while로 쓰는게 안전할지는 좀더 생각해봐야 할듯
    -> while이 좀더 쉬울거 같은??


[이해 및 구상]

3*3
행 개수가 열의 개수보다 크거나 같은 경우
    모든 행에 대해서 정렬 수행, 출현 빈도가 적은 순서대로 정렬
    출현횟수가 같은 숫자가 있는경우 해당 숫자가 작은 순서대로 정렬
    정렬 수행시 해당 숫자와 해당 숫자의 출현 빈도수를 함께 출력

    가장 큰 길이의 행을 기준으로 나머지도 0으로 채워주기,
    단 0에 대해서는 연산을 수행할때 무시함

행의 개수가 열의 개수보다 적은 경우
    열에 대해서 위 과정을 수행

행이나 열의 길이가 100을 넘어가는 경우 처음 100개 제외하고는 모두 버림

A[r][c]가 원하는 값이 될때까지 얼마나 걸리는지 시간을 구하기
r, c가 oob일수도?

"""
from collections import defaultdict

def oob(r, c):
    return not (0<=r<len(A) and 0<=c<len(A[0]))

def operate():
    for cr in range(len(A)):
        cnts = defaultdict(int)
        for cc in range(len(A[cr])):
            if A[cr][cc] == 0: # 0에 대해서는 연산하지 않음
                continue
            cnts[A[cr][cc]] += 1
        tmp = []
        for num in cnts:
            tmp.append((cnts[num], num)) # 빈도수, 숫자
        tmp.sort() # 사전 순 정렬
        nlst = []
        for cnt, num in tmp:
            nlst.append(num)    # 넣을때는 num먼저 그다음 cnt
            nlst.append(cnt)
        A[cr] = nlst

    mxlen = min(max(map(len, A)), 100)
    for cr in range(len(A)):
        if mxlen <= len(A[cr]):
            A[cr] = A[cr][:mxlen]
        else:
            A[cr].extend([0] * (mxlen - len(A[cr])))
    return

def solve():
    global A
    for turn in range(100 + 1):
        if not oob(er, ec) and A[er][ec] == K:
            break
        turn += 1
        if len(A) >= len(A[0]): # 행 길이가 열 길이 보다 크거나 같은 경우
            operate()
        else: # 아니라면 전치 -> 연산 -> 다시 전치
            A = [list(lst[:]) for lst in zip(*A)]
            operate()
            A = [list(lst[:]) for lst in zip(*A)]
        # for l in A:
        #     print(l)

    if turn == 100 + 1:
        print(-1)
    else:
        print(turn)



    return
er, ec, K = map(int, input().split())
er -= 1
ec -= 1
A = [list(map(int, input().split())) for _ in range(3)]

solve()

# ----------------------- 1차 풀이 ------------------------
# """
# [요약평]
# 시간 복잡도 괜찮다면 전치행렬 사용하자
# 종료조건이 초, 횟수 등으로 나올때 엣지 조심 (100초)
#
# [타임라인]
# (녹화파일 깨져서 정확하지 않음)
# 이해 및 구상 : 10분
# 구현 : 15분
# 디버깅 : 5분
# -------------------
# 총 30분
#
# [이해 및 구상]
# -) 열 연산에 대해서 미리 생각해보지 않음
# +) cnt를 defaultdict로 구현하는 것 미리 생각
#
# [구현]
# -) 전치 연산 시 시간 복잡도도 계산해뒀다면 좋았을 듯
# +) Z로 최대 개수를 설정 (디버깅 시 용이)
# +) 100초까지만 확인하도록 초반에 미리 생각
#
# [디버깅]
# +) 예제를 대상으로 제대로 배열이 바뀌는지 확인
# +) Z를 낮은 값 ex) 4 로 설정해 Z보다 커질 시 자리는 것까지 확인
#
#
#
# """
#
#
# from collections import defaultdict
#
# er, ec, K = map(int, input().split())
# er -= 1
# ec -= 1
# Z = 100
# arr = [list(map(int, input().split())) for _ in range(3)]
#
# def row_op(arr):
#
#     for r in range(len(arr)):
#         cnt = defaultdict(int)
#         for c in range(len(arr[r])):
#             if arr[r][c] != 0:
#                 cnt[arr[r][c]] += 1
#         tmp = []
#         for k, v in cnt.items():
#             tmp.append((k, v)) # 수, 개수
#         tmp.sort(key=lambda x: (x[1], x[0]))
#         arr[r] = []
#         for num, c in tmp:
#             arr[r].append(num)
#             arr[r].append(c)
#         if len(arr[r]) > Z:
#             arr[r] = arr[r][:Z]
#     mxlen = max(map(len, arr))
#     for r in range(len(arr)):
#         for _ in range(mxlen - len(arr[r])):
#             arr[r].append(0)
#
#     return arr
#
# t = 0
# while True:
#     # 되는지부터 확인
#     if er<len(arr) and ec<len(arr[0]) and arr[er][ec] == K:
#         break
#     t += 1
#     if t > 100:
#         t = -1
#         break
#     if len(arr) >= len(arr[0]):
#         arr = row_op(arr)
#     else:
#         arr_t = [list(lst) for lst in zip(*arr)]
#         arr_t = row_op(arr_t)
#         arr = [list(lst) for lst in zip(*arr_t)]
#
# print(t)

