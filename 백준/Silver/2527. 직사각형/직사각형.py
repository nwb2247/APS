for _ in range(4) :
    l1, d1, r1, u1, l2, d2, r2, u2 = map(int, input().split())
    if l2 > r1 or r2 < l1 or d2 > u1 or u2 < d1:
        print("d")
    elif ((l1, d1) == (r2, u2) or (r1, d1) == (l2, u2)
          or (r1, u1) == (l2, d2) or (l1, u1) == (r2, d2)):
        print("c")
    elif l2 == r1 or r2 == l1 or d2 == u1 or u2 == d1:
        print("b")
    else:
        print("a")