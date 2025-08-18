"""
나이트 투어
1. 모든 칸 한번씩만 전부 방문
2. 시작점으로 되돌아와야함
체스판에 존재하는 칸만 주어짐

확인할 것
invalid
나이트 경로가 올바르지 않음.
왔던데 또방문
모든 부분방문하지 않음
마지막에서 처음으로 돌아오지 못함
"""
lst = [()]*36
for i in range(36):
    a, n = tuple(input())
    lst[i] = (int(n)-1, ord(a) - ord("A"))

def valid(cur, nxt):
    cr, cc = cur
    nr, nc = nxt
    if abs(cr-nr) == 1 and abs(cc-nc) == 2:
        return True
    elif abs(cr-nr) == 2 and abs(cc-nc) == 1:
        return True
    else:
        False

def solve():
    """
    나이트 경로가 올바르지 않음.
    왔던데 또방문 => 모든 부분방문하지 않음
    마지막에서 처음으로 돌아오지 못함
    """
    sset = set(lst)
    if len(sset) != 36:
        return False
    if not valid(lst[0], lst[-1]):
        return False

    for i in range(35):
        cur = lst[i]
        nxt = lst[i+1]
        if not valid(cur, nxt):
            return False

    return True

if solve():
    print("Valid")
else:
    print("Invalid")
