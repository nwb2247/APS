"""
[조건]
123 가위바위보
같은 카드인 경우 인덱스 작은 쪽이 이김
1번 부터 N번

[목표]
최종 우승자의 인덱스

[접근]
분할정복
1번부터 시작이므로 패딩
~(i+j)//2 / (i+j)//2+1~

"""
def dq(i, j): # 그룹의 시작과 끝 인덱스
    if i == j:
        # 종료 조건 : 그룹의 start == end (사이즈가 한명) 라면 종료
        # 3,4 / 4,5 등의 경우 모두 하나씩으로 나뉘므로 end>start (사이즈가 0)인 경우는 없음
        return i

    lwin = dq(i, (i+j)//2)  # 왼쪽 그룹에서 이긴 사람 (rwin보다 인덱스 작음)
    rwin = dq((i+j)//2+1, j)

    # 1 가위 2 바위 3 보
    if lst[lwin]%3 + 1 == lst[rwin]:    # 오른쪽이 이긴 경우
        return rwin
    else:                               # 왼쪽이 이겼거나 비긴 경우 => 왼쪽의 승리
        return lwin

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    print(f"#{tc} {dq(1, N)}")
