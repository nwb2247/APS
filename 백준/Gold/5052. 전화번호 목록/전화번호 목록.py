"""
반례
1
2
3333
333
-> NO 나와야하는데 Yes나옴
"""

def solve():
    N = int(input())
    stlst = [input() for _ in range(N)]
    trie = {}
    for st in stlst:
        cur = trie
        for i in st:
            if i not in cur:
                cur[i] = {}
            elif len(cur[i]) == 0:
                return False
            cur = cur[i]
        if len(cur) != 0:
            return False
    return True

TC = int(input())
for _ in range(TC):
    if solve():
        print("YES")
    else:
        print("NO")