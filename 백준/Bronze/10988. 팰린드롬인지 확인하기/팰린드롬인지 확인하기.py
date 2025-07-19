import sys

s = list(sys.stdin.readline().rstrip())

if s == s[::-1] :
    print(1)
else :
    print(0)