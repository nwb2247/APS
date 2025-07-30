"""
A->B으로 진행하면 경우의 수가 너무 많음
또한 B가 최대 10^9이므로 visited 배열을 사용할 수 없음
B->A로 진행하면서 (cur-1)/10, cur/2가 정수가 되는 경우만 큐에 삽입
"""


from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((B,0))
ans = -1
while q:
    cur, dist = q.popleft()
    if cur == A:
        ans = dist
        break
    adjs = []
    if cur%2 == 0:
        adjs.append(cur//2)
    if (cur-1)%10 == 0:
        adjs.append((cur-1)//10)

    for nxt in adjs:
        if nxt >= A:
            q.append((nxt, dist+1))

if ans != -1:
    ans += 1

print(ans)