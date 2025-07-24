"""
이분 탐색
가능한 답의 범위가 0~10^9이므로 완전 탐색으로는 시간 오버
이분 탐색을 이용한다.
"""
N, M = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = 1000000000

# 높이 h에 의해 잘린 나무 길이의 합
def cnt(h) :
    sm = 0
    for num in lst :
        sm += max(0, num-h)
    return sm

while left <= right :
    mid = (left+right)//2
    if cnt(mid) < M :
        right = mid-1
    # 등호를 right 갱신 조건(if) left 갱신 조건(else) 중 어디에 넣을지 생각해야 함
    # 가능한 가장 큰 h를 구해야 하므로 right가 정답이 되도록 해야하는데,
    # 이를 위해서 left 갱신에 조건에 등호 범위를 넣어야 한다.
    else :  # cnt(mid) >= M
        left = mid+1
print(right)
