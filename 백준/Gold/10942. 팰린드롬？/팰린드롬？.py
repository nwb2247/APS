"""
[조건]
수열 크기 N <= 2000
쿼리 수 M <= 1_000_000

수열은 1번부터 시작

[목표]
팰린드롬인지 아닌지 출력

[접근]
N은 작고 M은 상대적으로 크기때문에 전처리 필요
각 인덱스에 대해서 팰린드롬의 중앙값이 될 때 최대 길이를 저장
(길이가 홀수인경우 짝수인경우(는 왼쪽 중앙) 두개 배열로 관리)

O(N^2 + M)
"""
import sys

input = sys.stdin.readline

N = int(input())
lst = [-1] + list(map(int, input().split()))
M = int(input())
queries = [tuple(map(int, input().split())) for _ in range(M)]

mx_odd = [0]*(N+1)
mx_even = [0]*(N+1)

for i in range(1, N+1):
    s, e = i, i
    lng = 1
    while s-1>=1 and e+1<=N and lst[s-1] == lst[e+1]:
        lng += 2
        s -= 1
        e += 1
    mx_odd[i] = lng
    s, e = i, i+1
    if i+1>N or lst[s] != lst[e]:
        continue
    lng = 2
    while s - 1 >= 1 and e + 1 <= N and lst[s - 1] == lst[e + 1]:
        lng += 2
        s -= 1
        e += 1
    mx_even[i] = lng

for s, e in queries:
    lng = e-s+1
    m = (s+e)//2
    if lng%2 == 1:
        print(int(mx_odd[m] >= lng))
    else:
        print(int(mx_even[m] >= lng))
