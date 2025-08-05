"""
비트마스킹을 이용한 풀이
"""


N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
# 공집합 제외위해 1부터
for bits in range(1, 1<<N): # 가능한 모든 비트에 대해 (1<<N) 으로도 가능
    sm = 0
    for pos in range(N):            # 0~N-1 위치가 1이면 포함 sm에 추가
        if ((bits>>pos) & 1) == 1:  # 위치가 1이면 선택
            sm += lst[pos]
    if sm == S:
        ans += 1

print(ans)

# # 시간복잡도: 2^N (N<=20이므로 안전함)

# def dfs(depth, sm):
#     # depth: 몇번째 원소의 포함여부를 결정할 지 (종료조건의 N, depth 등을 잘 결정하자)
#     # sm : 지금가지의 합
#     global ans
#     if depth == N: # 모든 원소의 포함여부를 결정했다면
#         if sm == S:
#             ans += 1
#         return
#     dfs(depth+1, sm+lst[depth]) # depth번째 원소를 포함하고 다음 번째 원소 고려
#     dfs(depth+1, sm)            # 포함하지 않고 다음 번째 원소 고려

# N, S = map(int, input().split())
# lst = list(map(int, input().split()))
# ans = 0
# dfs(0, 0)
# if S == 0:
#     ans -= 1 # 0인 경우 아무것도 고르지 않는 경우도 경우에 포함되므로 -1 빼줌
# print(ans)

# # 디버깅을 위해 lll 추가해봄 => 0일때, 아무것도 추가하지 않는 경우도 들어가므로, 빼줘야함
# # def dfs(depth, sm, lll):
# #     # depth: 몇번째 원소의 포함여부를 결정할 지 (종료조건의 N, depth 등을 잘 결정하자)
# #     # sm : 지금가지의 합
# #     global ans
# #     if depth == N: # 모든 원소의 포함여부를 결정했다면
# #         if sm == S:
# #             print(lll)
# #             ans += 1
# #         return
# #     dfs(depth+1, sm+lst[depth], lll+[lst[depth]]) # depth번째 원소를 포함하고 다음 번째 원소 고려
# #     dfs(depth+1, sm, lll)            # 포함하지 않고 다음 번째 원소 고려
# #
# # N, S = map(int, input().split())
# # lst = list(map(int, input().split()))
# # ans = 0
# # dfs(0, 0, [])
# # print(ans)



