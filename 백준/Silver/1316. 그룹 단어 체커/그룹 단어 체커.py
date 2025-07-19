import sys

N = int(sys.stdin.readline())

cnt = 0
for _ in range(N) :
    a = [False]*26
    s = sys.stdin.readline().rstrip()
    cur = " "
    for c in s :
        if cur == c : continue
        if a[ord(c)-ord('a')] :
            cnt += 1
            break
        else :
            a[ord(c)-ord('a')] = True
            cur = c
print(N-cnt)