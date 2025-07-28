N = int(input())
lst = [int(input()) for _ in range(N)]
s = 0
nxt = 1 # 다음에 push할 수 (1,2,3... 순으로)
stk = []
# res = [] 결과 확인용
ans = []
while s < N:
    if len(stk) == 0:
        stk.append(nxt)
        ans.append("+")
        nxt += 1
    else:
        if stk[-1] < lst[s]:
            stk.append(nxt)
            ans.append("+")
            nxt += 1
        elif stk[-1] == lst[s]:
            stk.pop()
            # res.append(stk.pop()) 결과 확인용
            ans.append("-")
            s += 1
        elif stk[-1] > lst[s]:  # top of stack이 출력해야하는 수보다 크면 만들 수 없음 (출력해야하는 수는 밑에 깔려있으므로)
            ans = "NO"
            break
if ans == "NO" :
    print(ans)
else:
    print("\n".join(ans))
