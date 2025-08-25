from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def check(cr, cc, nr, nc):
    return L <= abs(arr[cr][cc] - arr[nr][nc]) <= R


day = 0
while True:
    day += 1
    visited = [[0] * N for _ in range(N)]
    cnt = 0 # (1이면 break)
    for sr in range(N):
        for sc in range(N):
            if visited[sr][sc] == 0:
                q = deque()
                cnt += 1
                pos = []

                visited[sr][sc] = 1
                q.append((sr, sc))
                pos.append((sr, sc)) # (D) pos에도 넣어줘야함



                while q:
                    cr, cc = q.popleft()

                    for dr, dc in DS:
                        nr, nc = cr+dr, cc+dc
                        if oob(nr, nc):
                            continue
                        if visited[nr][nc] == 0 and check(cr, cc, nr, nc):
                            visited[nr][nc] = 1
                            pos.append((nr, nc))
                            q.append((nr, nc))

                sm = sum(map(lambda p:arr[p[0]][p[1]], pos))
                for r, c in pos:
                    arr[r][c] = sm//(len(pos))

    if cnt == N*N: # (D) 더 이상 두 국가가 연합을 이루지 않는 경우로 해야함 (처음에는 잘못생각해서 1로 둠;;;)
        break

print(day-1)


