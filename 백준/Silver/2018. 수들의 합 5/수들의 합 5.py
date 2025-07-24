N = int(input())
cnt = 0 # 방법의 합계
for i in range(1, N+1) : # 1부터 시작
    j = i
    sm = 0
    while sm < N :  # 계속 더해서 크거나 같아질 때까지 다음 수를 더해줌
        sm += j
        j += 1
    if sm == N :    # 마지막 수까지 더한 합이 정확히 N과 일치하면 cnt 추가 (더 크다면 아무것도 수행 안함)
        cnt += 1

print(cnt)
