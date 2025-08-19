"""
완전 탐색
매번 visited 새로 생성해서 같은 위치에 같은 방향으로 왔다면 성공 (갇힘)
중간에 나가버린다면 실패
100 * 4*100*100 => 가능 아ㅏㅏㅏㅏㅏㅏ
시계방향 90도 회전, 처음엔 오른쪽

문제 잘 읽기 -> 첫번째 열에만 둘 수 있음 아...
"""
def oob(r, c):
    return not (0<=r<N and 0<=c<M)


def check(sr, sc):
    visited = [[set() for _ in range(M)] for _ in range(N)] # 이미 그 좌표에서 그 방향으로 도착한 적이 있는지
    visited[sr][sc].add(0)  # 동쪽 방향 넣어줌
    cr, cc, cd = sr, sc, 0
    while True:
        if (sr, sc) == (0, 1):
            print(cr, cc, cd)
        dr, dc = DS[cd]
        nr, nc = cr+dr*ARR[cr][cc], cc+dc*ARR[cr][cc]
        if oob(nr, nc):
            return False
        cr, cc, cd = nr, nc, (cd+1)%4 # (도착시 다음 움직힐 방향을 검사해서 visited와 비교해야함)
        if cd in visited[cr][cc]:
            return True
        visited[cr][cc].add(cd)

N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
DS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상 (rc좌표)

ans = []
for sr in range(N):
    if check(sr, 0):
        ans.append((sr, 0))
print(len(ans))
for pos in ans:
    print(pos[0] + 1, end=" ")