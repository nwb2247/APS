"""
[조건]
3<=N<=16 한 변 길이
각 놓인 방향마다 다음 진행가능한 방향이 다름
각 방향에 대해 꼭 빈칸이어야하는 부분이 존재 (색깔로 표시되어있음)

[목표]
마지막 위치까지 갈 수 있는 방법의 갯수 출력

[접근]
백트래킹으로 풀면 시간 초과 O(3^(N+N)) (가로 세로)
경로의 개수를 세는 것이므로 DP를 사용해보자
각 좌표마다 놓인 방향에 대한 방법 3가지를 기록
진행방향 특성상 위나 오른쪽 위 대각으로 진행하지 않으므로
DP 기록시 0행부터 오른쪽방향으로 내려와 기록해도됨

[주의사항]
벽으로 이동 불가 뿐만이나라 대각선의 경우 더 넓은 범위에 벽이 있으면 안됨

[엣지 케이스]

"""
N = int(input())

ds = [[(0,1),(1,1),(0,0)],          # 0: 오른쪽, 1:오른쪽아래, 2:아래 , (0,0)이면 패스하도록
      [(0,1),(1,1),(1,0)],          # [i][j] : i 현재 방향 j다음 위치에서의 방향
      [(0,0),(1,1),(1,0)]]

free = [[(0,0)],                    # 각 방향에 대해 벽이 없어야 하는 부분
        [(0,0),(-1,0),(0,-1)],
        [(0,0)]]

arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 초기 상태 설정
DP[0][1][0] = 1

for cr in range(N):
    for cc in range(N):
        if arr[cr][cc] == 1:
            continue
        for i in range(3):      # 각 놓인 방향 마다
            for j, d in enumerate(ds[i]): # 0, [(0,1),(1,1),(0,0)]  각 앞으로의 방향에 대해
                if d == (0,0): continue
                dr, dc = d
                nr, nc = cr + dr, cc + dc
                if 0<=nr<N and 0<=nc<N and arr[nr][nc] != 1: # 범위 내에 있고 벽이 아니라면 기록
                    for fr, fc in free[j]:
                        if not (0 <= nr + fr < N and 0 <= nc + fc < N and arr[nr + fr][nc + fc] != 1):
                            break
                    else:
                        DP[nr][nc][j] += DP[cr][cc][i]     # 방법의 수를 더해줌

# for lst in DP:
#     print(lst)

print(sum(DP[N-1][N-1]))


