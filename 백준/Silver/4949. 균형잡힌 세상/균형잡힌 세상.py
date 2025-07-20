import sys

s = sys.stdin.readline().rstrip()

while s != "." :
    stack = []
    sol = True
    for c in s :
        if c == '[' or c == '(' :
            stack.append(c)
        elif c == ')' :
            if len(stack) != 0  and stack[-1] == '(' :
                stack.pop()
            else :
                sol = False
                break
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                sol = False
                break
    if len(stack) != 0 :
        sol = False
    if sol :
        print("yes")
    else :
        print("no")
    s = sys.stdin.readline().rstrip()