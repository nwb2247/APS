"""
경사로 길이 X, 높이 1

경사로 놓으려면 경사로의 길이만큼 지형높이가 연속되어야함

경사로를 놓아서 (여러개도 가능) 처음부터 쭉 끝까지 연결 시킬 수 있으면 카운트
(단 두개를 겹쳐서 놓을 수는 없음)


활주로를 건설할 수 있는 경우의 수
"""

N, X = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
ARR_T = [list(lst) for lst in zip(*ARR)]

def oob(r, c):
    return not (0<=r<N and 0<=c<N)

def check_row(cr, arr):
    cnt = 1
    cc = 1
    while cc < N:
        if arr[cr][cc] == arr[cr][cc-1]:
            cnt += 1
            cc += 1
        elif arr[cr][cc] - 1 == arr[cr][cc-1]: # 즉 더 커졌다면
            if cnt >= X:
                cnt = 1         # (D) 0이 아니라 1 (하나 세고 맨 아래줄에서 바로 cc += 1해주므로)
                cc += 1
            else:
                return False
        elif arr[cr][cc] == arr[cr][cc-1] - 1:  # 즉 더 작아졌다면
            for zc in range(cc, cc+X):
                if oob(cr, zc) or arr[cr][zc] != arr[cr][cc]:
                    return False
            cc = zc+1
            cnt = 0     # (D) 0이 아니라 1 (하나 세고 맨 아래줄에서 바로 cc += 1해주므로)
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

print(solve())


