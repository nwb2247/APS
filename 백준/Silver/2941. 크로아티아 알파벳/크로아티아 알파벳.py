import sys

s = sys.stdin.readline().rstrip()

rep = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in rep :
    s = s.replace(c, "1")
print(len(s))
