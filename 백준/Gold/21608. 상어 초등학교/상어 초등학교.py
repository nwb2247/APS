ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def oob(r, c):
    return not (0<=r<N and 0<=c<N)


def seat(num, sset):
    pos = []
    mx = -1
    for cr in range(N):
        for cc in range(N):
            if arr[cr][cc] != 0:
                continue
            cnt = 0
            for dr, dc in ds:
                nr, nc = cr+dr, cc+dc
                if oob(nr, nc):
                    continue
                if arr[nr][nc] in sset:
                    cnt += 1
            if cnt > mx:
                pos = [(cr, cc)]
                mx = cnt
            if cnt == mx:
                pos.append((cr, cc)) # nr아닌 cr임
    # print(mx)
    # print(pos)

    if len(pos) == 1:
        cr, cc = pos[0]     # pos[0]에서 가져와야함
        arr[cr][cc] = num
        return

    # 2단계
    pos2 = []            # 이름을 pos로 하면 위와 겹쳐서 안됨...
    mx = -1
    for cr, cc in pos:
        cnt = 0
        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] == 0:
                cnt += 1
        if cnt > mx:
            pos2 = [(cr, cc)]
            mx = cnt
        if cnt == mx:
            pos2.append((cr, cc))

    if len(pos2) == 1:
        cr, cc = pos2[0]  # pos[0]에서 가져와야함
        arr[cr][cc] = num
        return

    # 3단계

    # print(pos2)

    pos2.sort(key=lambda x:(x[0], x[1]))
    cr, cc = pos2[0]
    arr[cr][cc] = num
    return


N = int(input())
arr = [[0]*N for _ in range(N)]
d = dict()
for _ in range(N*N): # 1부터 시작해야함
    num, *(fav) = map(int, input().split())
    sset = set(fav)
    d[num] = sset

    seat(num, sset)
    # for l in arr:
    #     print(l)
    # print()

ans = 0
for cr in range(N):
    for cc in range(N):
        cnt = 0
        num = arr[cr][cc]
        sset = d[num]
        for dr, dc in ds:
            nr, nc = cr+dr, cc+dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] in sset:
                cnt += 1
        if cnt == 0:
            ans += 0
        elif cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)
