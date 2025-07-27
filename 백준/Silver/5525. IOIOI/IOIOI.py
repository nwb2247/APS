N = int(input())
M = int(input())

st = input().rstrip()
s = 0
cnt = 0
while s < M:
    if st[s] == "O":
        s += 1
        continue
    l = 0
    while s+2*l+1<M and s+2*l+2<M and st[s+2*l+1:s+2*l+3] == "OI":
        l += 1
    cnt += max(0, l-N+1)
    s = s+2*l+1
print(cnt)


# # 1차 시도
# N = int(input())
# M = int(input())
# pat = "I"+"OI"*N
# st = input().rstrip()
# cnt = 0
# while len(st) > 0:
#     k = st.find(pat)
#     if k == -1:
#         break
#     cnt += 1
#     st = st[k+1:]
# print(cnt)
