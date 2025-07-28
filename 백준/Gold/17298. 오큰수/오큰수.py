"""
스택으로 풀어보기 (시간 복잡도 O(N)?)

오큰수 찾자마다 바로 pop하므로
각 인덱스에 대해 push pop이 각한번씩만 이루어지므로 O(N)
"""
N = int(input())
lst = list(map(int, input().split()))
stk = []
ans = [-1]*N    # 발견하지 못한 경우 -1출력하므로 -1로 초기화
for i in range(N):
    while len(stk) != 0 and lst[stk[-1]] < lst[i]: # lst[i]가 오큰수가 되는 모든 값을  pop
        ans[stk.pop()] = lst[i] # ans에 기록
    stk.append(i) # i도 stk에 push
print(*ans)

