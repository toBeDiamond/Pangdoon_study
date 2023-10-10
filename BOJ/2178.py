from collections import deque                            # deque 선언

N, M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]          # 2차원 배열을 받아 주기
miro = [[0] * M for _ in range(N)]                          # 2차원 배열과 똑같은 크기의 0으로 이루어 진 배열
Q = deque()                                                 # deque() 로 만들어 진 Q
di = [0, -1, 0, 1]                                          # 4방향 탐색
dj = [-1, 0, 1, 0]
Q.append((0, 0))                                            # deque 에 시작 점의 위치를 넣어 준다.
miro[0][0] = 1                                              # 0으로 이루어 진 배열에 시작 점에 visited 체크 해준다.

while Q:                                                    # Q가 있는 동안
    tmp = Q.popleft()                                       # 빼 내준다, 빼내준 것을 tmp 에 담는다.
    for i in range(4):                                      # 4방향 탐색
        ni = tmp[0] + di[i]
        nj = tmp[1] + dj[i]
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 1:    # 범위를 벗어 나지 않고 갈수 있는 길이면
            board[ni][nj] = 2                                     # 2로 바꿔 주고
            miro[ni][nj] = miro[tmp[0]][tmp[1]] + 1               # 이전 거리의 + 1 만큼 값을 넣어 준다.
            Q.append((ni, nj))                                    # Q에 갔던 길을 넣어 준다. ( 다시 그 길을 바탕으로 4방향 탐색 해서 나아 간다 )

print(miro[N-1][M-1])    # miro 에는 얼마만에 거기에 도착했는지 값이 적혀있다. 그래서 miro의 마지막 도착점의 인덱스를 넣어서 값을 나오게 한다.