N = int(input())
lst = [0] + list(map(int, input().split()))
stk = []
ans = [0]*(N+1)
for i in range(N,0,-1):
    while len(stk) != 0 and lst[stk[-1]] < lst[i]:
        ans[stk.pop()] = i
    stk.append(i)
print(*ans[1:])