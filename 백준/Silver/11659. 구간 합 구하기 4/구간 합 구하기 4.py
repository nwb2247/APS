"""
[조건]
N전체 수의 개수
M 쿼리수

[목표]
i ~ j 번째의 합 구하기

[아이디어]
누적합 구해두고 cumsum[j]-cumsum[i-1]
i, j 1부터 시작하므로 padding
1번째 부터 j번째 -> cumsum[j]-cumsum[0]으로 함께 일반화 가능
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    lst[i] += lst[i-1]
for _ in range(M):
    i, j = map(int, input().split())
    print(lst[j]-lst[i-1])