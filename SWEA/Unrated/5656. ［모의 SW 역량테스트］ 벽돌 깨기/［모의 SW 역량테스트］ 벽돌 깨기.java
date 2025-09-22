"""
폭발은 연쇄적으로 동시에 처리

연쇄 작용 다 끝나면 그 때 중력 처리
해당 길이 보면서, 방문하지 않은 경우 q에 넣고 방문한 경우라도 다음것을 확인... (멈추면 안됨)

해당 위치에 벽돌이 없는 경우더라도 일단 떨어뜨리고, 없으면 아무것도 하지 않기??
"""

from collections import deque


def oob(r, c):
    return not (0 <= r < R and 0 <= c < C)


def explode(sr, sc, arr):
    v = [[0 for _ in range(C)] for _ in range(R)]
    q = deque()
    v[sr][sc] = 1
    q.append((sr, sc))

    tmp = []
    while q:
        cr, cc = q.popleft()
        tmp.append((cr, cc))

        for cd in range(4):  # 각 방향에 대해서
            dr, dc = ds[cd]
            for l in range(arr[cr][cc]):  # 벽돌에 적혀있는 숫자 - 1 만큼 (I) 각 방향 -> 각 길이 순으로 봐야함 (길이 -> 방향 XXX)
                nr, nc = cr + dr * l, cc + dc * l
                if oob(nr, nc):  # 벽밖으로 나가면 그 이상은 못감
                    break
                if arr[nr][nc] == 0 or v[nr][nc] != 0:  # 빈칸이거나 이미 방문한 곳이라면 다음 l로 넘어감
                    continue
                v[nr][nc] = 1
                q.append((nr, nc))

    # 디버깅용
    # z = [[0 for _ in range(R)] for _ in range(C)]
    # for zr, zc in tmp:
    #     z[zr][zc] += 1
    # for l in z:
    #     print(l)
    
    # 0으로 만들어줌
    for cr, cc in tmp:
        arr[cr][cc] = 0

def gravity(arr):
    for cc in range(C):
        stk = []
        for cr in range(R):
            if arr[cr][cc] != 0:
                stk.append(arr[cr][cc])
        for cr in range(R-1, -1, -1):
            if stk:
                arr[cr][cc] = stk.pop()
            else:
                arr[cr][cc] = 0

def backtrack(depth, arr):  # 지금까지 몇번 떨궜는지, 점수
    global ans

    if depth == K:
        cnt = 0
        for cr in range(R):
            for cc in range(C):
                if arr[cr][cc] != 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    for sc in range(C):
        narr = [lst[:] for lst in arr]
        for sr in range(R):     # 벽돌이 존재하는 가장 윗쪽을 확인
            if narr[sr][sc] == 0:   # 비었다면 넘어감
                continue
            # 벽돌을 마주했다면 처리하고 하부재귀 호출
            explode(sr, sc, narr)
            gravity(narr)
            backtrack(depth + 1, narr)
            break # 맨 위만 보므로 바로 break
        else:  # 벽돌이 없었다면 (break되지 않았다면) 그냥 narr 건드리지 않고 넘김
            backtrack(depth + 1, narr)

    return


def solve():
    backtrack(0, mmap)

    # explode(2, 2, mmap)
    # gravity(mmap)
    # for l in mmap:
    #     print(*l)

    return


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 0상 1하 2좌 3우

TC = int(input())
for tc in range(1, TC + 1):

    K, C, R = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(R)]

    ans = R * C
    solve()
    print(f"#{tc} {ans}")
