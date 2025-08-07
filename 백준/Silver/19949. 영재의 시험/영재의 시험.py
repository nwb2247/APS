"""

7:32
[조건]
10 문제
3개의 연속된 문제는 답을 같지 않게 함

[목표]
5점 이상일 경우의 수 구하기

[접근]
이미 5개 이상 틀린경우 가지치기

2개의 답 기억하면서 인자로 가져가기

(D) 문제 잘 읽기 (3개의 답이 "연속으로" 나오지 않는 것)


"""

def dfs(depth, wrong, before2, before1):

    global ans

    if wrong>5: # 가지치기 (이미 틀린답 5개 초과)
        return

    if depth == 10:
        ans += 1
        return

    for i in range(1, 6):
        if i == before2 and i == before1:
            continue
        nw = 1 if i != sollst[depth] else 0
        dfs(depth + 1, wrong + nw, before1, i)


sollst = list(map(int, input().split()))
ans = 0
dfs(0, 0, -1, -1)
print(ans)
