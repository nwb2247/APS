lst = list(input().rstrip())
ans = 10
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        ans += 5
    else:
        ans += 10
print(ans)
