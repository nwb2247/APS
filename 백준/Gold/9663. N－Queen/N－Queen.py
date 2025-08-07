"""
[조건]
N<=15

[목표]
퀸 N개가 서로 공격할 수 없게 놓는 경우

[접근]
각 행마다 퀸을 배치할 열을 선택한다
이 때 열, 우하향 대각, 우상향 대각의 방문 배열을 모두
우하향 차가 -(N-1) ~ (N-1) -> 2N-2짜리 배열 만들기 (N-1 베이스 업) => 파이썬 음수 인덱싱 가능하므로 베이스 업 하지 않아도됨
우상향 합이 0 ~ 2N-2
"""

def dfs(depth):  # depth 열의 위치를 결정해야하는 현재 행 인덱스
    global ans

    if depth == N:
        ans += 1
        return

    for c in range(N):
        # visited_down (우하향) 파이썬 음수 인덱싱 가능하므로 베이스 업 하지 않아도됨
        if visited_c[c] == 0 and visited_down[depth - c] == 0 and visited_up[depth + c] == 0:
            visited_c[c] = visited_down[depth - c] = visited_up[depth + c] = 1
            dfs(depth + 1)
            visited_c[c] = visited_down[depth - c] = visited_up[depth + c] = 0


# def dfs(depth):  # depth 열의 위치를 결정해야하는 현재 행 인덱스
#     global ans
#
#     if depth == N:
#         ans += 1
#         return
#
#     for c in range(N):
#         if visited_c[c] == 0 and visited_down[depth - c + N - 1] == 0 and visited_up[depth + c] == 0:
#             visited_c[c] = visited_down[depth - c + N - 1] = visited_up[depth + c] = 1
#             dfs(depth + 1)
#             visited_c[c] = visited_down[depth - c + N - 1] = visited_up[depth + c] = 0


N = int(input())
visited_c = [0] * N
visited_down = [0] * (2 * N - 1)  # 우하향
visited_up = [0] * (2 * N - 1)  # 우상향
ans = 0

dfs(0)
print(ans)
