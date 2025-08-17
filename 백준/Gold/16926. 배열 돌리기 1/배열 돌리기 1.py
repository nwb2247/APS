"""
N, M <= 300
R <= 1000
N*M*R 90_000_000

new_arr에 값 넣으면서, 넣으려는 부분에 값 있으면 방향 전환,
네 방향 탐색이 끝나면 (cd == 4) sr, sc을 1씩 늘림
sr, sc에 값이 있으면 종료
"""
def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)

def rotate(arr):
    new_arr = [[0 for _ in range(M)] for _ in range(N)]
    sr, sc = 0, 0
    while new_arr[sr][sc] == 0:
        cr, cc, cd = sr, sc, 0
        while cd < 4:
            dr, dc = DS[cd]
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc) or new_arr[nr][nc] != 0:
                # 범위 밖이거나 이미 채웠다면 방향바꾸고 continue nr, nc를 다시 할당
                cd += 1
                continue
            new_arr[nr][nc] = arr[cr][cc]
            cr, cc = nr, nc
        # for l in new_arr:
        #     print(l)
        # print()
        sr += 1
        sc += 1
    return new_arr



N, M, R = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
DS = [(1,0), (0,1), (-1,0), (0,-1)] #하우상좌
for _ in range(R):
    ARR = rotate(ARR)
for lst in ARR:
    print(*lst)
