"""
회전 4 * 대칭 3 가지 * 나의 위치 4가지 * 테트로노미노 모양 5 => 160가지
(D) 생각해보면 나의 위치 4는 곱할 필요가 없음
why? 어차피 다른 점에서 시작했을떄 내가 포함되는 경우가 있기때문
N*M = 4*500
완탐 시간 OK

좌측 상단을 0, 0으로 두고, 대칭 회전 시켜서 8개 모양만들기,
각 모양에서 한점을 잡았을때 나머지의 상대위치 변환 시켜주는 함수
4개가 전부 범위에서 벗어나는지 아닌지 확인
"""
tetros = [((0, 0), (0, 1), (0, 2), (0, 3)), # 중복 처리 위해 tuple로 받음 (이중 튜플도 set에 넣을 수 있음)
          ((0, 0), (1, 0), (2, 0), (2, 1)),
          ((0, 0), (1, 0), (1, 1), (2, 1)),
          ((0, 0), (0, 1), (0, 2), (1, 1)),
          ((0, 0), (0, 1), (1, 0), (1, 1))]
# 5개

# 회전 (180도)
new = []
for t in tetros:
    tmp = tuple([(c, r) for r, c in t])
    new.append(tmp)
tetros += new
# 10개 (180도)

# 대칭
new = []
for t in tetros:
    tmp = tuple([(-r, c) for r, c in t])
    new.append(tmp)
    tmp = tuple([(r, -c) for r, c in t])
    new.append(tmp)
    tmp = tuple([(-r, -c) for r, c in t])
    new.append(tmp)
tetros += new
# 40개
sset = set(tetros)
# len(sset) # 36개
tetros = list(sset)
# for t in tetros:
#     print(t)


# new = []                           (D) 어차피 다른 점 시작에서 내가 포함될 수 있으므로 이부분은 굳이 X
# for t in tetros:
#     for br, bc in t:
#         tmp = []
#         for r, c in t:
#             tmp.append((r-br, c-bc))
#         new.append(tuple(tmp))
# tetros = new # (new에 tetro가 포함되어있음)
# # 160개

N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for cr in range(N):
    for cc in range(M):
        for tetro in tetros:
            sm = 0
            for tr, tc in tetro:
                nr, nc = cr+tr, cc+tc
                if not (0<=nr<N and 0<=nc<M):
                    break # 이 테트로는 망함, sm 쓸모 없음
                sm += ARR[nr][nc]
            else:
                # break 되지 않았다면 범위내 있는 테트로 이므로 ans에 반영
                ans = max(ans, sm)
print(ans)

