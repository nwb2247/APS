N = int(input())
go = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(len(ans)-go[i], i+1)
print(*ans)
