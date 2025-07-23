import math
N = int(input())

lst = [0]*(N+1)

for i in range(1, N+1) :
    M = math.floor(i**0.5)
    for j in range(1, M+1) :
        if i%j == 0 :
            lst[i] += 1

print(sum(lst))