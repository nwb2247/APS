"""
[조건]
3*2^k (3, 6, 12, 24, 48...)

[목표]
별찍기

[접근]
3짜리 만들어놓고 확장시키기
"""
import math
N = int(input())
num = int(math.log(N//3, 2))

piece = [[' ',' ','*',' ',' '],
         [' ','*',' ','*',' '],
         ['*','*','*','*','*']]

for i in range(num):
    top = [[' '] * (3*2**i) + lst + [' '] * (3*2**i) for lst in piece]
    bottom = [lst + [' '] + lst for lst in piece]
    piece = top+bottom


for lst in piece:
    print("".join(lst))

