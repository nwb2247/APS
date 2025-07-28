"""
스택으로 풀어보기
"""
N = int(input())
lst = [0] + list(map(int, input().split())) # 탑 idx는 1번부터 시작
stk = []    # 탑의 idx를 저장하는 stk (ans에 저장하기 위함)
ans = [0]*(N+1)
for i in range(N,0,-1):     # 레이저를 왼쪽부터 쏘므로 역방향으로 순회
    while len(stk) != 0 and lst[stk[-1]] < lst[i]: # stk에 더 낮은 높이 탑이 없을 때까지 pop
        # i가 더 크다는 것은 i가 수신하는 탑이라는 뜻
        ans[stk.pop()] = i  # ans 배열에 저장
    stk.append(i)           # i도 stk에 push
print(*ans[1:])             # 1번부터 왼쪽의 어떤 탑이 수신하는지 출력