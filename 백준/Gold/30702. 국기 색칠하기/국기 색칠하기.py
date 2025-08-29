"""
A에서 같은 영역 선택해 B[sr][sc]와 일치하는지 확인
"""

from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
B = [list(input()) for _ in range(R)]

def oob(r, c):
    return not (0<=r<R and 0<=c<C)

def solve():    # 답 아니면 바로 출력 위해 함수화

    v = [[0]*C for _ in range(R)]
    for sr in range(R):
        for sc in range(C):
            if v[sr][sc] == 1:
                continue
            a = A[sr][sc]
            b = B[sr][sc]

            q = deque()

            v[sr][sc] = 1
            q.append((sr, sc))

            while q:
                cr, cc = q.popleft()
                if B[cr][cc] != b:
                    print("NO")
                    return

                for dr, dc in ds:
                    nr, nc = cr+dr, cc+dc
                    if oob(nr, nc):
                        continue
                    if A[nr][nc] != a:
                        continue
                    if v[nr][nc] != 0:
                        continue
                    v[nr][nc] = 1
                    q.append((nr, nc))

    print("YES")

solve()



