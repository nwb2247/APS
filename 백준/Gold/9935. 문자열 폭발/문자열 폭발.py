st = list(input().rstrip())
stk = []
pat = list(input().rstrip()) # stk과 비교위에 list로 받아옴
for c in st:
    stk.append(c)
    if len(stk) >= len(pat) and stk[-1] == pat[-1]:     # 끝 글자가 같다면
        if stk[-len(pat):] == pat:                      
        # 스택의 끝부분과 패턴이 일치하는지 확인 
        # (단, stk의 길이가 패턴보다 크거나 같은지 확인 필요)
            for _ in range(len(pat)):   # 패턴 개수만큼 popo
                stk.pop()
if len(stk) != 0:
    print("".join(stk))
else:
    print("FRULA")