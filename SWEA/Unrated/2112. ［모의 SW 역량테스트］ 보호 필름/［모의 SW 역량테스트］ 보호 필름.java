TC = int(input())


def check():
    for cc in range(C):
        seq = [0] * R
        seq[0] = 1
        for cr in range(1, R):
            if mmap[cr][cc] == mmap[cr - 1][cc]:
                seq[cr] = seq[cr - 1] + 1
            else:
                seq[cr] = 1

        if max(seq) < K:
            return False

    return True


def backtrack(depth, cnt):  # 현재 몇번째 행을 바꿀 차롄지, 현재까지 몇번 바꿨는지..
    global ans
    if cnt >= ans:  # 가지치기 
        return
    
    if check():     # 확인
        ans = min(ans, cnt)
        return

    if depth == R:  # R까지 도달했는데 안되는 경우 
        return 

    origin = mmap[depth][:]  # 깊은 복사

    backtrack(depth + 1, cnt)  # 그대로 진헹

    mmap[depth] = [0] * C
    backtrack(depth + 1, cnt + 1)  # 싹다 0으로 바꾸기

    mmap[depth] = [1] * C
    backtrack(depth + 1, cnt + 1)  # 싹다 1으로 바꾸기

    mmap[depth] = origin  # 원복

    return


def solve():
    backtrack(0, 0)


for tc in range(1, TC + 1):
    R, C, K = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(R)]
    ans = R # K<=R이므로 실패할 경우는 없음..
    solve()
    print(f"#{tc} {ans}")
