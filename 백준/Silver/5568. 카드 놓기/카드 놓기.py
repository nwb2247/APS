"""
[조건]
N<=10 장 카드에서 K장 선택하고 나란히 정수 만들기
2<=K<=4

[목표]
만들 수 있는 정수의 갯수 set으로 처리 후 len(sset)

[아이디어]
(10-2)!

"""
def dfs(depth): # depth : 직전까지 넣은 카드 수, st 현재까지 추가된 문자열

    if depth == K:      # 종료 조건 (K개를 모두 골랐다면)
        ansset.add("".join(ans))
        return # (D) 종료 조건에서 return 안해줬음...

    for i in range(N):  # 아직 넣지 않은 카드 고르기
        if visited[i] == 0:
            visited[i] = 1
            ans.append(lst[i])
            dfs(depth+1)
            visited[i] = 0
            ans.pop()

N = int(input())
K = int(input())


lst = [input() for _ in range(N)]
# print(lst)
N = len(lst)
visited = [0]*N
ans = []
ansset = set()
dfs(0)
print(len(ansset))