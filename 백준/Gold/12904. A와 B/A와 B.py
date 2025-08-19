# """
# """
S = list(input())
T = list(input())

ans = False
while len(S) < len(T):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T = T[::-1]
if len(S) == len(T) and S == T:
    print(1)
else:
    print(0)