import sys


a, b, c = map(int, sys.stdin.readline().split())

if a == b and b == c :
    print(10000 + a*1000)
elif a != b and b!= c and c!= a :
    print(max(a,b,c)*100)
elif a == b or a == c :
    print(1000+a*100)
else :
    print(1000+b*100)
