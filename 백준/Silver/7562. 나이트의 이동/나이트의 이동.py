def solve():
    cnt = [[-1] * L for _ in range(L)]              # 도달할 수 없는 경우를 -1로 출력하기 위해 -1로 초기화
    cnt[sr][sc] = 0                                 # 자기자신까지 도달하는 것은 0번으로 가능
    q = []
    q.append((sr, sc))
    while q:
        cr, cc = q.pop(0)
        if cr == er and cc == ec:                       # 목표 좌표에 도착하면 break (return하지 않도록 주의)
            break
        for dr, dc in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]: # 나이트 이동 가능 영역
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < L and 0 <= nc < L:            # 범위 내에 있고
                if cnt[nr][nc] == -1:                  # 방문한 적이 없는 경우라면
                    cnt[nr][nc] = cnt[cr][cc] + 1
                    q.append((nr, nc))
    print(cnt[er][ec])


TC = int(input())
for _ in range(TC):
    L = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    solve()
