import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().split())

x = int((e*c-b*f) / (a*e-b*d))
y = int((-c*d+a*f) / (a*e-b*d))

print(x, y)