"""
질문 100개 이히

3자리이므로 1000개 (0안쓰므로 그 이하)

=> 완전탐색
"""

def check(st, base): # 각 질문에 대해 스크라이크와 볼 확인
    strike = 0
    ball = 0
    for i, c in enumerate(st):
        if c == base[i]:    # 위치가 정확히 일치한다면
            strike += 1
        elif c in base:     # 위치는 다르지만 들어있다면
            ball += 1
    return strike, ball

def dfs(depth):

    if depth == 3:      # 숫자 3자리 완성되면
        st = "".join(stlst)
        for q, strike, ball in lst: # 각 질문에 대해 
            if not (check(st, q) == (strike, ball)):    # 스트라이크, 볼 다른 것 있으면 종료
                break
        else:               # break 되지 않았다면 정답후보이므로 추가
            ans.append(st)
        return

    for i in range(1, 10):
        if visited[i] == 0:
            visited[i] = 1
            stlst[depth] = str(i)
            dfs(depth+1)
            visited[i] = 0

N = int(input())

lst = [()]*N
for i in range(N):
    ip = input().split()
    lst[i] = ip[0], int(ip[1]), int(ip[2])

stlst = [""]*3
visited = [0]*10
ans = []

dfs(0)

print(len(ans))




