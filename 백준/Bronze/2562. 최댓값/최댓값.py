import sys

order = 0
m = 0
for i in range(1, 10) :
     n = int(sys.stdin.readline())
     if n > m :
         m = n
         order = i
print(m)
print(order)