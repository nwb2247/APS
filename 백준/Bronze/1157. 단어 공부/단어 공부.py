# 1157

import sys
input = sys.stdin.readline

text = input().rstrip().upper()

a = list(set(text))

d = dict(zip(a, [0]*len(a)))

for t in text :
  d[t] += 1

M = 0
n = 1
ka = None
for k, v in d.items() :
  if v > M :
    n = 1
    M = v
    ka = k
  elif v == M :
    n += 1

if n != 1 :
  print("?")
else :
  print(ka)