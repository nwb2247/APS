"""
공기와 맞닿아 있는 광물 하나 골라 채굴 가능

-> 좌상우를 0으로 패딩, 맨 밑을 1000001으로 패딩 (최소가 0 최대가 1000000)
단, 0인 경우는 광물 카운트 하면안됨

이분 탐색과 같이 사용

(D) 또 10**6인데 100000 ;;
"""

from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def oob(r, c):
    return not (0<=r<R+2 and 0<=c<C+2)

R, C, K = map(int, input().split())
arr = [[0]*(C+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(R) ] + [[1000001]*(C+2)]



def check(d):
    cnt = 0
    q = deque()
    v = [[0 for _ in range(C+2)] for _ in range(R+2)]
    q.append((0, 0))
    v[0][0] = 1

    while q:
        cr, cc = q.popleft()

        if arr[cr][cc] > 0:
            # print(cr, cc)
            cnt += 1

        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] > d:
                continue
            if v[nr][nc] == 1:
                continue
            v[nr][nc] = 1
            q.append((nr, nc))

    return cnt

check(2)

left = 0
right = 1000000
ans = right
while left<=right:
    mid = (left+right)//2
    if check(mid) >= K:
        ans = mid
        right = mid-1
    else:
        left = mid+1

print(ans)


