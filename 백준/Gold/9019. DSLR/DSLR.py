from collections import deque
import sys

fs = [[(x*2)%10000, (x+9999)%10000, (x%1000)*10 + x//1000, x//10 + (x%10)*1000] for x in range(10000)]
cs = ["D", "S", "L", "R"]

TC = int(input())

for _ in range(TC):
    visited = [False]*10000
    s, e = map(int, input().split())
    q = deque()
    q.append((s, ""))
    ans = 0
    while len(q) != 0:
        val, path = q.popleft()
        if val == e:
            ans = path
            break
        if visited[val]:
            continue
        visited[val] = True
        for i, nval in enumerate(fs[val]):
            if visited[nval]:
                continue
            q.append((nval, path + cs[i]))
    print("".join(ans))
