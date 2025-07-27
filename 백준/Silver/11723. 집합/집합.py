import sys
input = sys.stdin.readline

S = [False]*21
N = int(input())
for _ in range(N):
    op = input().split()
    if op[0] == "add" and not S[int(op[1])]:
        S[int(op[1])] = True
    elif op[0] == "remove" and S[int(op[1])]:
        S[int(op[1])] = False
    elif op[0] == "check":
        if S[int(op[1])]:
            print(1)
        else:
            print(0)
    elif op[0] == "toggle":
        S[int(op[1])] = not S[int(op[1])]
    elif op[0] == "all":
        for i in range(1, 21):
            S[i] = True
    elif op[0] == "empty":
        for i in range(1, 21):
            S[i] = False
    else:
        pass
        # 위에서 add, remove의 조건에 의해 아무것도 수행되지 않는 경우 이 라인이 수행
        # 따라서 empty를 else로 처리하면 문제가 생김
