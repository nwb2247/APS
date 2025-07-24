N = 9
lst = [int(input()) for _ in range(N)]
sm9 = sum(lst)  # 9명의 합
found = False
for i in range(N-1) :
    for j in range(i+1, N) :
        if sm9 - lst[i] - lst[j] == 100 :
            found = True
            lst.pop(j)  # 더 나중 인덱스인 j부터 pop해야함 (i부터 pop하면 뒷 인덱스에 영향을 줌)
            lst.pop(i)
            break
    if found : # 찾았으면 2중 for문 종료
        break
print(*sorted(lst), sep="\n")
