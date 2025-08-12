"""
[조건]
크레인 수 N<=50
박수 수 M <= 10000
값 <=100_0000

1초에 박스 하나씩,
크레인은 무게제한 있음
모든 크레인은 동시에 옮길 수 있음

[목표]
최소시간 구하기

모든 박스를 옮길 수 없다면 ex) 모든 크레인 무게제한보다 큰 화물이 있는 경우
-1출력

[접근]
크레인 무게제한 오름차순 정렬
박스 내림차순 정렬
박스에서 하나씩 꺼내서 넣을 수 있는 크레인 찾기, 다음 크레인보다 len이 적으면 넣고, 같으면 다음크레인으로 넘김
(크레인의 개수가 박스 수보다 더 적으므로 이방법 수행)

가장 큰 크레인을 우선순위로 하지만, loaded를 최대한 일정하게끔함
=> 넣을 수 있는 딱 맞는 크레인이 넣되, 이미 지금 크레인과 다음 크레인 (더 큰) 크레인의 높이가 같다면 다음 크레인으로 넘김
"""
def solve():
    N = int(input())
    climit = list(map(int, input().split()))
    climit.sort()
    climit = climit

    M = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort(reverse=True)



    loaded = [0]*N + [10001]

    for box in boxes:

        for i in range(N):  # i 크레인 인덱스
            if box > climit[i] or loaded[i+1] == loaded[i]:
                continue
            else:
                loaded[i] += 1
                break


        else:   # 어디에도 넣을 수 없으면 break
            return -1

    # print(climit)
    # print(boxes)
    # print(loaded)
    return loaded[N-1]

print(solve())
