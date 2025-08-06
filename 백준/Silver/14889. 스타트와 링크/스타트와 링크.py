"""
[조건]
N 짝수 <= 20
누구랑 같은 팀 하는 가에 따라 시너지

[목표]
시너지가 최소가 되도록
시너지 차이의 최소값


[아이디어]
10개 고르면 나머지 10개는 반대팀 20C10?
-> 시너지는 한명 빠지고 한명 들어갈때 완전히 달리지므로 가지치기 어려움
"""

def cal():
    spower = 0
    lpower = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if star[i] == 1 and star[j] == 1:
                spower += (arr[i][j] + arr[j][i])
            elif star[i] == 0 and star[j] == 0:
                lpower += (arr[i][j] + arr[j][i])
    return abs(spower-lpower)

def dfs(depth, start): # depth : 직전까지 star에 넣은 사람 수 , start: star에 넣기를 고려할 인덱스
    global ans
    if depth == N//2:
        ans = min(ans, cal())
        return

    for selected in range(start, N):
        star[selected] = 1
        dfs(depth+1, selected+1)
        star[selected] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
star = [0]*N
ans = 100*N*N

dfs(0, 0)
print(ans)