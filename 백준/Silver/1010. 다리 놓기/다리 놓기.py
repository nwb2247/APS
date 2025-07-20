import sys
import math

for _ in range(int(input())) :
    line = sys.stdin.readline().split()
    print(math.comb(int(line[1]), int(line[0])))