"""
[조건]
가능한 최대의 총예산
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여
그 이상인 예산요청에는 모두 상한액을 배정한다.
상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

[목표]
배정된 예산들 중 최대값
총예산M 이 이미 모든 예산의 합을 넘으면 상한액 필요 x
but, 모든 예산의 합이 M을 넘는다면,
상한액이 최대가 최도록해야함 (-> 총합이 최대가 되면서 M을 넘지 않도록)

[접근]

이진탐색, 처음 end 값을 최대 정수로 하고
합이 M을 넘지 않는지 확인
넘으면 e을 내려가고
넘지 않으면 s를 올려감

"""

def cal_sm(mx):
    return sum(map(lambda x: mx if x>mx else x, lst))


def binary_search():
    s, e = 1, max(lst)  # 예산들중 가장 큰값으로 e를 초기화
    ans = -1
    while s <= e:
        m = (s+e)//2
        sm = cal_sm(m)
        if sm <= M: # 상한을 둔 예산들의 합계가 M보다 작거나 같으면 s를 m보다 더 늘릴 여지가 존재
            ans = m # m이 정답이 될 수 있으므로 기록
            s = m+1
        else:       # M를 초과하면 e를 m보다 낮춰야함
            e = m-1
    return ans


N = int(input())
lst = list(map(int, input().split()))
M = int(input())
print(binary_search())
