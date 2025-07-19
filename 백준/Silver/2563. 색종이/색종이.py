import sys

paper = [[False for j in range(100)] for i in range(100)]

N = int(sys.stdin.readline())

for _ in range(N) :
    r, c = map(int, sys.stdin.readline().split())
    for i in range(r,r+10) :
        for j in range(c,c+10) :
            paper[i][j] = True

print(sum(map(sum, paper)))

