from collections import deque

TC = int(input())
for _ in range(TC):
    ops = input().rstrip()
    N = int(input())
    # pop외 별다른 연산 없으므로 굳이 int로 바꿔주지 않아도 됨
    lst = list(input().rstrip()[1:-1].split(","))
    # D 연산이 길이보다 크다면 error
    if ops.count("D") > N:
        print("error")
        continue
    # deque에 넣어줌
    deq = deque(list(lst))
    is_rev = False
    for op in ops:
        # R이 들어오면 실제로 reverse하지 않고 pop 위치을 바꿔줌
        if op == "R":
            is_rev = not is_rev
        else:
            if is_rev:
                deq.pop()
            else:
                deq.popleft()

    if is_rev:
        deq.reverse()   # in-place reverse
    print("[", ",".join(deq), "]", sep="")
