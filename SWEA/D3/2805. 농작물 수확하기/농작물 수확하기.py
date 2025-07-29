# 7:46 ~ 7:51 5분

def solve(tc):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    d = N // 2
    sum = 0
    for r in range(N):
        for c in range(N):
            if abs(r - d) + abs(c - d) <= d:
                sum += arr[r][c]
    print(f"#{tc} {sum}")


def main():
    TC = int(input())
    for tc in range(1, TC + 1):
        solve(tc)


main()
