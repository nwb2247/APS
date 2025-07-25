N = int(input())
lst = list(map(int, input().split()))
s = 0
e = 1
cnts = [0]*10
cnts[lst[0]] = 1
mx = 0
while s < N and e < N:
    if 10 - cnts.count(0) <= 2:
        mx = max(mx, e - s)
        cnts[lst[e]] += 1
        e += 1
    else:
        cnts[lst[s]] -= 1
        s += 1
if 10 - cnts.count(0) <= 2:
    mx = max(mx, e - s)

print(mx)
