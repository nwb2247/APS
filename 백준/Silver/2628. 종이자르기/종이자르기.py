N, M = map(int, input().split())
T = int(input())
rs = []
cs = []
for _ in range(T):
    d, pos = map(int, input().split())
    if d == 0:
        rs.append(pos)
    else:
        cs.append(pos)

rs.append(0)
rs.append(M)
rs.sort()
cs.append(0)
cs.append(N)
cs.sort()
# print(rs, cs)
ans = 0
r_mx = 0
c_mx = 0
for i in range(len(rs)-1):
    r_mx = max(r_mx, rs[i+1]-rs[i])
for i in range(len(cs)-1):
    c_mx = max(c_mx, cs[i+1]-cs[i])
print(r_mx*c_mx)