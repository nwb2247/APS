# python에서 -1 인덱스는 마지막 인덱스이므로 index error가 나지 않고 엉뚱한 답을 내놓음
# 따라서 빈 공간을 -1로 초기화하면 실수하기 쉽거나, 별도의 처리가 필요함
# 0으로 초기화하고 시작 입력을 0번째가 아닌 1번째로 받자
arr = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(1, N+1) :    # 0번째가 아닌 1번째부터 받으므로 (N+1)
    # 시작 좌표, 너비, 높이 받기
    sc, sr, w, h = map(int, input().split())
    # 해당 숫자로 덧씌우기
    for r in range(sr, sr+h) :
        for c in range(sc, sc+w) :
            arr[r][c] = i
cnts = [0]*(N+1)            # 0번째가 아닌 1번째부터 받으므로 (N+1)
for r in range(1001) :
    for c in range(1001) :
        num = arr[r][c]
        # -1일땐 pass 해야함
        # (주의 : python에서 -1 인덱스는 마지막 인덱스이므로 index error가 나지 않고 엉뚱한 답을 내놓음)
        if num != -1 :
            cnts[num] += 1
        # else :
        #     pass
print(*cnts[1:], sep="\n")

# 1번째 시도
# arr = [[-1]*1001 for _ in range(1001)]
# # 0번째, 1번째 등으로 받을 예정이므로, -1로  초기화
# N = int(input())
# for i in range(N) :
#     # 시작 좌표, 너비, 높이 받기
#     sc, sr, w, h = map(int, input().split())
#     # 해당 숫자로 덧씌우기
#     for r in range(sr, sr+h) :
#         for c in range(sc, sc+w) :
#             arr[r][c] = i
# cnts = [0]*N
# for r in range(1001) :
#     for c in range(1001) :
#         num = arr[r][c]
#         # -1일땐 pass 해야함
#         # (주의 : python에서 -1 인덱스는 마지막 인덱스이므로 index error가 나지 않고 엉뚱한 답을 내놓음)
#         if num != -1 :
#             cnts[num] += 1
#         # else :
#         #     pass
# print(*cnts, sep="\n")
#
