from collections import deque
def bfs(v):
    global count

    while Q:
        count += 1
        tmp = Q.popleft()
        visited[tmp[0]][tmp[1]] = 1
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                bfs((ni, nj))



N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(K):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    Q = deque()
    result = 0

for _ in range(N):
    count = 0
    for x in range(N):
        for y in range(M):

            if arr[x][y] == 1:
                Q.append((x, y))
                bfs((x, y))
                if count > result:
                    result = count

print(result)
print(arr)
