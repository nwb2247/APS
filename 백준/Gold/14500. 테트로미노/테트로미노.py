"""

DFS 응용 -> "지금까지 추가한 것들과 맞닿아 있는 모든 것들을 후보로 넣으려면?!"

폴리오미노, N개의 정사각형들이 인접하게 붙어있어야함

[1]
이를 위해 현재까지 포함된 블록의 리스트를 유지한채로
그 안에서 하나씩 꺼내 인접한 곳에 넣을 것이 있는지 확인하기!!!

[2]
[1]을 수행하기 위해 시작점을 정해서 들어가는데
일단 한점에서 돌리면
그 점에서 들어갈 모든 경우의 수를 탐색하기 때문에
다음번엔 그 점이 포함되는 경우는 고려할 필요가 없음
    => 시작점에 대해서는 visited를 원상복구하지 않아도 됨
"""
def oob(r, c):
    return not (0<=r<N and 0<=c<M)


def backtrack(depth, sm):
    global ANS

    if sm + (K-depth)*MX <= ANS: # 가지치기 (지금까지 합한거 + 나머지를 최대로 채워도 ANS가 갱신되지 않는다면)
        return

    if depth == K:  # 종료 조건 (테트로미노 K:4)
        ANS = max(ANS, sm)
        return

    for tr, tc in CONTAINED[:depth]: # (depth까지가 현재까지 블록에 넣은 테트로임)
        for dr, dc in DS:
            nr, nc = tr+dr, tc+dc
            if oob(nr, nc):
                continue

            if VISITED[nr][nc] == 0:
                VISITED[nr][nc] = 1
                CONTAINED[depth] = (nr, nc)
                backtrack(depth + 1, sm + ARR[nr][nc])
                VISITED[nr][nc] = 0


DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

K = 4
N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
VISITED = [[0 for _ in range(M)] for _ in range(N)]
CONTAINED = [() for _ in range(K)] # "K개의 폴리오미노"로도 확장 가능
MX = max(map(max, ARR)) # 가지치기를 위해 ARR에서 가장 큰 것을 찾음

ANS = 0

for sr in range(N):
    for sc in range(M):
        VISITED[sr][sc] = 1
        CONTAINED[0] = (sr, sc)
        backtrack(1, ARR[sr][sc]) # depth, sm
        # sr, sc에 대해 모든 경우의 수를 다 확인하므로 더 이상 sr, sc가 들어갈 일은 없음
        # 따라서 VISITED[sr][sc] = 0 의 원상복구 안하는게 더 빠름

print(ANS)


# --------- 1번째 아이디어 : 모양의 경우의 수 만들어 완전탐색 ---------
# """
# 회전 4 * 대칭 3 가지 * 나의 위치 4가지 * 테트로노미노 모양 5 => 160가지
# (D) 생각해보면 나의 위치 4는 곱할 필요가 없음
# why? 어차피 다른 점에서 시작했을떄 내가 포함되는 경우가 있기때문 => 40가지면 충분
# N*M = 4*500
# 완탐 시간 OK
#
# 좌측 상단을 0, 0으로 두고, 대칭 회전 시켜서 8개 모양만들기,
# 각 모양에서 한점을 잡았을때 나머지의 상대위치 변환 시켜주는 함수
# 4개가 전부 범위에서 벗어나는지 아닌지 확인
# """
# tetros = [((0, 0), (0, 1), (0, 2), (0, 3)), # 중복 처리 위해 tuple로 받음 (이중 튜플도 set에 넣을 수 있음)
#           ((0, 0), (1, 0), (2, 0), (2, 1)),
#           ((0, 0), (1, 0), (1, 1), (2, 1)),
#           ((0, 0), (0, 1), (0, 2), (1, 1)),
#           ((0, 0), (0, 1), (1, 0), (1, 1))]
# # 5개
#
# # 회전 (180도)
# new = []
# for t in tetros:
#     tmp = tuple([(c, r) for r, c in t])
#     new.append(tmp)
# tetros += new
# # 10개 (180도)
#
# # 대칭
# new = []
# for t in tetros:
#     tmp = tuple([(-r, c) for r, c in t])
#     new.append(tmp)
#     tmp = tuple([(r, -c) for r, c in t])
#     new.append(tmp)
#     tmp = tuple([(-r, -c) for r, c in t])
#     new.append(tmp)
# tetros += new
# # 40개
# sset = set(tetros)
# # len(sset) # 36개
# tetros = list(sset)
# # for t in tetros:
# #     print(t)
#
#
# # new = []                           (D) 어차피 다른 점 시작에서 내가 포함될 수 있으므로 이부분은 굳이 X
# # for t in tetros:
# #     for br, bc in t:
# #         tmp = []
# #         for r, c in t:
# #             tmp.append((r-br, c-bc))
# #         new.append(tuple(tmp))
# # tetros = new # (new에 tetro가 포함되어있음)
# # # 160개
#
# N, M = map(int, input().split())
# ARR = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# for cr in range(N):
#     for cc in range(M):
#         for tetro in tetros:
#             sm = 0
#             for tr, tc in tetro:
#                 nr, nc = cr+tr, cc+tc
#                 if not (0<=nr<N and 0<=nc<M):
#                     break # 이 테트로는 망함, sm 쓸모 없음
#                 sm += ARR[nr][nc]
#             else:
#                 # break 되지 않았다면 범위내 있는 테트로 이므로 ans에 반영
#                 ans = max(ans, sm)
# print(ans)
#
