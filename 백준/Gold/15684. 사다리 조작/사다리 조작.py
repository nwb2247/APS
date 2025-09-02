def check():     # 확인 완료
    res = []
    for i in range(1, C+1):
        cr, cnum = 0, i
        while cr < R:
            # 디버깅위 4개 다 확인
            if arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 0:
                pass
            elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 0:
                cnum -= 1
            elif arr[cr][cnum - 1] == 0 and arr[cr][cnum] == 1:
                cnum += 1
            elif arr[cr][cnum - 1] == 1 and arr[cr][cnum] == 1:
                print("error!!!!!")

            # 전부 내려가긴 해야함 (수정시 주의)
            cr += 1

        # print(i, cnum)
        if i != cnum:
            return False
    return True


def solve():
    global ans

    # 아무것도 추가안해도 가능이면? 0 만들고 return
    if check():
        ans = 0
        return

    # 1개
    for cr, cc in pos:
        arr[cr][cc] = 1
        if check():
            ans = 1
            return
        arr[cr][cc] = 0 # 원복
    
    # 2개
    for i in range(L):
        cri, cci = pos[i]
        arr[cri][cci] = 1
        for j in range(i+1, L):
            crj , ccj = pos[j]
            if arr[crj][ccj-1] != 0 or arr[crj][ccj+1] != 0:
                continue
            arr[crj][ccj] = 1
            if check():
                ans = 2
                return
            arr[crj][ccj] = 0
        arr[cri][cci] = 0 # 원복

    # 3개
    for i in range(L):
        cri, cci = pos[i]
        arr[cri][cci] = 1
        for j in range(i + 1, L):
            crj, ccj = pos[j]
            if arr[crj][ccj - 1] != 0 or arr[crj][ccj + 1] != 0:
                continue
            arr[crj][ccj] = 1
            for k in range(j+1, L):
                crk, cck = pos[k]
                if arr[crk][cck - 1] != 0 or arr[crk][cck + 1] != 0:
                    continue
                arr[crk][cck] = 1
                if check():
                    ans = 3
                    return
                arr[crk][cck] = 0
            arr[crj][ccj] = 0
        arr[cri][cci] = 0  # 원복

C, K, R = map(int, input().split())

# [0] 사다리 표현
arr = [[0]*(C+1) for _ in range(R)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b] = 1

# for l in arr:
#     print(l)

# [1] pos 일단 가능한 점들 넣음
pos = []
for zr in range(R):
    for zc in range(1, C): # 양끝은 포함하면 안됨
        if arr[zr][zc] == 0 and arr[zr][zc-1] == 0 and arr[zr][zc+1] == 0:
            pos.append((zr, zc))
L = len(pos) # pos의 크기

ans = -1 # 로 두고 1개 2개 3개 를 차례로 확인해봄 solve() return 이용해 빠른 탈출
solve()
print(ans)



