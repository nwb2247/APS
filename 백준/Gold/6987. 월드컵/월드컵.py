def backtrack(depth):

    global found

    if depth == L: # 다 완성됐다면 일치하는지 확인
        bad = False
        for r in range(6):
            for c in range(3):
                if ARR[r][c] != RES[r][c]:
                    bad = True
                    break
            if bad:
                break
        else:
            found = True
        return

    x, y = VS[depth]

    for i in range(3):
        ARR[x][i] += 1
        ARR[y][2-i] += 1
        if ARR[x][i] <= RES[x][i] and ARR[y][2-i] <= RES[y][2-i]:
            backtrack(depth + 1)
        ARR[x][i] -= 1
        ARR[y][2-i] -= 1

VS = []
for i in range(6):
    for j in range(i+1, 6):
        VS.append((i, j))
L = len(VS)

ans = []
for tc in range(4):
    lst = list(map(int, input().split()))
    RES = [[0 for _ in range(3)] for _ in range(6)]
    for i in range(6):
        for j in range(3):
            RES[i][j] = lst[3*i + j]
    ARR = [[0 for _ in range(3)] for _ in range(6)]
    found = False
    backtrack(0)
    if found:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)