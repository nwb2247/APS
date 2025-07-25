N, M = map(int, input().split())
lst = [0]*M

def recur(start, depth) :
    global N, M, lst # 전역 변수
    if depth == M : # lst 완성시 출력
        print(*lst)
        return
    for i in range(start, N+1) : # start부터 N까지 depth 인덱스에 넣고 재귀 호출
        lst[depth] = i
        recur(i, depth+1)

recur(1, 0)

