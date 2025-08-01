H = 1
C = 12
O = 16

lst = input().rstrip()

stk = []
for c in lst:
    if c == ")":
        sm = 0
        while stk[-1] != "(":
            sm += stk.pop()
        stk.pop() # 여는 괄호 꺼내기
        stk.append(sm)
    elif c == "H":
        stk.append(H)
    elif c == "C":
        stk.append(C)
    elif c == "O":
        stk.append(O)
    elif c == "(":
        stk.append("(")
    else: # 숫자라면
        stk.append(stk.pop()*int(c))
print(sum(stk))



"""
닫는 괄호 만나면 여는 괄호만날때까지 더해서 다시 append
숫자 만나면 마지막거 pop에서 곱해주고 append
"""