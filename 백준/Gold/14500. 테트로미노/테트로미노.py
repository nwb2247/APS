"""
DFS 응용 - "특정한 수의" + "서로 인접한 칸으로 구성된" 블럭
    [1] 시작점을 지정해서 BFS 진행
    [2] 시작점에 대해선 방문 원상복구 안함
        시작점에 대해서 가능한 모든 경우를 다 따져본것 이므로 굳이 다시 넣을 필요가 없음
        즉 시작점이 포함되는 것은 이미 다 따져본 것이고, 앞으로 탐색할 것에 대해서는 시작점이 들어가지 않음
    [3] 단, 한 시작점에 대해서는 여러개가 들어갈 수는 있음
        따라서 "경우의 수"를 따지는 경우엔
        정렬 -> set 연산 위한 튜플화 -> 중복 제거 의 처리가 필요함

(경우의 수 X)
for sr in
    for sc in
        visited[sr][sc] = 1
        backtrack(depth, [(sr, sc)]
        # 원상 복구 X

def backtrack(depth, contained):
    if depth == K: # 정해진 블록의 수
        (contained 에 대한 정답 처리)
        return

    for cr, cc in contained:
        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) : contained
            if visited[nr][nc] == 0:
                visited[cr][cc] = 1
                backtrack(depth + 1, contained + [(nr, nc)]
                visited[cr][cc] = 0

--------------------------------------------------

(경우의 수 O) ### : 추가된 부분
cnt = 0 # 모든 경우의 수
for sr in
    for sc in
        ### blocks = []
        # 한 시작점에 대해선 중복이 있을 수 있기 때문에
        # 튜플화 하여 넣고 set 만들어서 고유한 것만 남기기
        visited[sr][sc] = 1
        backtrack(depth, [(sr, sc)]
        # 원상 복구 X

        ### cnt += len(set(blocks))

def backtrack(depth, contained):
    if depth == K: # 정해진 블록의 수
        ### blocks.append(tuple(sorted(contained)))
        # 정렬하고, 튜플만들고 blocks에 넣기
        return

    for cr, cc in contained:
        for dr, dc in DS:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) : contained
            if visited[nr][nc] == 0:
                visited[cr][cc] = 1
                backtrack(depth + 1, contained + [(nr, nc)]
                visited[cr][cc] = 0

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