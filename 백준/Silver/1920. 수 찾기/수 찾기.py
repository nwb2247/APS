def binary_search(t):
    s, e = 0, N - 1
    while s <= e:
        m = (s+e)//2
        if lst[m] == t:
            return 1        # 찾았다면 1 반환
        elif lst[m] < t:
            s = m+1         # m이 목표값보다 작다면 => s를 올려 조정 (m은 정답이 아니므로 미포함)
        else:   # lst[m] > t
            e = m-1         # m이 목표값보다 크다면 => e를 낮춰 조정 (m은 정답이 아니므로 미포함)
    return 0    # 못찾고 s>e 됐다면 종료


N = int(input())
lst = list(map(int, input().split()))
lst.sort() # 이진 탐색 사용을 위해서 정렬 필요

M = int(input())
query = list(map(int, input().split()))
for q in query:
    print(binary_search(q))


