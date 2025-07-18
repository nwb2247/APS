import sys

r = [False]*42
for _ in range(10) :
    r[int(sys.stdin.readline())%42] = True
print(r.count(True))