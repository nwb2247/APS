import sys

N, X = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
output = []
for n in nums :
    if n < X :
        output.append(str(n))
print(" ".join(output))