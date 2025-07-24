N = int(input())

lst = [float(input()) for _ in range(N)]

mx = lst[0]
cur = mx
for f in lst[1:] :
    if f > cur*f :
        cur = f
    else :
        cur *= f
    mx = max(mx, cur)
print(f"{mx:.3f}")