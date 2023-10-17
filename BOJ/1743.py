from collections import deque                  # deque 사용을 하기 위한 것
def bfs():                                     # bfs 함수 정의
    global count                               # count를 쓰기 위해서
    while Q:                                   # Q가 빌때까지
        tmp = Q.popleft()                      # 빼줌
        count += 1                             # bfs가 실행될때마다 음식물 쓰레기 개수를 올림
        for k in range(4):                     # 4방향 탐색
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:   # 범위를 안벗어나고, visited도 0이고 arr도 음식물쓰레기 인 곳으로만
                visited[ni][nj] = 1         # visited 체크
                Q.append((ni, nj))          # 그곳을 Q에 넣어준다.



N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(K):                           # 음식물 쓰레기 그래프로 만들어주기
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1                        # 인덱스 값을 맞춰주기 위해서 -1씩 해주었다.
                                             # ex) 1, 1 자리에 있는 음식물 쓰레기는 0, 0에 있다.

result = 0                                   # 답을 담아줄 결과 값
Q = deque()
for x in range(N):
    for y in range(M):                       # 2중 포문을 돌면서
        if arr[x][y] == 1 and visited[x][y] == 0:      # 음식물 쓰레기이고 방문한 적이 없는 음식물 쓰레기라면
            count = 0                                  # count를 초기화 해줄 위치
            Q.append((x, y))                           # 음식물 쓰레기 위치를 넣어준다.
            visited[x][y] = 1                          # visited 체크를 해준다.
            bfs()
            if count > result:                         # 만일 음식물 쓰레기 더미 양의 개수가 result 보다 크면 바꿔준다.
                result = count

print(result)

