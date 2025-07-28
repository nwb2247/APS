"""
스택으로 풀어보기
top of stk 이 무얼 의미하는지 생각하자
왼쪽부터 하나씩 추가할 때, 추가하는 것이 앞의 것들을 가리는지 생각해보자.
가려지는 것이 없을 때까지 pop
"""

N = int(input())
stk = []
for _ in range(N):
    new = int(input())
    while len(stk) != 0 and stk[-1] <= new: # 가려지는 것이 없을 때까지 pop
        stk.pop()
    stk.append(new)
print(len(stk))
