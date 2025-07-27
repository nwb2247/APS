N = int(input())
M = int(input())

st = input().rstrip()
s = 0 # P_l의 시작 인덱스
cnt = 0 # P_N의 갯수
while s < M:
    if st[s] != "I":
        s += 1
        continue
    # I로 시작한다면 P_l의 l을 구함
    l = 0
    while s+2*l+1<M and s+2*l+2<M and st[s+2*l+1:s+2*l+3] == "OI":
        l += 1
    # l이 최대가 되는 P_l을 구하면 l-N+1을 cnt에 더해줌 (ex) P_4에는 P_2이 3개 들어감
    cnt += max(0, l-N+1)
    # s를 P_l이 끝나는 다음 인덱스로 변경해줌
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
