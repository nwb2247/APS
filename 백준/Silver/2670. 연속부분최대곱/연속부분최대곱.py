import sys

N = int(sys.stdin.readline())
arr = [float(sys.stdin.readline()) for _ in range(N)]

cur = arr[0]
sol = cur
for f in arr[1:] :
    cur = max(cur*f, f)
    sol = max(sol, cur)
print(f"{sol:.3f}")

