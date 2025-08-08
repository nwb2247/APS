def binary_search(N):
    s, e = 0, N # e는 N으로
    while s<=e:
        m = (s+e)//2
        z = m*m
        if z == N:  # m*m가 N과 같다면 제곱근이므로 출력
            return m
        elif z < N: # N보다 작다면 s를 위로 조정 (m은 답이 아님을 확인했으므로 미포함)
            s = m+1
        else:       # N보다 크다면 e를 아래로 조정 (m은 답이 아님을 확인했으므로 미포함)
            e = m-1
    # 항상 제곱근이 정수로 있는 경우만 주어지므로 while문 도중에 return
    return -1

N = int(input())
print(binary_search(N))