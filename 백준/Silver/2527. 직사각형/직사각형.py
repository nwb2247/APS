
"""
변수명 내가 알아보기 쉽게 바꾸기 (l1 : 첫번째 직사각형의 left 좌표(x1))
분기를 여러번 하는 경우 조건에 의해 확실하게 분기가 되는지 생각해보기

가장 쉬운 겹치지 않는 경우부터 분기
l2 == r1 or r2 == l1 or d2 == u1 or u2 == d1 (선으로 겹치는) 경우
점으로 겹치는 경우를 더 큰 범위로 포함하므로, 
점으로 겹치는 경우를 먼저 걸러낸다.

가장 까다롭게 느껴지는 조건인 면으로 겹치는 경우를 else로 처리
"""

for _ in range(4) :
    l1, d1, r1, u1, l2, d2, r2, u2 = map(int, input().split())
    if l2 > r1 or r2 < l1 or d2 > u1 or u2 < d1:
        print("d")
    elif ((l1, d1) == (r2, u2) or (r1, d1) == (l2, u2)
          or (r1, u1) == (l2, d2) or (l1, u1) == (r2, d2)):
        print("c")
    elif l2 == r1 or r2 == l1 or d2 == u1 or u2 == d1:
        print("b")
    else:
        print("a")