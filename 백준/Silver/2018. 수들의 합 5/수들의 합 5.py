N = int(input())

ans = 0
sm = 0
start = 0   # 연속 숫자의 시작 숫자
for i in range(1, N+1) :
    sm += i         # 현재 숫자(i) 를 추가
    if sm > N :     # 더했더니 N보다 크다면 작아질 때까지 연속된 앞부분 빼줌
        while sm > N :
            sm -= start
            start += 1  # 맨 앞 숫자를 빼고 그 다음 숫자로 갱신
    if sm == N :    # 뺀 결과가 N과 똑같다면 (N보다 작지 않다면) ans +=1
        ans += 1
print(ans)

# N = int(input())
# cnt = 0 # 방법의 합계
# for i in range(1, N+1) : # 1부터 시작
#     j = i
#     sm = 0
#     while sm < N :  # 계속 더해서 크거나 같아질 때까지 다음 수를 더해줌
#         sm += j
#         j += 1
#     if sm == N :    # 마지막 수까지 더한 합이 정확히 N과 일치하면 cnt 추가 (더 크다면 아무것도 수행 안함)
#         cnt += 1
#
# print(cnt)
