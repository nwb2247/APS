"""

" ~~~~~~~~~~~~~~~~~그 값이 0이면 학생의 만족도는
0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다."

0, 1 이면 1이 아니라,
0이면 0, 1이면 1

[요약평]
[1]
문제를 꼼꼼히 읽는 것을 떠나서,
새롭게 읽을 수 있어야한다. (전체화면으로 전환, 확대, 축소, 한글자씩 마음속으로 또는 소리 안나게 입모양으로 읽어보기)

[2]
평소에 실수하는 부분이 아니라고 해서, 시험에서도 그 실수를 안하는건 아니다...
평소에 하던 실수가 아닐 수도 있다고 생각하고, 완전히 새로운 마음으로 다시 생각

[3]
코드를 갈아엎을 시간을 너무 짧게 남겨둬서, 문제를 한 번 더 꼼꼼히 읽을 시간을 확보하지 못함
이러면 다시 푸는 의미가 퇴색됨.. (처음보다 더 꼼꼼히 읽을 시간 까지 고려해서 시간을 남겨두자)
    => 빠르게 푸는 것이 중요한 이유

[4]
첫 제출에 틀렸다고 해서 너무 당황하지 말자
디버깅 시간이 충분히 남아있다면 풀때보다 더 차분한 마인드로 확인하기,
(차분하지 못하면 오히려 더 못찾는다.)

[5]
점수 규칙의 공식을 준 것이 아닌 이상
각 상황에 대해 하드 코딩 하자 (쓰면서라도 한번 더 꼼꼼히 읽을 수 있도록 하기 위해)

[타임라인]
이해 및 구상 : 6분
구현 : 13분
디버깅 : 81분 이상 + (저녁시간 10분
-----
타임 오버

[이해 및 구상]

[구현]
-) 자료형 선택이 명확하지는 못했음 (order + favlst(list[set()]) 으로 관리했다면 좋았을듯
-) pos, pos2, d 등 변수명도 모호
-) 정렬할 필요 없었긴 했음 (확실히 한다는 측면에 나쁘진 않음)
+) 구현 과정에서 각 단계별로 함수화하려던 것을 수정했지만, 문제 없음을 확인하고 잘 바꿨음

[디버깅]
-) [요약평]과 동일

"""

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)


def seat(num, sset):
    pos = []
    mx = -1
    for cr in range(N):
        for cc in range(N):
            if arr[cr][cc] != 0:
                continue
            cnt = 0
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if oob(nr, nc):
                    continue
                if arr[nr][nc] in sset:
                    cnt += 1
            if cnt > mx:
                pos = [(cr, cc)]
                mx = cnt
            if cnt == mx:
                pos.append((cr, cc))  # nr아닌 cr임
    # print(mx)
    # print(pos)

    if len(pos) == 1:
        cr, cc = pos[0]  # pos[0]에서 가져와야함
        arr[cr][cc] = num
        return

    # 2단계
    pos2 = []  # 이름을 pos로 하면 위와 겹쳐서 안됨...
    mx = -1
    for cr, cc in pos:
        cnt = 0
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] == 0:
                cnt += 1
        if cnt > mx:
            pos2 = [(cr, cc)]
            mx = cnt
        if cnt == mx:
            pos2.append((cr, cc))

    if len(pos2) == 1:
        cr, cc = pos2[0]  # pos[0]에서 가져와야함
        arr[cr][cc] = num
        return

    # 3단계

    # print(pos2)

    pos2.sort(key=lambda x: (x[0], x[1]))
    cr, cc = pos2[0]
    arr[cr][cc] = num
    return


N = int(input())
arr = [[0] * N for _ in range(N)]
d = dict()
for _ in range(N * N):  # 1부터 시작해야함
    num, *(fav) = map(int, input().split())
    sset = set(fav)
    d[num] = sset

    seat(num, sset)
    # for l in arr:
    #     print(l)
    # print()

ans = 0
for cr in range(N):
    for cc in range(N):
        cnt = 0
        num = arr[cr][cc]
        sset = d[num]
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if oob(nr, nc):
                continue
            if arr[nr][nc] in sset:
                cnt += 1
        if cnt == 0:  # (D) : 0일때 1을 더해줌 (문제를 잘 못 읽음)
            ans += 0
        elif cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
print(ans)
