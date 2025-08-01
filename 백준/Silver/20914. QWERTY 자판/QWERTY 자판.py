from collections import deque

adj = {}
adj["Q"] = ("W", "A")
adj["W"] = ("Q", "A", "S", "E")
adj["E"] = ("W", "S", "D", "R")
adj["R"] = ("E", "D", "F", "T")
adj["T"] = ("R", "F", 'G', 'Y')
adj['Y'] = ('T', 'G', 'H', 'U')
adj['U'] = ('Y', 'H', 'J', 'I')
adj['I'] = ('U', 'J', 'K', 'O')
adj['O'] = ('I', 'K', 'L', 'P')
adj['P'] = ('O', 'L')
adj['A'] = ('Q', 'W', 'S', 'Z')
adj['S'] = ('W', 'E', 'D', 'X', 'Z', 'A')
adj['D'] = ('E', 'R', 'F', 'C', 'X', 'S')
adj['F'] = ('R', 'T', 'G', 'V', 'C', 'D')
adj['G'] = ('T', 'Y', 'H', 'B', 'V', 'F')
adj['H'] = ('Y', 'U', 'J', 'N', 'B', 'G')
adj['J'] = ('U', 'I', 'K', 'M', 'N', 'H')
adj['K'] = ('I', 'O', 'L', 'M', 'J')
adj['L'] = ('O', 'P', 'K')
adj['Z'] = ('A', 'S', 'X')
adj['X'] = ('Z', 'S', 'D', 'C')
adj['C'] = ('X', 'D', 'F', 'V')
adj['V'] = ('C', 'F', 'G', 'B')
adj['B'] = ('V', 'G', 'H', 'N')
adj['N'] = ('B', 'H', 'J', 'M')
adj['M'] = ('N', 'J', 'K')

TC = int(input())
for _ in range(TC):
    st = input().rstrip()
    N = len(st)
    ans = 0
    for i in range(N-1):
        q = deque()
        visited = [0]*26
        q.append(st[i])
        visited[ord(st[i])-ord("A")] = 1
        while q:
            cur = q.popleft()
            if cur == st[i+1]:
                break
            for nxt in adj[cur]:
                if visited[ord(nxt)-ord("A")] == 0:
                    visited[ord(nxt) - ord("A")] = visited[ord(cur)-ord("A")]+2
                    q.append(nxt)
        ans += visited[ord(st[i+1]) - ord("A")]
    print(ans+1)
