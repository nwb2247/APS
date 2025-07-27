N = int(input())
# is_connected[i][i] == False 자기 자신은 다른 정점 들렸다가 돌아올수 있는 경우에 True가 됨
is_connected = [list(map(lambda x: False if x == '0' else True, input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            """
            플로이드 워셜 응용
            False : 연결 안됨 / True : 연결됨
            is_connected[i][j] or (is_connected[i][k] and is_connected[k][j])
            이미 연결 되어있거나 k를 경유해 갈수 있는 경우에 True가 됨
            """
            is_connected[i][j] = is_connected[i][j] or (is_connected[i][k] and is_connected[k][j])
for i in range(N):
    print(*map(int, is_connected[i]))
