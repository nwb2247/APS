"""
백트래킹, 가지치기?

한번 나쁜 수열 만들어졌으면 그 밑에는 뭐가 나와도 나쁜 수열 => 가지치기

"""

def bad(depth): # 나쁜 수열인지 확인
    l = 1
    while depth - 2*l >= 0: # 비교 수열 길이 1씩 늘려가면서 비교
        if ans[depth-2*l:depth-l] == ans[depth-l:depth]: # 같으면 True 반환
            return True
        else:
            l += 1
    return False

def backtracking(depth):

    global is_found

    if is_found: # 가지치기 1 : 답 찾았으면 종료 (하나만 출력하면 되므로)
        return

    if bad(depth): # 가지치기 2: 나쁜 수열이면 더 이상 확인 X
        return
    
    if depth == N:                      # 가치치기 당하지 않고 N까지 왔으면 정답
        print("".join(map(str, ans)))   # 출력
        is_found = True                 # 찾았음을 표시
        return

    for i in range(1, 4): # 가장 작은 수여야 하므로 되도록 1, 2, 3 순으로 넣음
        ans[depth] = i
        backtracking(depth + 1)

N = int(input())
ans = [0]*N
is_found = False
backtracking(0)

# N = 19
# lst = list(range(N))
# print(lst)
# depth = N
# l = 1
# while depth-2*l >= 0:
#     print(lst[depth-2*l:depth-l], lst[depth-l:])
#     l += 1
