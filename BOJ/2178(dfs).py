def dfs(a, b, cnt):    # dfs 함수(a, b 좌표와 거기까지 온 거리)
    global min_cnt     # 최소 거리를 구해줄 것을 글로벌로 선언해서 가져옴
    if cnt > min_cnt:    # 그 장소까지 온 거리가 이미 최솟값을 넘어섰다면 함수 종료 (가지치기)
        return
    if a == N - 1 and b == M - 1:    # 마지막 종료 지점에 도착을 했다면
        if min_cnt > cnt:    # 그 곳까지 간 길이 최소 거리보다 더 최소라면
            min_cnt = cnt    # 최소 거리를 갱신해준다.
        return
    else:
        for i in range(4):    # 4방향 탐색
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni < N and 0 <= nj < M:    # 범위 넘지않게
                if board[ni][nj] == 1 and visited[ni][nj] == 0:    # 갈수 있는 길이고, 방문했던 적이 없던 길이라면
                    visited[ni][nj] = 1    # visited 체크
                    dfs(ni, nj, cnt + 1)   # visited 체크를 해주면서 그 길로 함수실행, 거리는 + 1 더해준다(한칸 움직였으므로).
                    visited[ni][nj] = 0    # 혹시나 막다른 길을 만나서 나왔다면 다시 이전 갈림길로 돌아가야하기 때문에 visited 체크를 풀어준다.


N, M = map(int, input().split())
di = [0, 1, 0, -1]    # 4방향 탐색
dj = [-1, 0, 1, 0]
board = [list(map(int,input())) for _ in range(N)]    # 2차원 배열을 받아준다.
visited = [[0] * M for _ in range(N)]    # visited 체크를 해줄 0으로 이루어진 2차원 배열
visited[0][0] = 1    # 첫번째 시작점을 체크해준다.
min_cnt = 987654321    # 가지치기 밑 최소 거리를 구해줄 값을 정해준다.
dfs(0, 0, 1)    # 시작점 (0, 0 과 거리) dfs 함수 실행
print(min_cnt)



