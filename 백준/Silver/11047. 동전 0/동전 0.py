"""
동전 N 종류, 동전은 필요한 만큼 충분히 가지고 있음,
lst[i]는 lst[i-1]의 배수
따라서 lst[i]원은 항상 lst[i-1]보다 lst[i]로 사용할때 더 적게 사용할 수 있다
=> 큰 동전부터 먼저 쓰기
"""

N, K = map(int, input().split()) # 동전종류수, K원
lst = [int(input()) for _ in range(N)]

cnt = 0 # 사용한 동전 개수
for val in lst[::-1]:   # 큰 동전부터
    cnt += K//val       # 몫을 cnt에 추가
    K %= val            # 나머지가 K가 됨
    if K == 0:          # K가 0원이 됐다면 (이번 동전 종류 사용으로)
        break           # 종료

print(cnt)