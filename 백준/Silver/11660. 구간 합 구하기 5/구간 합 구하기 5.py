"""
[조건]
N*N전체 수의 개수
M 쿼리수

[목표]
시작점에서 끝점에 만드는 사각형 범위 합 구하기

[아이디어]
누적합 구해두고 진행
padding
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, N+1):
        arr[r][c] += arr[r-1][c] + arr[r][c-1] - arr[r-1][c-1]

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    print(arr[r2][c2] - (arr[r2][c1-1] + arr[r1-1][c2]) + arr[r1-1][c1-1])