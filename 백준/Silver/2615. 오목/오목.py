ds = [[-1, 1], [0, 1], [1, 1], [1, 0]] # 시작점이 맨 왼쪽이 되도록


def check(sr, sc, dr, dc):            # 해당 시작점, 해당 방향에서 오목이 있는지 확인
    global ans, ans_pos

    tr, tc = sr-dr, sc-dc             # 반대편에서도 이어지면 종료 (왼쪽 방향으로만 이어지도록)
    if 0 <= tr < L and 0 <= tc < L:
        if arr[sr][sc] == arr[tr][tc]:
            return

    l = 1
    nr, nc = sr + l * dr, sc + l * dc
    while 0 <= nr < L and 0 <= nc < L:      # 연속된 색의 길이를 구함
        if arr[sr][sc] != 0 and arr[sr][sc] == arr[nr][nc]:
            l += 1
            nr, nc = sr + l * dr, sc + l * dc
        else:
            break
    if l == 5:              # 5라면 ans, ans_pos를 갱신
        ans = arr[sr][sc]
        ans_pos = [sr+1, sc+1]
        return

L = 19
arr = [list(map(int, input().split())) for _ in range(L)]
ans = 0
ans_pos = [0, 0]
for sr in range(L):
    for sc in range(L):
        for dr, dc in ds:
            check(sr, sc, dr, dc)
if ans == 0:
    print(0)
else:
    print(ans)
    print(*ans_pos)



