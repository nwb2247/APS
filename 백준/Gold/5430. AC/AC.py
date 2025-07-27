from collections import deque

TC = int(input())
for _ in range(TC):
    ops = input().rstrip()
    N = int(input())
    lst = []
    if N != 0:
        lst = list(map(int, input().rstrip()[1:-1].split(",")))
    else:
        input()
    if ops.count("D") > N:
        print("error")
        continue
    deq = deque(lst)
    is_rev = False
    for op in ops:
        if op == "R":
            is_rev = not is_rev
        else:
            if is_rev:
                deq.pop()
            else:
                deq.popleft()

    if is_rev:
        deq.reverse()   # in-place reverse
    print("[", end="")
    print(*deq, sep=",", end="")
    print("]")
