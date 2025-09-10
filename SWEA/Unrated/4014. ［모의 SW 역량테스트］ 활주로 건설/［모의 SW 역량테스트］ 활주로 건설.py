"""
경사로 길이 X, 높이 1

경사로 놓으려면 경사로의 길이만큼 지형높이가 연속되어야함

경사로를 놓아서 (여러개도 가능) 처음부터 쭉 끝까지 연결 시킬 수 있으면 카운트
(단 두개를 겹쳐서 놓을 수는 없음)


활주로를 건설할 수 있는 경우의 수
"""

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def check_row(cr, arr):
    cc = 0  # 지금까지 확인한 것 중 마지막 인덱스
    cnt = 1 # 지금까지 연속 개수
    while True:
        nc = cc + 1 # 다음 인덱스
        if oob(cr, nc):
            break
        # [1] 같다면
        if arr[cr][nc] == arr[cr][cc]:
            cc = nc
            cnt += 1    # nc를 확인했으므로 1증가
        # [2] 더 커졌다면
        elif arr[cr][nc] == arr[cr][cc] + 1:
            if cnt >= X:    # 지금까지 연속수가 X와 같거나 더 길다면 OK
                cc = nc
                cnt = 1     # nc를 세어주고, 셌으므로 1로 초기화
            else:
                return False
        elif arr[cr][nc] == arr[cr][cc] - 1:  # 즉 더 작아졌다면
            for zc in range(nc, nc+X):
                if oob(cr, zc) or arr[cr][zc] != arr[cr][nc]:
                    return False
            cc = nc+X-1
            cnt = 0   
        else:
            return False

    return True


def solve():
    ans = 0
    for cr in range(N):
        if cr == 0:
            debug = 10
        # if tc == 6:
        #     print(cr, check_row(cr, ARR))
        if check_row(cr, ARR):
            ans += 1
    for cr in range(N):
        # if tc == 6:
        #     print(cr, check_row(cr, ARR_T))
        if check_row(cr, ARR_T):
            ans += 1
    return ans

TC = int(input())
for tc in range(1, TC+1):
    N, X = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    ARR_T = [list(lst) for lst in zip(*ARR)]
    # for a in arr:
    #     print(a)
    res = solve()
    print(f"#{tc} {res}")