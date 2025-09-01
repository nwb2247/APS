"""
[요약평]
최근에 비슷한 문제를 풀어봤다면 더 긴장하고 집중해서 문제를 읽어야한다.
(비슷한 문제이지, 같은 문제가 아니기 때문)
(ex) 0 <= l < N 이 아닌 0 <= l < N 등 조건에서 파이가 발생)

[타임라인]
이해 및 구상 : 5분
1차 구현 : 18분 (melt까지)
1차 디버깅 : 3분 (N -> N+1 확인)
2차 구현 : 6분 (bfs)
2차 디버깅 : 2분 (bfs 시작 지점 조건)
-------
총 34분

[이해 및 구상]
-) 최근에 풀었던 문제와 유사하다보니, 조건이 달라졌음에도 이를 확인하지 못함 (이전 문제의 조건을 생각)

[구현]
+) 각 기능을 분리, 하나씩 구현할때마다 제대로 작동되는지 확인
+) 기준점 잡고 회전

[디버깅]

"""

# 손구상 내용
#
# 격자 나누고 90도 회전
# br, bc
# offest_c = 2**l + 1
#
# 주변에 얼음 3칸 이상 -> 그대로
# 주변에 얼음 3칸 미만 -> -1
# => narr 만들어야함
#
# 가장 큰 덩어리가 차지 하는 칸 BFS



from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


N, Q = map(int, input().split())
R, C = 2 ** N, 2 ** N       # 실수 줄이기 위해 R, C로 따로 만들어줌
arr = [list(map(int, input().split())) for _ in range(R)]
ops = list(map(int, input().split()))

# 0<=L<=N
# l에 따른 좌측상단 시작점
starts = [[] for _ in range(N + 1)]  # (D) N 아닌 N+1

for l in range(N + 1):  # (D) N 아닌 N+1
    for sr in range(0, R, 2 ** l):
        for sc in range(0, C, 2 ** l):
            starts[l].append((sr, sc))


def rotate(l):
    narr = [[0] * C for _ in range(R)]
    for sr, sc in starts[l]:
        br, bc = sr - 1, sc - 1     # (D) : 회전의 기준점 (회전해도 그대로 있는 점), 꼭 회전 대상 내 좌표가 아니어도 됨..., (정수로 잡는 것이 좋음)
        offset_c = 2 ** l + 1       # 회전 후 좌표 조정을 위해 더해줘야 하는 값
        for cr in range(sr, sr + 2 ** l):
            for cc in range(sc, sc + 2 ** l):
                dr, dc = cr - br, cc - bc   # cr, cc 가 기준점에서 얼마나 떨어져 있는지
                nr, nc = br + dc, bc - dr + offset_c    # nr, nc 회전 and 좌표 조정
                narr[nr][nc] = arr[cr][cc]

    return narr


def melt():
    narr = [[0] * C for _ in range(R)]
    for cr in range(R):
        for cc in range(C):
            if arr[cr][cc] == 0:
                continue
            cnt = 0
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc):
                    continue
                if arr[nr][nc] > 0:
                    cnt += 1
            if cnt >= 3:
                narr[cr][cc] = arr[cr][cc]
            else:
                narr[cr][cc] = arr[cr][cc] - 1  # 주변에 얼음있는곳이 3칸 미만이라면 1녹임

    return narr


def bfs():
    v = [[0] * C for _ in range(R)]
    mx = 0
    for sr in range(R):
        for sc in range(C):
            if arr[sr][sc] == 0:  # (D) 녹은 부분은 탐색안함
                continue
            if v[sr][sc] != 0:
                continue
            q = deque()
            q.append((sr, sc))
            v[sr][sc] = 1
            cnt = 0

            while q:
                cr, cc = q.popleft()
                cnt += 1

                for dr, dc in ds:
                    nr, nc = cr + dr, cc + dc
                    if oob(nr, nc):
                        continue
                    if arr[nr][nc] == 0:
                        continue
                    if v[nr][nc] != 0:
                        continue
                    v[nr][nc] = 1
                    q.append((nr, nc))
            # print((sr, sc, cnt))
            mx = max(mx, cnt)

    return mx


for l in ops:
    arr = rotate(l)
    arr = melt()
    # print(l)
    # for l in arr:
    #     print(l)

print(sum(map(sum, arr)))
print(bfs())
