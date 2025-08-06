"""
[조건]
N<=11
음수를 나누는 경우엔 양수취하고 구한 몫을 음수로
주어지는 수는 모두 양수
사용가능한 덧셈뺄셈곱셈나눗셈 의 횟수 주어짐 (합은 N-1개)

[목표]
만들 수 있는 최소 최대값

[아이디어]
최소 최대 모두 구해야함,
남아있는 연산자 수를 이용해 넘기고 복원하기...

"""

def dfs(depth, val): # 연산된 수 갯수 (처음엔 1)
    global mx, mn
    if depth == N:
        # print(lll, val)
        mx = max(mx, val)
        mn = min(mn, val)
        return
    for i in range(4):
        if opnums[i] > 0:
            opnums[i] -= 1
            # dfs(depth+1, ops[i](val, lst[depth]), lll + [ccc[i], lst[depth]])
            dfs(depth + 1, ops[i](val, lst[depth]))
            opnums[i] += 1

N = int(input())
lst = list(map(int, input().split()))
opnums = list(map(int, input().split()))
ccc = ["+","-","*","/"]
ops = [lambda x, y: x + y,
       lambda x, y: x - y,
       lambda x, y: x * y,
       lambda x, y: x // y if x >= 0 else -((-x)//y)] # (debug : 부호좀 제대로 보자)

mn = 1000000000
mx = -1000000000

# dfs(1, lst[0], [lst[0]])
dfs(1, lst[0])
print(mx)
print(mn)
