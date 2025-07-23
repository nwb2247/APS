L = int(input())
N = int(input())

lst = [0]*(L+1)

f = 0
fv = 0
for i in range(1,N+1) :
    P, K = map(int, input().split())
    if K-P+1 > fv :
        fv = K-P+1
        f = i
    for j in range(P, K+1) :
        if lst[j] == 0 :
            lst[j] = i
cnt = [0]*(N+1)
for i in lst :
    cnt[i] += 1
print(f)
print(cnt[1:].index(max(cnt[1:]))+1)

