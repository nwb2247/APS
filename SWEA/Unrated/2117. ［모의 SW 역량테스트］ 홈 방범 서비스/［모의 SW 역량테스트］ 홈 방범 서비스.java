def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def inside(cr, cc, br, bc, l):
    return abs(cr-br) + abs(cc-bc) <= l

def solve():
    global ans
    for br in range(N):
        for bc in range(N):
            for k in range(2 * N):
                cost = k * k + (k - 1) * (k - 1)
                cnt = 0
                l = k - 1
                for cr in range(br - l, br + l + 1):
                    for cc in range(bc - l, bc + l + 1):
                        # 격자 밖이거나, 맨해튼 내에 있는게 아니거나, 집이 없다면 넘어감
                        if oob(cr, cc) or not inside(cr, cc, br, bc, l) or mmap[cr][cc] == 0:
                            continue
                        cnt += 1
                if cnt * M - cost >= 0:  # 손해를 보지 않는거니까 0도 가능
                    ans = max(ans, cnt)

    return


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(N)]


    ans = 0
    solve()
    print(f"#{tc} {ans}")
