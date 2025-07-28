N = int(input())
lst = [int(input()) for _ in range(N)]
cnt = 0 
mx = 0 # 현재까지의 최대값 (최대값보다 작거나 같은 높이는 보이지 않으므로)
# 뒤에서부터 순회
for num in lst[::-1]:
    if num > mx: # 더 높은 것이 발견되면 cnt 추가하고 mx도 갱신
        cnt += 1
        mx = num
print(cnt)