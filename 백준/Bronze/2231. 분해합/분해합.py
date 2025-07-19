import sys

N = int(sys.stdin.readline())

sol = 0
for j in range(N) :
    sum = 0
    i = j
    while i != 0 :
        sum += i%10
        i //= 10
    if sum+j == N :
        sol = j
        break
print(sol)