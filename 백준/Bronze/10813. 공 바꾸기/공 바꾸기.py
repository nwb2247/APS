# 10813

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

now = list(range(1, n + 1))

while m :
  i, j = list(map(int, input().split()))
  temp = now[i-1]
  now[i-1] = now[j-1]
  now[j-1] = temp
  m -= 1

print(" ".join(list(map(str,now))))