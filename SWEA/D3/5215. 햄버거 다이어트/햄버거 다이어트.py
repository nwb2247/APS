"""
[조건]
N <= 20

[목표]
햄버거 재료 점수, 칼로리 제공
정해진 칼로리 "이하"의 조합에서
가장 선호하는 햄버거 조합 찾기 => 점수 출력

[아이디어]
각 재료마다 넣을지 말기 확인
2^20
칼로리를 기준으로 가지치기 수행


"""


def dfs(depth, cal, score):
    # 재료 인덱스 (넣을지 말지 결정할) / 칼로리합 / 맛점수합
    global ans

    if cal > K:  # (가지치기)
        return

    if depth == N and cal <= K:  # (종료조건)
        ans = max(ans, score)
        return

    dfs(depth + 1, cal + arr[depth][1], score + arr[depth][0])
    dfs(depth + 1, cal, score)


TC = int(input())

for tc in range(1, TC + 1):
    N, K = map(int, input().split())  # 재료 수 , 칼로리 제한
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    # [0] : 맛점수 / [1]: 칼로리
    ans = 0
    dfs(0, 0, 0)
    print(f"#{tc} {ans}")
