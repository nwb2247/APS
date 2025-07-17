import sys

N = int(input())

output = []
for i in range(N) :
    output.append(str(sum(map(int, sys.stdin.readline().split()))))
print('\n'.join(output))